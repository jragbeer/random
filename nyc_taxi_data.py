import numpy as np
import pandas as pd
import urllib
import sqlite3
import datetime
import pickle
import dateutil
from pprint import pprint
import holidays
import logging
import gc
import io
import dask
import copy
from dask.distributed import Client, progress
import dask.dataframe as dd
import os
from multiprocessing import Pool
from tqdm import tqdm
from tqdm import tqdm

switch = {"Green": "Green_Taxi_Trip_Data",
          "Yellow": "Yellow_Taxi_Trip_Data",
          "FHV": "For_Hire_Vehicles_Trip_Data",
          "HVFHV": "HV_FHV", }
buffer = io.StringIO()

# db = 'NYC_Taxi_Data.db'
# path2 = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
# conn = sqlite3.connect(path2 + db)

# df = pd.read_sql('select PULocationID, DOLocationID, passenger_count, pickup_hour from Trip_Data where pickup_hour >= 18 and pickup_hour < 21', conn)
# print(df.sample(26).to_string())
# print(datetime.datetime.now()-timee)
# print('over')
# df_one = {}

#
ny_holidays = holidays.CountryHoliday("US", state='NY')
timee = datetime.datetime.now()
path = os.getcwd().replace('\\','/') + "/data/"
db = 'NYC_Taxi_Data.db'
conn = sqlite3.connect(path + db)
conn.text_factory = lambda b: b.decode(errors='ignore')
logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(message)s',
                    handlers=[logging.FileHandler(path + "log.txt"), logging.StreamHandler()])
logging.info(timee)
col = 'yellow'
all_points = np.asarray(pd.read_csv(path + 'zone_lookup.csv')['LocationID'])

# util and functions no longer used
def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()
def create_initial_database_from_csv(year, colour):
    # create database and add data to it
    try:
        print(year, colour)
        fp = path + f"{year}_{switch[colour]}.csv"
        dfcolumns = pd.read_csv(fp, nrows=1)
        df_list = []
        data = pd.read_csv(fp, header=None, skiprows=1, usecols=list(range(1, len(dfcolumns.columns))),
                           chunksize=15_000_000, names=dfcolumns.columns, error_bad_lines=False, engine='python')
        n = 1
        for chunk in data:
            print(n)
            df_list.append(initial_data_clean(chunk))
            n += 1

        large_df = pd.concat(df_list)
        if 'fhv' in colour.lower():
            large_df.to_sql(f'{year}_FHV', conn, if_exists='append', index=False)
        else:
            large_df.to_sql(f'{year}_{colour.upper()}', conn, if_exists='replace', index=False)
        print('done', datetime.datetime.now() - timee)

    except Exception as e:
        print(error_handling())
def read_db(tablename, conn_):
    query = "select * from {}".format(tablename)
    df = pd.read_sql(query, conn_, parse_dates=['pickup_datetime', 'dropoff_datetime'])
    return df
def make_season(series):
    array = []
    for x in series:
        new_date = datetime.datetime(2000, x.month, x.day)
        if datetime.datetime(2000, 3, 1) <= new_date < datetime.datetime(2000, 6, 1):
            array.append('spring')
        elif datetime.datetime(2000, 6, 1) <= new_date < datetime.datetime(2000, 9, 1):
            array.append('summer')
        elif datetime.datetime(2000, 9, 1) <= new_date < datetime.datetime(2000, 12, 1):
            array.append('fall')
        else:
            array.append('winter')
    return array

# part one (read from csv, initial clean, save as parquet)
def initial_data_clean(df):
    """
    Make the numeric columns smaller and drop any bad lines.
    :param df: initial NYC Taxi csv data - raw (but column names are changed)
    :return: a df with a few rows dropped and downcasted
    """
    df['dolocationid'] = pd.to_numeric(df['dolocationid'], errors='coerce', downcast='float')
    df['pulocationid'] = pd.to_numeric(df['pulocationid'], errors='coerce', downcast='float')
    df = df.replace([np.inf, -np.inf], np.nan)
    try:
        df = df.dropna(how='any')
    except ValueError as ve:
        print(df.sample(5).to_string())
        print(df[df.isna().any(axis=1)].to_string())
    df['dolocationid'] = pd.to_numeric(df['dolocationid'], errors='coerce', downcast='integer')
    df['pulocationid'] = pd.to_numeric(df['pulocationid'], errors='coerce', downcast='integer')
    df.reset_index(inplace=True, drop=True)
    return df
def readcsv(file):
    """
    This function cleans the column names of the csv file and drops bad rows (via a *initial_data_clean* call).

    :param file: NYC Taxi csv file
    :return: cleaned df
    """
    dfcolumns = pd.read_csv(file, nrows=1)
    # make all of the different col names across files the same
    a = dfcolumns.columns
    cols_to_use = [x for x in a if 'datetime' in x.lower()] + [x for x in a if 'locationid' in x.lower()]
    data = pd.read_csv(file, usecols=cols_to_use, error_bad_lines=False, )
    data.columns = [x.replace(' ', '_').lower().replace('lpep_', '').replace("tpep_", '') for x in data.columns]
    return initial_data_clean(data)
def create_parquet_by_colour(colour='green'):
    global timee
    csv_path = path + f'/{colour}/'
    files = os.listdir(csv_path)
    files = [csv_path + x for x in files]
    file_sizes = 0
    for each in files:
        file_sizes += os.stat(each).st_size / 1024**3
    logging.info(f"{colour.capitalize()} total file size as CSV: {file_sizes:.1f} GB")
    # set up your pool
    # with Pool(processes=4) as pool:
    #     # have your pool map the file names to dataframes
    #     df_list = pool.map_async(readcsv, files,)
    #     df_list.wait()
    #     df = pd.concat(df_list.get(), ignore_index=True)
    df = pd.concat((readcsv(each) for each in files[::-1]), ignore_index=True)
    logging.info(f'initial clean finished for all processes: {datetime.datetime.now() - timee}')
    df = initial_data_clean(df)
    df.to_parquet(path + f'{colour}_data_oct2020.parquet')

@dask.delayed
def inner_trans(df):
    df['dolocationid'] = df['dolocationid'].astype(np.int16)
    df['pulocationid'] = df['pulocationid'].astype(np.int16)
    df.reset_index(inplace=True, drop=True)
    # logging.info(df.sample(5).to_string())
    # df.info()
    # logging.info(datetime.datetime.now() - timee)
    try:
        df['dropoff_date'] = pd.to_datetime(df['dropoff_datetime'], errors='coerce')
    except:
        df['dropoff_date'] = df['dropoff_datetime']
    try:
        df['pickup_date'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
    except:
        df['pickup_date'] = df['pickup_datetime']
    if df['dropoff_date'].equals(df['dropoff_datetime']):
        pass
    else:
        df['dropoff_date'] = df['pickup_date']
    df = df.dropna(how='any')
    df = df.drop(['dropoff_datetime', 'pickup_datetime'], 1, )
    tmp = {'weekend': [],
           "day_of_week": [],
           'holiday': []}
    df['month'] = df['pickup_date'].dt.month
    df['p_Hour'] = df['pickup_date'].dt.hour
    df['day'] = df['pickup_date'].dt.day
    df['year'] = df['pickup_date'].dt.year
    df['d_Hour'] = df['dropoff_date'].dt.hour
    for x in df['pickup_date']:
        p = x.isoweekday()
        tmp["day_of_week"].append(p)
        if p in [6, 7]:
            tmp['weekend'].append(1)
        else:
            tmp['weekend'].append(0)
        if x.date() in ny_holidays:
            tmp["holiday"].append(1)
        else:
            tmp["holiday"].append(0)
    for k, v in tmp.items():
        df[k] = pd.Series(v).astype(np.int16)
    df['season'] = pd.Series(make_season(df['pickup_date'])).astype('category')
    return df
@dask.delayed
def inner_trans2(df):
    df['dolocationid'] = df['dolocationid'].astype(np.int16)
    df['pulocationid'] = df['pulocationid'].astype(np.int16)
    logging.info(datetime.datetime.now() - timee)
    df.reset_index(inplace=True, drop=True)
    try:
        df['dropoff_date'] = pd.to_datetime(df['dropoff_datetime'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    except Exception as e:
        df['dropoff_date'] = df['dropoff_datetime']
    logging.info(datetime.datetime.now() - timee)
    try:
        df['pickup_date'] = pd.to_datetime(df['pickup_datetime'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    except:
        df['pickup_date'] = df['pickup_datetime']
    # years = pick_up_date.astype('datetime64[Y]').astype(int) + 1970
    # months = pick_up_date.astype('datetime64[M]').astype(int) % 12 + 1
    # days = (pick_up_date - pick_up_date.astype('datetime64[M]')).astype(int) + 1
    # hours = pick_up_date.astype('datetime64[H]').astype(int)
    # for i, each in enumerate(pick_up_date):
    #     print(each, years[i], months[i], days[i], hours[i])
    logging.info(datetime.datetime.now() - timee)
    df = df.drop(['dropoff_datetime', 'pickup_datetime'], 1, )
    df = df.replace([np.inf, -np.inf,'NaN', 'NaT'], np.nan)
    try:
        df = df.dropna(how='any')
    except ValueError as ve:
        print(df.sample(15).to_string())
        print('you suck')
        # print(df[df.isna().any(axis=1)].to_string())
    df['month'] = df['pickup_date'].dt.month
    df['p_Hour'] = df['pickup_date'].dt.hour
    df['day'] = df['pickup_date'].dt.day
    df['year'] = df['pickup_date'].dt.year
    df['d_Hour'] = df['dropoff_date'].dt.hour
    df['day_of_week'] = df['pickup_date'].dt.weekday + 1
    df['weekend'] = (df['day_of_week'] < 6).astype(int)
    df['holiday'] = df['pickup_date'].isin(ny_holidays)
    seasons = ['winter', 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall',]
    df['season'] = df['pickup_date'].dt.month.map(dict(zip(range(1, 13), seasons))).astype('category')
    logging.info(f"vectorize done: {datetime.datetime.now() - timee}")
    return df

def data_transforms_dask_delayed(colour='green', size=2_200_000):
    # dfs = []
    # counter = 0
    # for yr in range(2016, 2020):
    #     for chunk in pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, chunksize=size):
    #         counter += len(chunk)
    #         print(f"# of rows: {counter}")
    #         dfs.append(inner_trans(chunk))

    df = pd.read_parquet(path + f'{colour}_data.parquet')
    logging.info(datetime.datetime.now() - timee)
    df = pd.concat(dask.compute(*dfs))
    df['colour'] = colour
    df['colour'] = df['colour'].astype('category')
    df.columns = [x.lower() for x in df.columns]
    # df.info(buf=buffer)
    # with open(path + "log.txt", "a",
    #           encoding="utf-8") as f:
    #     f.write(buffer.getvalue())
    df.info()
    logging.info(datetime.datetime.now() - timee)
    pickle_out = open(path + f"data_{colour}_all.pickle", "wb")
    pickle.dump(df, pickle_out, protocol=4)
    pickle_out.close()
    gc.collect()
    logging.info(datetime.datetime.now() - timee)
def data_transforms_orig_vector(colour='green', ):
    # dfs = (pd.read_sql(f"""# select * from "{yr}_{colour.upper()}" """, conn, ) for yr in range(2016, 2020))
    # df = pd.concat(dfs)
    df = pd.read_parquet(path + f'{colour}_data.parquet')
    df = inner_trans2(df)
    df['colour'] = colour
    df['colour'] = df['colour'].astype('category')
    df.columns = [x.lower() for x in df.columns]
    df.to_parquet(path + f'df_done_{colour}.parquet')
def data_transforms_dask_vector(colour='green', size=5_000_000, ):
    dfs=[]
    df = pd.read_parquet(path + f'{colour}_data.parquet')
    logging.info(datetime.datetime.now() - timee)
    for x in np.split(df, np.arange(size, len(df), size)):
        dfs.append(inner_trans2(x))
    df = pd.concat(dask.compute(*dfs))
    df['colour'] = colour
    df['colour'] = df['colour'].astype('category')
    df.columns = [x.lower() for x in df.columns]
    # logging.info(df.sample(5).to_string())
    # df.info(buf=buffer)
    # with open(path + "log.txt", "a",
    #           encoding="utf-8") as f:
    #     f.write(buffer.getvalue())
    # logging.info(datetime.datetime.now() - timee)
    # pickle_out = open(path + f"data_{colour}_all_orig2.pickle", "wb")
    # pickle.dump(df, pickle_out, protocol=4)
    # pickle_out.close()
    gc.collect()
    df.to_parquet(path + 'df.parquet')

def data_transforms(colour='green', size=2_200_000):
    dfs = pd.concat(pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, ) for yr in [2016, 2017, 2018, 2019])
    df = pd.concat([inner_trans(x) for x in np.split(dfs, np.arange(size, len(dfs), size))])
    df['colour'] = colour
    df.columns = [x.lower() for x in df.columns]
    logging.info(df.sample(5).to_string())
    df.info(buf=buffer)
    with open(path + "log.txt", "a",
              encoding="utf-8") as f:
        f.write(buffer.getvalue())
    logging.info(datetime.datetime.now() - timee)
    pickle_out = open(path + f"data_{colour}_all.pickle", "wb")
    pickle.dump(df, pickle_out, protocol=4)
    pickle_out.close()
    gc.collect()
    logging.info(datetime.datetime.now() - timee)
def data_transforms_orig(colour='green', ):
    dfs = (pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, ) for yr in [2016, 2017, 2018, 2019])
    df = pd.concat(dfs)
    df = inner_trans(df)
    df['colour'] = pd.Series([colour for x in range(len(df.index))]).astype('category')
    df.columns = [x.lower() for x in df.columns]
    logging.info(df.sample(5).to_string())
    df.info(buf=buffer)
    with open(path + "log.txt", "a",
              encoding="utf-8") as f:
        f.write(buffer.getvalue())
    logging.info(datetime.datetime.now() - timee)
    pickle_out = open(path + f"data_{colour}_all_orig.pickle", "wb")
    pickle.dump(df, pickle_out, protocol=4)
    pickle_out.close()
    gc.collect()
    logging.info(datetime.datetime.now() - timee)

def thing(weekend, season, day_of_week, hr, m, yr, h, each, data, right):

    # data = data[(data['year'] == yr) & (data['holiday'] == h) &(data['p_hour'] == hr) & (data['month'] == m)]

    for d in day_of_week:
        data = data[data['day_of_week'] == d]
        for s in season:
            data = data[data['season'] == s]
            for w in weekend:
                data = data[data['weekend'] == w]
                value_counts = pd.DataFrame(data[each].value_counts())
                value_counts.columns = ['value']
                new_vals_df = pd.concat([pd.DataFrame(data={'value': 1}, index=[i]) for i in all_points if i not in list(value_counts.index)])
                tmp = pd.concat([new_vals_df, value_counts], )
                right['Pick-Up'][str('green')][yr][m][hr][h][d][s][w] = tmp
    return right

def inner_post_transform(w, s, d, h, hr, m, yr, each, data):
    c = datetime.datetime.now()
    data = data[(data['weekend'] == w) & (data['season'] == s) & (data['year'] == yr) & (data['holiday'] == h) & (data['day_of_week'] == d) & (data['p_hour'] == hr) & (data['month'] == m)]
    value_counts = pd.DataFrame(data[each].value_counts())
    value_counts.columns = ['value']
    new_vals_df = pd.concat([pd.DataFrame(data={'value': 1}, index=[i]) for i in all_points if i not in list(value_counts.index)])
    wow = pd.concat([new_vals_df, value_counts], )
    done = datetime.datetime.now()
    print(done-c)
    return wow
def post_transform():
    df_one = {}
    colours = ['green']
    years = [2016, 2017, 2018, 2019, ]
    weekend = [0, 1]
    season = ["fall", "winter", "summer", "spring"]
    holiday = [False, True ]
    day_of_week = list(range(1,8))
    hour = list(range(0,24))
    months = list(range(1,13))
    inner_dict = {i:
                    {y:
                       {m:
                           {hr:
                                {h:
                                     {d:
                                          {s: {w: {} for w in list(weekend)} for s in list(season)}
                                      for d in list(day_of_week)}
                                 for h in list(holiday)}
                            for hr in list(hour)}
                        for m in list(months)}
                    for y in list(years)}
                for i in list(colours)}
    pu_do_data = {"Pick-Up": inner_dict,
                  "Drop-Off": inner_dict}
    num = 0
    for colour in colours:
        df_one[colour] = pd.read_parquet(path + f"df_done_{colour}.parquet")
        df_one[colour].info()
    data = df_one['green'].drop(columns=['day', 'dropoff_date','pickup_date'])
    data.info()
    print(data.sample(100).to_string())
    # df_one['all'] = pd.concat([df_one[x] for x in colours], sort=False)
    for each in ['pulocationid', "dolocationid"]:
        for car_type in colours:
            for yr in years:
                for m in tqdm(months):
                    for hr in hour:
                        for h in holiday:
                            for d in day_of_week:
                                for s in season:
                                    for w in weekend:
                                        tmp = inner_post_transform(w,s,d,h,hr,m,yr, each, df_one['green'].copy())
                                        if each == "pulocationid":
                                            pu_do_data['Pick-Up'][str(car_type)][yr][m][hr][h][d][s][w] = tmp
                                        else:
                                            pu_do_data['Drop-Off'][str(car_type)][yr][m][hr][h][d][s][w] = tmp
    pickle_out = open("green_output1.pickle", "wb")
    pickle.dump(pu_do_data, pickle_out)
    pickle_out.close()

create_parquet_by_colour('green')

# if __name__ == '__main__':
#     # client = Client(n_workers=1, threads_per_worker=4, memory_limit='5GB')
#     # client = Client()
#     # print(client)
#     # for col in ['yellow']:
#     #     # create_parquet_by_colour(col)
#     #     # logging.info(datetime.datetime.now() - timee)
#     #     data_transforms_dask_vector(col)
#     #     # func = data_transforms_orig_vector
#     #     # logging.info(func.__name__)
#     #     # func()
#     #     gc.collect()
#     #     logging.info(datetime.datetime.now() - timee)
#     timee = datetime.datetime.now()
#     post_transform()

