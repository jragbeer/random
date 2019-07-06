import numpy as np
import pandas as pd
import urllib
import sqlite3
import datetime
import sys
import pickle
import holidays
import copy

def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return '{}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno)
def download_data_from_AWS():
    # Download data from AWS S3
    for yr in range(6, 9):
        if yr != 6:
            for month in range(1, 13):
                urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/trip+data/"
                                           "fhv_tripdata_201{0}-{1:0=2d}.csv".format(yr, month),
                                           path2 + "nyc_fhv.201{}-{}.csv".format(yr, month))
                print(yr, month, datetime.datetime.now() - timee)
        else:
            for month in range(7, 13):
                urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/trip+data/"
                                           "fhv_tripdata_201{0}-{1:0=2d}.csv".format(yr, month),
                                           path2 + "nyc_fhv.201{}-{}.csv".format(yr, month))
                print(yr, month, datetime.datetime.now() - timee)
def create_initial_database_from_csv():
    # create database and add data to it
    for yr in range(7, 9):
        for month in range(1, 13):
            if yr == 7 and month < 7:
                continue
            try:
                print(yr, month)
                fp = path2 + "nyc_fhv.201{}-{}.csv".format(yr, month)
                dfcolumns = pd.read_csv(fp, nrows=1)
                df = pd.read_csv(fp, header=None, skiprows=1, usecols=list(range(len(dfcolumns.columns))),
                                 names=dfcolumns.columns)
                df.rename(columns={c: c.replace(' ', '_').lower() for c in df.columns}, inplace=True)
                try:
                    df.rename(
                        {"tpep_dropoff_datetime": "dropoff_datetime", "tpep_pickup_datetime": "pickup_datetime", },
                        inplace=True)
                except:
                    df.rename(
                        {"lpep_dropoff_datetime": "dropoff_datetime", "lpep_pickup_datetime": "pickup_datetime", },
                        inplace=True)

                df.drop([x for x in df.columns if
                         x not in ['pickup_datetime', "dropoff_datetime", "pulocationid", "dolocationid"]], 1,
                        inplace=True)
                df.dropna(how='any', inplace=True)
                df['pulocationid'] = df['pulocationid'].astype(int)
                df['dolocationid'] = df['dolocationid'].astype(int)
                df.reset_index(inplace=True, drop=True)
                print(f'dataframe is {len(df)} long')
                df['pickup_hour'] = pd.Series([int(str(x)[11:13]) for x in df['pickup_datetime']], index=df.index)
                df['dropoff_hour'] = pd.Series([int(str(x)[11:13]) for x in df['dropoff_datetime']], index=df.index)
                df.to_sql('Trip_Data', conn, if_exists='append', index=False)
                print('done')
                print('month', datetime.datetime.now() - timee)
            except Exception as e:
                print(str(e))
                print(error_handling())
                pass
        print('year', datetime.datetime.now() - timee)
def data_transforms():
    for colour in ['green', 'yellow', 'FHV']:
        path2 = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
        db = 'NYC_Taxi_Data_{}.db'.format(colour)
        conn = sqlite3.connect(path2 + db)
        query = "select pickup_datetime as tpep_pickup_datetime, dropoff_datetime as tpep_dropoff_datetime, pulocationid, dolocationid, pickup_hour, dropoff_hour from Trip_Data where pickup_hour >= 18 and pickup_hour < 21"
        df = pd.read_sql(query, conn)
        print(df.sample(10).to_string())
        print(datetime.datetime.now()-timee)
        try:
            df['Year'] = pd.Series([int(str(x)[0:4]) for x in df.tpep_pickup_datetime], index = df.index)
            df['Month'] = pd.Series([int(str(x)[5:7]) for x in df.tpep_pickup_datetime], index = df.index)
            df['Day'] = pd.Series([int(str(x)[8:10]) for x in df.tpep_pickup_datetime], index=df.index)
        except:
            df['Year'] = pd.Series([int(str(x)[0:4]) for x in df.lpep_pickup_datetime], index = df.index)
            df['Month'] = pd.Series([int(str(x)[5:7]) for x in df.lpep_pickup_datetime], index = df.index)
            df['Day'] = pd.Series([int(str(x)[8:10]) for x in df.lpep_pickup_datetime], index=df.index)
        print(df.sample(10).to_string())
        weekday = []
        datestrings = []
        for x in df.itertuples():
            try:
                weekdaynumber = datetime.datetime(int(x.Year), int(x.Month), int(x.Day), x.pickup_hour)
                weekday.append(weekdaynumber.isoweekday()) # 1 is monday, 7 is sunday
                try:
                    try:
                        datestring = datetime.datetime(int(x.Year), int(x.Month), int(x.Day), x.pickup_hour,
                                                   int(str(x.lpep_pickup_datetime)[14:16]))
                    except:
                        datestring = datetime.datetime(int(x.Year), int(x.Month), int(x.Day), x.pickup_hour,
                                                   int(str(x.tpep_pickup_datetime)[14:16]))
                    datestrings.append(datestring)
                except:
                    datestrings.append(np.nan)
            except:
                weekday.append(8)
        print(datetime.datetime.now()-timee)
        df['day_of_week'] = pd.Series(weekday, index=df.index)
        df['datestring'] = pd.Series(datestrings, index=df.index)
        df['weekend'] = [1 if x.day_of_week in [6, 7] else 0 for x in df.itertuples()]
        try:
            df['holiday'] = [1 if datetime.datetime(int(x.tpep_pickup_datetime[:4]), int(x.tpep_pickup_datetime[5:7]), int(x.tpep_pickup_datetime[8:10])).date() in ny_holidays else 0 for x in df.itertuples()]
        except:
            df['holiday'] = [1 if datetime.datetime(int(x.lpep_pickup_datetime[:4]), int(x.lpep_pickup_datetime[5:7]),
                                                    int(x.lpep_pickup_datetime[8:10])).date() in ny_holidays else 0 for x in
                             df.itertuples()]
        df['colour'] = ['{}'.format(colour) for x in range(len(df.index))]
        df.columns = [x.lower() for x in df.columns]
        pickle_out = open("data_{}_cut.pickle".format(colour),"wb")
        pickle.dump(df, pickle_out)
        pickle_out.close()
def read_db(tablename, conn_):
    query = "select * from {}".format(tablename)
    df = pd.read_sql(query, conn_, parse_dates=['pickup_datetime', 'dropoff_datetime'])
    return df

ny_holidays = holidays.CountryHoliday("US",state='NY')

timee = datetime.datetime.now()
print(timee)

path = "C:/Users/J_Ragbeer/Desktop/"
path2 = "C:/Users/Julien/PycharmProjects/NYCTaxi/data/"
db = 'Taxi_Data.db'
conn = sqlite3.connect(path2 + db)

print(datetime.datetime.now()-timee)
df_one = {}
pu_do_data = {"Pick-Up": {}, "Drop-Off": {}}

for colr in ['yellow', 'green', "fhv", "all", ]:
    pickle_in = open("pulocationid_{}_full.pickle".format(colr),"rb")
    pu_data = pickle.load(pickle_in)
    pickle_in = open("dolocationid_{}_full.pickle".format(colr),"rb")
    do_data = pickle.load(pickle_in)
    pu_data.columns = ['value']
    do_data.columns = ['value']
    pu_do_data['Pick-Up'][str(colr)] = pu_data
    pu_do_data['Drop-Off'][str(colr)] = do_data

all_points = pu_do_data['Pick-Up']['fhv'].index

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
    pickle_in = open("data_{}1.pickle".format(colour),"rb")
    df_one[colour] = pickle.load(pickle_in)
    print(datetime.datetime.now()-timee)

df_one['all'] = pd.concat([df_one[x] for x in ['yellow', 'green', 'fhv']], sort=False)
for each in ['pulocationid', "dolocationid"]:
    for z in ['yellow', 'green', 'fhv', 'all']:
        for t in [2016, 2017, 2018, 'all']:
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

print(datetime.datetime.now()-timee)
