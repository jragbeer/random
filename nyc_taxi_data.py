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
from dask.distributed import Client, progress
import dask.dataframe as dd

if __name__ == '__main__':

    client = Client(n_workers=7, threads_per_worker=1, memory_limit='8.5GB')
    # client = Client()
    print(client)
    switch = {"Green": "Green_Taxi_Trip_Data",
              "Yellow": "Yellow_Taxi_Trip_Data",
              "FHV": "For_Hire_Vehicles_Trip_Data",
              "HVFHV": "HV_FHV", }
    buffer = io.StringIO()


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
                               chunksize=15_000_000, names=dfcolumns.columns, error_bad_lines=False, engine='python')
            n = 1
            for chunk in data:
                print(n)
                df_list.append(etl_csv_to_db(chunk))
                n += 1

            large_df = pd.concat(df_list)
            if 'fhv' in colour.lower():
                large_df.to_sql(f'{year}_FHV', conn, if_exists='append', index=False)
            else:
                large_df.to_sql(f'{year}_{colour.upper()}', conn, if_exists='replace', index=False)
            print('done', datetime.datetime.now() - timee)

        except Exception as e:
            print(error_handling())


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


    # @dask.delayed
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
            print('nada')
            df['pickup_date'] = df['pickup_datetime']
        if df['dropoff_date'].equals(df['pickup_date']):
            pass
        else:
            df['pickup_date'] = df['dropoff_date']
        # print(type(drop_off_date))
        # print(pick_up_date)
        # years = pick_up_date.astype('datetime64[Y]').astype(int) + 1970
        # months = pick_up_date.astype('datetime64[M]').astype(int) % 12 + 1
        # days = (pick_up_date - pick_up_date.astype('datetime64[M]')).astype(int) + 1
        # hours = pick_up_date.astype('datetime64[H]').astype(int)
        # for i, each in enumerate(pick_up_date):
        #     print(each, years[i], months[i], days[i], hours[i])
        logging.info(datetime.datetime.now() - timee)
        df = df.drop(['dropoff_datetime', 'pickup_datetime'], 1, )
        df = df.replace([np.inf, -np.inf], np.nan)
        try:
            df = df.dropna()
        except:

            df = df.dropna()
        tmp = {'weekend': [],
               "day_of_week": [],
               'holiday': []}
        df['month'] = df['pickup_date'].dt.month
        df['p_Hour'] = df['pickup_date'].dt.hour
        df['day'] = df['pickup_date'].dt.day
        df['year'] = df['pickup_date'].dt.year
        df['d_Hour'] = df['dropoff_date'].dt.hour
        df['day_of_week'] = df['pickup_date'].dt.weekday + 1
        df['weekend'] = (df['day_of_week'] < 6).astype(int)
        df['holiday'] = df['pickup_date'].isin(ny_holidays)
        logging.info("vectorize done: ")
        logging.info(datetime.datetime.now() - timee)

        # for x in df['pickup_date']:
        #     if x.date() in ny_holidays:
        #         tmp["holiday"].append(1)
        #     else:
        #         tmp["holiday"].append(0)

        # for k, v in tmp.items():
        #     df[k] = pd.Series(v).astype(np.int16)
        df['season'] = pd.Series(make_season(df['pickup_date'])).astype('category')
        return df


    def data_transforms_dask_delayed(colour='green', size=2_200_000):
        dfs = []
        counter = 0
        for yr in range(2016, 2020):
            for chunk in pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, chunksize=size):
                counter += len(chunk)
                print(f"# of rows: {counter}")
                dfs.append(inner_trans(chunk))
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
        df = pd.read_parquet(path + 'data.parquet')
        logging.info(datetime.datetime.now() - timee)
        df.info()
        df = inner_trans2(df)
        df['colour'] = pd.Series([colour for x in range(len(df.index))]).astype('category')
        df.columns = [x.lower() for x in df.columns]
        df.to_parquet(path + 'df_done_green.parquet')
        gc.collect()
        logging.info(datetime.datetime.now() - timee)


    def data_transforms_dask_vector(colour='green', size=5_000_000, ):
        dfs = []
        counter = 0
        for yr in range(2016, 2020):
            for chunk in pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, chunksize=size):
                counter += len(chunk)
                print(f"# of rows: {counter}")
                dfs.append(inner_trans2(chunk))
        logging.info(datetime.datetime.now() - timee)
        df = pd.concat(dask.compute(*dfs))
        df['colour'] = colour
        df['colour'] = df['colour'].astype('category')
        df.columns = [x.lower() for x in df.columns]
        logging.info(df.sample(5).to_string())
        df.info(buf=buffer)
        with open(path + "log.txt", "a",
                  encoding="utf-8") as f:
            f.write(buffer.getvalue())
        logging.info(datetime.datetime.now() - timee)
        # pickle_out = open(path + f"data_{colour}_all_orig2.pickle", "wb")
        # pickle.dump(df, pickle_out, protocol=4)
        # pickle_out.close()
        gc.collect()
        df.to_parquet(path + 'df.parquet')
        logging.info(datetime.datetime.now() - timee)


    def data_transforms(colour='green', size=2_200_000):
        dfs = pd.concat(pd.read_sql(f"""select * from "{yr}_{colour.upper()}" """, conn, ) for yr in [2016, 2017, 2018, 2019])
        df = pd.concat([inner_trans(x) for x in np.split(dfs, np.arange(size, len(dfs), size))])
        df['colour'] = pd.Series([colour for x in range(len(df.index))]).astype('category')
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
            pickle_in = open(f"data_{colour}.pickle", "rb")
            df_one[colour] = pickle.load(pickle_in)
            print(datetime.datetime.now() - timee)

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

    ny_holidays = holidays.CountryHoliday("US", state='NY')
    timee = datetime.datetime.now()
    path = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
    db = 'NYC_Taxi_Data.db'
    conn = sqlite3.connect(path + db)
    conn.text_factory = lambda b: b.decode(errors='ignore')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(message)s',
                        handlers=[logging.FileHandler(path + "log.txt"), logging.StreamHandler()])
    logging.info(timee)
    func = data_transforms_orig_vector
    logging.info(func.__name__)
    func()
    gc.collect()
    logging.info(datetime.datetime.now() - timee)

