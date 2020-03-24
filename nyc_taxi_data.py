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
# timee = datetime.datetime.now()
#
# pickle_in = open("final.pickle","rb")
# so_far = pickle.load(pickle_in)
# print(datetime.datetime.now()-timee)
#
# pickle_in = open("final0.pickle","rb")
# so_far2 = pickle.load(pickle_in)
# print(datetime.datetime.now()-timee)
#
# boo = {"Drop-Off": so_far["dolocationid"],"Pick-Up": so_far2["pulocationid"] }
# pickle_out = open("answers.pickle","wb")
# pickle.dump(boo, pickle_out)
# pickle_out.close()
# print(datetime.datetime.now()-timee)
# # import sys
# wow = []
# # for each in ['pulocationid', "dolocationid"]:
# for each in ['pulocationid',]:
#     for tipo in ['yellow', 'green', 'fhv', 'all']:
#         for yr in [2016, 2017, 2018, 'all']:
#             for hr in [18, 19, 20, "all"]:
#                 for mth in list(range(1, 13)) + ['all']:
#                     for day in list(range(1, 8)) + ['all']:
#                         for hlday in [0, 1, 'all']:
#                             zz = [each, tipo, yr, hr, mth, day, hlday, 'over']
#                             wow.append(zz)
#                             print(zz)
#                             if zz == so_far:
#                                 pickle_out = open("wow1.pickle", "wb")
#                                 pickle.dump(wow, pickle_out)
#                                 pickle_out.close()
#                                 sys.exit()
#                                 # break
#                             # else:
#                             #     print('no')


path = "C:/Users/Julien/PycharmProjects/nyctaxi/data/"
db = 'NYC_Taxi_Data.db'
timee = datetime.datetime.now()
conn = sqlite3.connect(path+db)

switch = {"Green": "Green_Taxi_Trip_Data",
          "Yellow": "Yellow_Taxi_Trip_Data",
          "FHV": "For_Hire_Vehicles_Trip_Data",
          "HVFHV": "HV_FHV",}

def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()

def etl_csv_to_db(df):
    df.columns = [x.replace(' ', '_').lower().replace('lpep_', '').replace("tpep_", '') for x in df.columns]
    print(df.columns)
    df = df[['pickup_datetime', "dropoff_datetime", "pulocationid", "dolocationid"]]
    df['dolocationid'] = pd.to_numeric(df['dolocationid'], errors='coerce', downcast='integer')
    df['pulocationid'] = pd.to_numeric(df['pulocationid'], errors='coerce', downcast='integer')
    df.dropna(how='any', inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df

def create_initial_database_from_csv(year, colour):
    # create database and add data to it
    try:
        print(year, colour)
        fp = path + f"{year}_{switch[colour]}.csv"
        dfcolumns = pd.read_csv(fp, nrows=1)
        df_list = []
        data = pd.read_csv(fp, header=None, skiprows=1, usecols=list(range(1, len(dfcolumns.columns))),
                           chunksize=15_000_000, names=dfcolumns.columns, error_bad_lines=False, engine = 'python')
        n = 1
        for chunk in data:
            print(n)
            df_list.append(etl_csv_to_db(chunk))
            n+=1

        large_df = pd.concat(df_list)
        if 'fhv' in colour.lower():
            large_df.to_sql(f'{year}_FHV', conn, if_exists='append', index=False)
        else:
            large_df.to_sql(f'{year}_{colour.upper()}', conn, if_exists='replace', index=False)
        print('done', datetime.datetime.now() - timee)

    except Exception as e:
        print(error_handling())

def data_transforms(colour='green'):
    dfs = (pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn,) for yr in [2018, 2019,])
    df = pd.concat(dfs)
    df['dolocationid'] = df['dolocationid'].astype(np.int16)
    df['pulocationid'] = df['pulocationid'].astype(np.int16)
    df.reset_index(inplace=True)
    logging.info(df.sample(5).to_string())
    logging.info(df.info())
    logging.info(datetime.datetime.now() - timee)
    try:
        df['dropoff_date'] = pd.Series(
            [datetime.datetime(int(str(x)[6:10]), int(str(x)[0:2]), int(str(x)[3:5]), int(str(x)[11:13])) for x in
             df['dropoff_datetime']])
    except:
        df['dropoff_date'] = df['drop_off_datetime']
    try:
        df['pickup_date'] = pd.Series([datetime.datetime(int(str(x)[6:10]), int(str(x)[0:2]), int(str(x)[3:5]), int(str(x)[11:13])) for x in df['pickup_datetime']])
    except:
        df['pickup_date'] = df['pickup_datetime']
    if df['dropoff_date'].asarray() == df['drop_off_datetime'].asarray():
        df['dropoff_date'] = df['pickup_date']
    df['Month'] = pd.Series([x.month for x in df['pickup_date']]).astype(np.int16)
    df['Day'] = pd.Series([x.day for x in df['pickup_date']]).astype(np.int16)
    df['year'] = pd.Series([x.day for x in df['pickup_date']]).astype(np.int16)
    df['p_Hour'] = pd.Series([x.hour for x in df['pickup_date']]).astype(np.int16)
    df['d_Hour'] = pd.Series([x.hour for x in df['dropoff_date']]).astype(np.int16)
    df['season'] = make_season(df['pickup_date'])
    logging.info(df.sample(5).to_string())
    logging.info(df.info())
    logging.info(datetime.datetime.now() - timee)
    df['day_of_week'] = pd.Series([x.isoweekday() for x in df['dropoff_date']]).astype(np.int16)
    logging.info(datetime.datetime.now() - timee)
    df['weekend'] = pd.Series([1 if x in [6, 7] else 0 for x in df['day_of_week']]).astype(np.int16)
    df['holiday'] = pd.Series([1 if x.date() in ny_holidays else 0 for x in df['dropoff_date']]).astype(np.int16)
    logging.info(datetime.datetime.now() - timee)
    df['colour'] = [colour for x in range(len(df.index))]
    df.columns = [x.lower() for x in df.columns]
    logging.info(df.sample(5).to_string())
    logging.info(df.info())
    logging.info(datetime.datetime.now() - timee)
    pickle_out = open(path + f"data_{colour}1.pickle","wb")
    pickle.dump(df, pickle_out)
    pickle_out.close()
    gc.collect()
    logging.info(datetime.datetime.now() - timee)
def make_season(series):
    array = []
    for x in series:
        new_date = datetime.datetime(2000, x.month, x.day)
        if datetime.datetime(2000, 3, 1) <= new_date < datetime.datetime(2000,6,1):
            array.append('spring')
        elif datetime.datetime(2000, 6, 1) <= new_date < datetime.datetime(2000,9,1):
            array.append('summer')
        elif datetime.datetime(2000, 9, 1) <= new_date < datetime.datetime(2000, 12,1):
            array.append('fall')
        else:
            array.append('winter')
    return array
def post_transform():

    for colour in ['yellow', 'green', 'fhv']:
        #
        # pickle_in = open("data_{}_cut.pickle".format(colour),"rb")
        # df = pickle.load(pickle_in)
        # print(df.columns)
        # df.rename({"tpep_dropoff_datetime": "dropoff_datetime", "tpep_pickup_datetime": "pickup_datetime", }, axis = 'columns', inplace = True)
        # df.rename({"lpep_dropoff_datetime": "dropoff_datetime", "lpep_pickup_datetime": "pickup_datetime", }, axis = 'columns',
        #               inplace=True)
        # print(df.columns)
        # df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
        # df['day'] = [x.day for x in df['pickup_datetime']]
        # df.drop([x.lower() for x in df.columns if x not in ['pickup_datetime', 'dropoff_datetime', 'pulocationid',
        #    'dolocationid', 'pickup_hour', 'dropoff_hour', 'year', 'month', 'day',
        #    'day_of_week', 'weekend', 'holiday', 'colour']], 1, inplace=True)
        pickle_in = open(f"data_{colour}.pickle","rb")
        df_one[colour] = pickle.load(pickle_in)
        print(datetime.datetime.now()-timee)

    df_one['all'] = pd.concat([df_one[x] for x in ['yellow', 'green', 'fhv']], sort=False)
    for each in ['pulocationid', "dolocationid"]:
        for z in ['yellow', 'green', 'fhv', 'all']:
            for t in [2016, 2017, 2018, 2019, 'all']:
                rrtt = copy.deepcopy(df_one[z])
                if t != 'all':
                    rrtt = rrtt[rrtt['year'] == t]
                rr = pd.DataFrame(rrtt[each].value_counts())
                rr.columns = ['value']
                for i in all_points:
                    if i not in list(rr.index):
                        print(i, ' not in')
                        rr.append(pd.DataFrame(data={'value': 0}, index=[i]))
                pickle_out = open("{}_{}_{}_full_test.pickle".format(each, z, t), "wb")
                pickle.dump(rr, pickle_out)
                pickle_out.close()
                print(datetime.datetime.now() - timee)
                print('over')

def read_db(tablename, conn_):
    query = "select * from {}".format(tablename)
    df = pd.read_sql(query, conn_, parse_dates=['pickup_datetime', 'dropoff_datetime'])
    return df

ny_holidays = holidays.CountryHoliday("US",state='NY')
timee = datetime.datetime.now()
path = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
db = 'NYC_Taxi_Data.db'

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(message)s',
                    handlers=[logging.FileHandler(path+"log.txt"),
                              logging.StreamHandler()])
conn = sqlite3.connect(path + db)
conn.text_factory = lambda b: b.decode(errors = 'ignore')
logging.info(timee)

# db = 'NYC_Taxi_Data.db'
# path2 = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
# conn = sqlite3.connect(path2 + db)

# df = pd.read_sql('select PULocationID, DOLocationID, passenger_count, pickup_hour from Trip_Data where pickup_hour >= 18 and pickup_hour < 21', conn)
# print(df.sample(26).to_string())
# print(datetime.datetime.now()-timee)
# print('over')
# df_one = {}
# pu_do_data = {"Pick-Up": {}, "Drop-Off": {}}
#
# for colr in ['yellow', 'green', "fhv", "all", ]:
#     pickle_in = open("pulocationid_{}_full.pickle".format(colr),"rb")
#     pu_data = pickle.load(pickle_in)
#     pickle_in = open("dolocationid_{}_full.pickle".format(colr),"rb")
#     do_data = pickle.load(pickle_in)
#     pu_data.columns = ['value']
#     do_data.columns = ['value']
#     pu_do_data['Pick-Up'][str(colr)] = pu_data
#     pu_do_data['Drop-Off'][str(colr)] = do_data
#
# all_points = pu_do_data['Pick-Up']['fhv'].index
data_transforms('yellow')
logging.info(datetime.datetime.now()-timee)


# for i in ['FHV']:
#     for yr in [2018]:
#         create_initial_database_from_csv(yr, i)
#         gc.collect()