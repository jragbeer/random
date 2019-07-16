import pandas as pd
import numpy as np
import glob
import os
import datetime
import sqlite3
import smtplib
import calendar
import socket
import urllib
from urllib.request import HTTPError, URLError, Request, urlopen
import datetime
import pickle
from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import bs4 as bs
import time
import logging
import pytz
from shutil import copyfile, copy2
from sqlalchemy import create_engine

# credentials for Azure SQL
def get_credentials():
    path_to_file = "C:/Users/J_Ragbeer/PycharmProjects/weatherdata/"
    with open(path_to_file + "server_credentials.txt", 'r') as file:
        temp = file.read().splitlines()
        return list(temp)

# augment a dataframe of weather data
def hmdxx(temp, dew_temp):
    """

    returns the humidex reading given the air temp and dew temp

    :param x: air temp in Celsius
    :param y: dewpoint in Celsius
    :return: humidex reading as a float
    """
    return temp + (0.5555 * (6.11 * np.exp(5417.7530 * ((1 / 273.16) - (1 / (273.15 + dew_temp)))) - 10))
def clean_weather(weather):

    """
    cleans a raw weather dataframe....
    Adds cyclical variables such as weekday, hour, month and formats some, to remove degree symbol, drops columns

    :param weather: dataframe with weather data
    :return: the same dataframe as input, but with more useful columns
    """
    weather.index = pd.to_datetime(weather.index)
    weather.fillna(method='ffill', inplace=True)
    weather['Humidex'] = pd.Series([hmdxx(x[5], x[7]) for x in weather.itertuples()], index=weather.index)
    weather['Hour'] = pd.Series([int(x[0].hour) for x in weather.itertuples()], index=weather.index)
    weather['Weekday'] = pd.Series([int(x[0].weekday()) for x in weather.itertuples()], index=weather.index)
    weather['wd_sin'] = np.sin(weather['Weekday'] * (2. * np.pi / 7))
    weather['wd_cos'] = np.cos(weather['Weekday'] * (2. * np.pi / 7))
    weather['hr_sin'] = np.sin(weather['Hour'] * (2. * np.pi / 24))
    weather['hr_cos'] = np.cos(weather['Hour'] * (2. * np.pi / 24))
    weather['mnth_sin'] = np.sin((weather['Month'] - 1) * (2. * np.pi / 12))
    weather['mnth_cos'] = np.cos((weather['Month'] - 1) * (2. * np.pi / 12))
    try:
        weather['Temp'] = weather['Temp (°C)']
        weather['Dew Point Temp'] = weather['Dew Point Temp (°C)']
        weather.drop(['Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)',
                      'Wind Spd Flag', 'Visibility (km)', 'Visibility Flag', 'Temp Flag', 'Dew Point Temp Flag',
                      'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx Flag', 'Wind Chill', 'Rel Hum (%)', 'Hmdx',
                      'Dew Point Temp',
                      'Wind Chill Flag', 'Weather', 'Temp (°C)', 'Dew Point Temp (°C)'], 1, inplace=True)
    except Exception as e:
        pass
    return weather
def new_deg_days(df):
    """

    takes a temperature from a dataframe and returns two lists that correspond
    to its heat and cool degree days (from 6 degress C)

    :param df: input dataframe with a temperature column
    :return: two lists. 1st: heat degree day. 2nd: cool degree day
    """
    newdata = [i[4] for i in df.itertuples()]

    heatdays = [6-x for x in newdata]
    cooldays = [x-6 for x in newdata]
    newheatdays=[]
    newcooldays=[]
    for x in heatdays:
        if x < 0:
            newheatdays.append(0)
        else:
            newheatdays.append(x)
    for x in cooldays:
        if x < 0:
            newcooldays.append(0)
        else:
            newcooldays.append(x)
    return newheatdays,newcooldays
def fill_missing(idf, freq= 'D'):
    if freq == 'D':
        pass
    elif freq == 'H':
        pass
def pull_historical_data(city = 'Toronto', year = 2014, freq = None):
    weatherpath = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
    weatherdb = '{}WeatherHistorical.db'.format(city.replace(' ', ''))
    conn2 = sqlite3.connect(weatherpath + weatherdb)
    if freq == 'D':
        weather = pd.read_sql('Select * from {} where YEAR >= {}'.format(citydict[city]['tablename']+ '_Daily', year), conn2,
                              index_col='DATETIME')
    else:
        weather = pd.read_sql('Select * from {} where YEAR >= {}'.format(citydict[city]['tablename'], year), conn2,
                              index_col='DATETIME')
    weather.index = pd.to_datetime(weather.index)
    return weather

# download data from Weather Canada and put into databases
def load_2019_data_hourly(month=1):
    """

    appends to database hourly weather data from jan 1, 2019 onward
    :return: nothing


    """
    for z in list(citydict.keys()):
        today = datetime.datetime.now()
        bigdf = get_new_data_hourly(citydict[z]['stationid'], 2019, month)
        bigdf = bigdf[bigdf.index < datetime.datetime(today.year, today.month, today.day-1, 5)]
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        db = '{}WeatherHistorical.db'.format(z.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        bigdf.to_sql(citydict[z]['tablename'], conn, index=True, if_exists='append')
        print(z, 'done')
def load_old_data_into_db_hourly():
    """
    replaces database for weather with all data from 2011 - 2018 that is available. Hourly
    :return: nothing
    """
    for z in list(citydict.keys()):
        dfs = {}
        for x in range(2011, 2019):
            for y in range(1, 13):
                try:
                    dfs['{}_{}'.format(x, y)] = get_new_data_hourly(citydict[z]['stationid'], x, y)
                    print(z, x, y)
                    time.sleep(2)
                except Exception as e:
                    print(str(e))
                    pass
        bigdf = pd.concat([x for x in dfs.values()])
        bigdf.drop_duplicates(inplace=True)
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        db = '{}WeatherHistorical.db'.format(z.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        bigdf.to_sql(citydict[z]['tablename'], conn, index=True, if_exists='replace')
        print(z, 'done')
def load_old_data_into_db_daily():
    """
    replaces database for weather with all data from 2011 - 2018 that is available. Hourly
    :return: nothing
    """
    for z in list(citydict.keys()):
        dfs = {}
        for x in range(2011, 2020):
            try:
                dfs['{}'.format(x)] = get_new_data_daily(citydict[z]['stationid'], x)
                print(z, x)
            except Exception as e:
                print(str(e))
                pass
        bigdf = pd.concat([x for x in dfs.values()])
        bigdf.drop_duplicates(inplace=True)
        today = datetime.datetime.now()
        bigdf = bigdf[bigdf.index < datetime.datetime(today.year, today.month, today.day)]
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        db = '{}WeatherHistorical.db'.format(z.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        bigdf.to_sql(citydict[z]['tablename']+'_Daily', conn, index=True, if_exists='replace')
        print(z, 'done')
def get_new_data_daily(stationid, year=None):
    """
    grab most recent data (this year) from Weather Canada in csv form. The dataframe is sorted, column datatypes assigned
    and many columns are dropped.

    :param stationid: station ID to grab from
    :param year: year
    :return: returns a dataframe that's cleaned
    """

    date = datetime.datetime.now()
    if year:
        datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month=1&Day=14&timeframe=2&submit=Download+Data.csv".format(
        stationid, year)
    else:
        datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month=1&Day=14&timeframe=2&submit=Download+Data.csv".format(
        stationid, date.year)
    try:
        df = pd.read_csv(datastring, skiprows = 25)
        df['Month'] = df['Month'].astype(np.int64)
    except:
        df = pd.read_csv(datastring, skiprows=24)
    df.columns = df.columns.str.replace('\(°C\)', '')
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.upper()
    cols = ['Date/Time', 'Year', 'Month','Day','Max Temp','Min Temp','Mean Temp','Total Precip (mm)']
    Wdata = df[[x.upper() for x in cols]]
    Wdata.rename({'DATE/TIME': 'DATETIME', 'MAX TEMP':'MAX_TEMP','MIN TEMP':'MIN_TEMP','MEAN TEMP':'MEAN_TEMP', 'TOTAL PRECIP (MM)':'TOTAL_PRECIP_MM'},axis = 'columns', inplace = True)
    Wdata.dropna(thresh=4, inplace=True)
    Wdata.fillna(method='ffill', inplace=True)
    Wdata.fillna(method='bfill', inplace=True)
    Wdata.set_index('DATETIME', inplace=True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()

    return Wdata
def get_new_data_hourly(stationid, year=None, month = None):
    """
    grab most recent data (this month) from Weather Canada in csv form. The dataframe is sorted, column datatypes assigned
    and extra columns HOUR and HUMIDEX are added, while many are dropped

    :param stationid: station ID to grab from
    :param year: year
    :param month: month
    :return: returns a dataframe that's cleaned
    """
    date = datetime.datetime.now()
    if year and month:
        datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe=1&submit=Download+Data.csv".format(
        stationid, year, month)
    else:
        datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe=1&submit=Download+Data.csv".format(
        stationid, date.year, date.month)
    try:
        df = pd.read_csv(datastring, encoding='utf-8', skiprows=16, header=None,
                         names=['DATETIME', 'YEAR', 'MONTH', 'DAY', 'Time', 'TEMP', 'Temp Flag',
                                'DEW_TEMP', 'Dew Point Temp Flag', 'REL_HUM', 'Rel Hum Flag',
                                'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                                'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                                'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])
        Wdata = df[['DATETIME', 'YEAR', 'MONTH', 'DAY', 'TEMP', 'REL_HUM', 'DEW_TEMP']]
        Wdata.fillna(method='ffill', inplace=True)
        Wdata.fillna(method='bfill', inplace=True)
        Wdata.set_index('DATETIME', inplace=True)
        Wdata.index = pd.to_datetime(Wdata.index)
    except Exception as i:
        df = pd.read_csv(datastring, encoding='utf-8', skiprows=17, header=None,
                         names=['DATETIME', 'YEAR', 'MONTH', 'DAY', 'Time', 'TEMP', 'Temp Flag',
                                'DEW_TEMP', 'Dew Point Temp Flag', 'REL_HUM', 'Rel Hum Flag',
                                'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                                'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                                'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])
        Wdata = df[['DATETIME', 'YEAR', 'MONTH', 'DAY', 'TEMP', 'REL_HUM', 'DEW_TEMP']]
        Wdata.fillna(method='ffill', inplace=True)
        Wdata.fillna(method='bfill', inplace=True)
        Wdata.set_index('DATETIME', inplace=True)
        Wdata.index = pd.to_datetime(Wdata.index)

    Wdata = Wdata.sort_index()
    Wdata['HOUR'] = Wdata.index.hour
    Wdata['HUMIDEX'] = pd.Series([hmdxx(x.TEMP, x.DEW_TEMP) for x in Wdata.itertuples()], index=Wdata.index)
    Wdata['REL_HUM'] = Wdata['REL_HUM'].astype(np.int64)
    return Wdata
def add_latest_historical(stationid, z, conn, year=None, month = None):
    """
    grab most recent data (this month) from Weather Canada in csv form. The dataframe is sorted, column datatypes assigned
    and extra columns HOUR and HUMIDEX are added, while many are dropped. Only returns from latest timestamp in DB to newest in csv.

    :param stationid: station ID to grab from
    :param year: year
    :param month: month
    :return: returns a dataframe that's cleaned
    """

    def read_latest_demand_datetime(conn, tablename):
        query = """select datetime from {}""".format(tablename)
        new = pd.read_sql(query, conn)
        return new.max()

    latest_dt = read_latest_demand_datetime(conn, citydict[z]['tablename'])
    latest_dt_datetime = datetime.datetime(int(latest_dt.values[0][:4]), int(latest_dt.values[0][5:7]), int(latest_dt.values[0][8:10]), int(latest_dt.values[0][11:13]))
    if year and month:
        datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe=1&submit=Download+Data.csv".format(
        stationid, year, month)
    try:
        df = pd.read_csv(datastring, encoding='utf-8', skiprows=16, header=None,
                         names=['DATETIME', 'YEAR', 'MONTH', 'DAY', 'Time', 'TEMP', 'Temp Flag',
                                'DEW_TEMP', 'Dew Point Temp Flag', 'REL_HUM', 'Rel Hum Flag',
                                'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                                'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                                'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])
        Wdata = df[['DATETIME', 'YEAR', 'MONTH', 'DAY', 'TEMP', 'REL_HUM', 'DEW_TEMP']]
        Wdata.set_index('DATETIME', inplace=True)
        Wdata.index = pd.to_datetime(Wdata.index)
    except:
        df = pd.read_csv(datastring, encoding='utf-8', skiprows=17, header=None,
                         names=['DATETIME', 'YEAR', 'MONTH', 'DAY', 'Time', 'TEMP', 'Temp Flag',
                                'DEW_TEMP', 'Dew Point Temp Flag', 'REL_HUM', 'Rel Hum Flag',
                                'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                                'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                                'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])
        Wdata = df[['DATETIME', 'YEAR', 'MONTH', 'DAY', 'TEMP', 'REL_HUM', 'DEW_TEMP']]
        Wdata.set_index('DATETIME', inplace=True)
        Wdata.index = pd.to_datetime(Wdata.index)
    Wdata.dropna(how='any', inplace=True)
    Wdata = Wdata.loc[latest_dt_datetime + datetime.timedelta(hours=1):, :]
    Wdata = Wdata.sort_index()
    Wdata['TEMP'] = Wdata['TEMP'].astype(float)
    Wdata['DEW_TEMP'] = Wdata['DEW_TEMP'].astype(float)
    Wdata['HOUR'] = Wdata.index.hour
    Wdata['HUMIDEX'] = pd.Series([hmdxx(x.TEMP, x.DEW_TEMP) for x in Wdata.itertuples()], index=Wdata.index)
    Wdata['REL_HUM'] = Wdata['REL_HUM'].astype(np.int64)
    return Wdata
def load_latest_data_into_db_hourly():
    """
    Updates DBs with newest data since the last timestamp. Hourly
    :return: nothing
    """
    today = datetime.datetime.now()
    credentials = get_credentials()
    connection_string = "Driver={ODBC Driver 13 for SQL Server};" + "Server={};Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryPassword".format(
        credentials[0], credentials[1], credentials[2], credentials[3])
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus(connection_string)))

    path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
    for z in list(citydict.keys()):
        db = '{}WeatherHistorical.db'.format(z.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        bigdf = add_latest_historical(citydict[z]['stationid'], z, conn, int(today.year), int(today.month))
        bigdf.drop_duplicates(inplace=True)
        bigdf.to_sql(citydict[z]['tablename'], conn, index=True, if_exists='append')
        bigdf.to_sql(citydict[z]['tablename'], engine, index=True, if_exists='append')
        logging.info(str(z) + ':  done')

# previous day's hourly weather scripts
def create_table_previous_hourly(c_, nameOfTable):
    """
    convenient function to create a table

    :param c_: connection to database
    :param nameOfTable: name of table in database
    :return: nothing
    """
    c_.execute(
        "CREATE TABLE IF NOT EXISTS {}(DATETIME TEXT, YEAR SMALLINT, MONTH TINYINT, DAY TINYINT, HOUR TINYINT, TEMP REAL, DEW_TEMP REAL, REL_HUM REAL, HUMIDEX REAL)".format(
            '"' + nameOfTable + '"'))
def data_entry_previous_hourly(c_, nameOfTable, DATETIME, YEAR, MONTH, DAY, HOUR, TEMP, DEW_TEMP, REL_HUM, HUMIDEX):
    """

    adding data to the table, the variables are self-explanatory

    :param c_: connection the the database
    :param nameOfTable: name of the table to add the row
    :param DATETIME:
    :param YEAR:
    :param MONTH:
    :param DAY:
    :param HOUR:
    :param TEMP:
    :param DEW_TEMP:
    :param REL_HUM:
    :param HUMIDEX:
    :return: nothing
    """
    c_.execute(
        'INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{},{})'.format('"' + nameOfTable + '"', DATETIME, YEAR, MONTH,
                                                                     DAY, HOUR, TEMP, DEW_TEMP, REL_HUM, HUMIDEX))
def get_previous_day_weather_hourly(city, stationid, tablename):
    """

    Automates adding new data to each of the database tables. if process cannot complete, tries again in 2 minutes, if still not complete, sends an email
    to work address.

    :param city: city to work on
    :param stationid: station id of said city
    :param tablename: table name for the city
    :return: nothing
    """

    def getpreviousdayweatherinner():
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        db = '{}WeatherHistorical.db'.format(city.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        c2 = conn.cursor()
        date = datetime.datetime.now()
        Wdata = get_new_data_hourly(stationid)
        # Wdata2 = Wdata[Wdata['Day'] == date.day - 1]
        aa = Wdata[(Wdata['DAY'] == (date.day - 1)) | (Wdata['DAY'] == (date.day - 2))]
        bb = aa[aa.index > datetime.datetime(date.year, date.month, date.day - 2, 4)]
        cc = bb[bb.index < datetime.datetime(date.year, date.month, date.day - 1, 5)]
        nameofTable = tablename

        for x in cc.itertuples():
            data_entry_previous_hourly(c2, nameofTable, DATETIME=x.Index, YEAR=x.YEAR, MONTH=x.MONTH, DAY=x.DAY,
                                      HOUR=x.HOUR,
                                      TEMP=x.TEMP, DEW_TEMP=x.DEW_TEMP, REL_HUM=x.REL_HUM, HUMIDEX=x.HUMIDEX)
        conn.commit()
        conn.close()
        copy2(path + db,'H:/python/weatherdata/' + db)
        logging.info("{} database copied to shared folder!".format(city.upper()))
        logging.info("{} got yesterday's data!".format(city.upper()))

    try:
        getpreviousdayweatherinner()
    except Exception as e:
        try:
            logging.info(str(e))
            logging.info('retrying in 2 minutes...')
            time.sleep(180)
            getpreviousdayweatherinner()
        except Exception as ee:
            logging.info(str(ee))
            send_email(text='Error in {} WEATHER PREVIOUS script'.format(city.upper()),
                       html='Error in {} WEATHER PREVIOUS script'.format(city.upper()))
def gather_previous_day_weather_hourly():
    """
    function to run 'getpreviousdayweather' for each city in the citydict
    :return: nothing
    """
    for x in citydict.keys():
        get_previous_day_weather_hourly(x, citydict[x]['stationid'], citydict[x]['tablename'])

# previous day's daily weather scripts
def create_table_previous_daily(c_, nameOfTable):
    """
    convenient function to create a table

    :param c_: connection to database
    :param nameOfTable: name of table in database
    :return: nothing
    """
    c_.execute(
        "CREATE TABLE IF NOT EXISTS {}(DATETIME TEXT, YEAR SMALLINT, MONTH TINYINT, DAY TINYINT, MAX_TEMP REAL, MIN_TEMP REAL, MEAN_TEMP REAL, TOTAL_PRECIP REAL)".format(
            '"' + nameOfTable + '"'))
def data_entry_previous_daily(c_, nameOfTable, DATETIME, YEAR, MONTH, DAY, MAX_TEMP, MIN_TEMP, MEAN_TEMP, TOTAL_PRECIP):
    """

    adding data to the table, the variables are self-explanatory

    :param c_: connection the the database
    :param nameOfTable: name of the table to add the row
    :param DATETIME:
    :param YEAR:
    :param MONTH:
    :param DAY:
    :param MAX_TEMP:
    :param MIN_TEMP:
    :param MEAN_TEMP:
    :param TOTAL_PRECIP:
    :return: nothing
    """
    c_.execute(
        'INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{})'.format('"' + nameOfTable + '"', DATETIME, YEAR, MONTH,
                                                                     DAY, MAX_TEMP, MIN_TEMP, MEAN_TEMP, TOTAL_PRECIP))
def get_previous_day_weather_daily(city, stationid, tablename):
    """

    Automates adding new data to each of the database tables. if process cannot complete, tries again in 2 minutes, if still not complete, sends an email
    to work address.

    :param city: city to work on
    :param stationid: station id of said city
    :param tablename: table name for the city
    :return: nothing
    """

    def getpreviousdayweatherinner():
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        db = '{}WeatherHistorical.db'.format(city.replace(' ', ''))
        conn = sqlite3.connect(path + db)
        c2 = conn.cursor()
        date = datetime.datetime.now()
        Wdata = get_new_data_hourly(stationid)
        Wdata = Wdata[Wdata.index == datetime.datetime(date.year, date.month, date.day - 1)]
        nameofTable = tablename

        for x in Wdata.itertuples():
            data_entry_previous_daily(c2, nameofTable, DATETIME=x.Index, YEAR=x.YEAR, MONTH=x.MONTH, DAY=x.DAY,
                                       MAX_TEMP=x.MAX_TEMP, MIN_TEMP=x.MIN_TEMP, MEAN_TEMP=x.MEAN_TEMP, TOTAL_PRECIP = x.TOTAL_PRECIP)
        conn.commit()
        conn.close()
        copy2(path + db,'H:/python/weatherdata/' + db)
        logging.info("{} (Daily) database copied to shared folder!".format(city.upper()))
        logging.info("{} (Daily) got yesterday's data!".format(city.upper()))

    try:
        getpreviousdayweatherinner()
    except Exception as e:
        try:
            logging.info(str(e))
            logging.info('retrying in 2 minutes...')
            time.sleep(180)
            getpreviousdayweatherinner()
        except Exception as ee:
            logging.info(str(ee))
            send_email(text='Error in {} WEATHER PREVIOUS DAILY script'.format(city.upper()),
                       html='Error in {} WEATHER PREVIOUS DAILY script'.format(city.upper()))
def gather_previous_day_weather_daily():
    """
    function to run 'getpreviousdayweather' for each city in the citydict
    :return: nothing
    """
    for x in citydict.keys():
        get_previous_day_weather_daily(x, citydict[x]['stationid'], citydict[x]['tablename']+ '_Daily')

# forecast scripts
def data_entry_forecast(c_, nameOfTable, timee, temp, feels, humidity, date):
    """

    inserts into table specified all of the values corresponding to the forecast

    :param c_: database connection
    :param nameOfTable: name of table to update
    :param timee: time of forcasted temp
    :param temp: temp in celsius
    :param feels: feels like (humidex temp)
    :param humidity: relative humidity level
    :param date: date of the forecast
    :return: nothing
    """

    c_.execute(
        'INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})'.format(
            '"' + nameOfTable + '"', str(date).split('.')[0],
            timee[0], temp[0], feels[0], humidity[0],
            timee[1], temp[1], feels[1], humidity[1],
            timee[2], temp[2], feels[2], humidity[2],
            timee[3], temp[3], feels[3], humidity[3],
            timee[4], temp[4], feels[4], humidity[4],
            timee[5], temp[5], feels[5], humidity[5],
            timee[6], temp[6], feels[6], humidity[6],
            timee[7], temp[7], feels[7], humidity[7],
            timee[8], temp[8], feels[8], humidity[8],
            timee[9], temp[9], feels[9], humidity[9],
            timee[10], temp[10], feels[10], humidity[10],
            timee[11], temp[11], feels[11], humidity[11],
            timee[12], temp[12], feels[12], humidity[12],
            timee[13], temp[13], feels[13], humidity[13],
            timee[14], temp[14], feels[14], humidity[14],
            timee[15], temp[15], feels[15], humidity[15]))
def create_table_forecast(nameOfTable):
    c2.execute("""CREATE TABLE IF NOT EXISTS {} (CURRENTTIME TEXT, 
                CURRENTHOUR SMALLINT, CURRENTHOURTEMP SMALLINT, CURRENTHOURFEELS SMALLINT, CURRENTHOURHUMIDITY SMALLINT,
                SECONDHOUR SMALLINT, SECONDHOURTEMP SMALLINT, SECONDHOURFEELS SMALLINT, SECONDHOURHUMIDITY SMALLINT,
                THIRDHOUR SMALLINT, THIRDHOURTEMP SMALLINT, THIRDHOURFEELS SMALLINT, THIRDHOURHUMIDITY SMALLINT,
                FOURTHHOUR SMALLINT, FOURTHHOURTEMP SMALLINT, FOURTHHOURFEELS SMALLINT, FOURTHHOURHUMIDITY SMALLINT,
                FIFTHHOUR SMALLINT, FIFTHHOURTEMP SMALLINT, FIFTHHOURFEELS SMALLINT, FIFTHHOURHUMIDITY SMALLINT,
                SIXTHHOUR SMALLINT, SIXTHHOURTEMP SMALLINT, SIXTHHOURFEELS SMALLINT, SIXTHHOURHUMIDITY SMALLINT,
                SEVENTHHOUR SMALLINT, SEVENTHHOURTEMP SMALLINT, SEVENTHHOURFEELS SMALLINT, SEVENTHHOURHUMIDITY SMALLINT,
                EIGHTHHOUR SMALLINT, EIGHTHHOURTEMP SMALLINT, EIGHTHHOURFEELS SMALLINT, EIGHTHHOURHUMIDITY SMALLINT,
                NINTHHOUR SMALLINT, NINTHHOURTEMP SMALLINT, NINTHHOURFEELS SMALLINT, NINTHHOURHUMIDITY SMALLINT,
                TENTHHOUR SMALLINT, TENTHHOURTEMP SMALLINT, TENTHHOURFEELS SMALLINT, TENTHHOURHUMIDITY SMALLINT,
                ELEVENTHHOUR SMALLINT, ELEVENTHHOURTEMP SMALLINT, ELEVENTHHOURFEELS SMALLINT, ELEVENTHHOURHUMIDITY SMALLINT,
                TWELFTHHOUR SMALLINT, TWELFTHHOURTEMP SMALLINT, TWELFTHHOURFEELS SMALLINT, TWELFTHHOURHUMIDITY SMALLINT,
                THIRTEENTHHOUR SMALLINT, THIRTEENTHHOURTEMP SMALLINT, THIRTEENTHHOURFEELS SMALLINT, THIRTEENTHHOURHUMIDITY SMALLINT,
                FOURTEENTHHOUR SMALLINT, FOURTEENTHHOURTEMP SMALLINT, FOURTEENTHHOURFEELS SMALLINT, FOURTEENTHHOURHUMIDITY SMALLINT,
                FIFTEENTHHOUR SMALLINT, FIFTEENTHHOURTEMP SMALLINT, FIFTEENTHHOURFEELS SMALLINT, FIFTEENTHHOURHUMIDITY SMALLINT,
                SIXTEENTHHOUR SMALLINT, SIXTEENTHHOURTEMP SMALLINT, SIXTEENTHHOURFEELS SMALLINT, SIXTEENTHHOURHUMIDITY SMALLINT)""".format(
        '"' + nameOfTable + '"'))
def gather_weather_forecast_hourly(citytimezone, nameofcity, url):
    """

    Go to weather.com's website and scrape the forecast - should be 16 values of each. Tries for 5 minutes
    initially, then 2.5 minutes, then sends an email stating that there was an error.

    :param citytimezone: timezone of the city
    :param nameofcity: name of the city
    :param url: partial url of the site to scrape from
    :return: nothing
    """

    try:
        credentials = get_credentials()
        connection_string = "Driver={ODBC Driver 13 for SQL Server};" + "Server={};Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryPassword".format(
            credentials[0], credentials[1], credentials[2], credentials[3])
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus(connection_string)))

        date = datetime.datetime.now().astimezone(pytz.timezone(citytimezone))
        name = '{}_Weather_Forecast'.format(nameofcity.replace(' ', '_'))
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + '{}weather.db'.format(nameofcity.replace(' ', '')))
        c2 = conn.cursor()
        # parse the Weather Channel's webpage and pulls forecasted weather data
        request = Request('https://weather.com/en-CA/weather/hourbyhour/l/{}'.format(url),
                          headers={'User-Agent': 'Mozilla/5.0'})
        graphsource = urlopen(request).read()
        soup = bs.BeautifulSoup(graphsource, 'html.parser')  # actual and predicted data
        timee = []
        temp = []
        feels = []
        humidity = []
        table = soup.find_all('tr')
        for x in table:
            for y in x.find_all('td'):
                if y.get('headers') == ['time']:
                    timee.append(y.text)
                if y.get('headers') == ['temp']:
                    temp.append(y.text)
                if y.get('headers') == ['feels']:
                    feels.append(y.text)
                if y.get('headers') == ['humidity']:
                    humidity.append(y.text)
        # these variables are for the weather data
        timee = [int(x.replace('\n', '').split(':')[0]) for x in timee]
        temp = [int(x.split('°')[0]) for x in temp]
        feels = [int(x.split('°')[0]) for x in feels]
        humidity = [x.split('%')[0] for x in humidity]
        maxxx = np.argmax(temp)

        col_headers = [
                       "CURRENTHOUR", "CURRENTHOURTEMP", "CURRENTHOURFEELS", "CURRENTHOURHUMIDITY",
                       "SECONDHOUR", "SECONDHOURTEMP", "SECONDHOURFEELS", "SECONDHOURHUMIDITY",
                       "THIRDHOUR", "THIRDHOURTEMP", "THIRDHOURFEELS", "THIRDHOURHUMIDITY",
                       "FOURTHHOUR", "FOURTHHOURTEMP", "FOURTHHOURFEELS", "FOURTHHOURHUMIDITY",
                       "FIFTHHOUR", "FIFTHHOURTEMP", "FIFTHHOURFEELS", "FIFTHHOURHUMIDITY",
                       "SIXTHHOUR", "SIXTHHOURTEMP", "SIXTHHOURFEELS", "SIXTHHOURHUMIDITY",
                       "SEVENTHHOUR", "SEVENTHHOURTEMP", "SEVENTHHOURFEELS", "SEVENTHHOURHUMIDITY",
                       "EIGHTHHOUR", "EIGHTHHOURTEMP", "EIGHTHHOURFEELS", "EIGHTHHOURHUMIDITY",
                       "NINTHHOUR", "NINTHHOURTEMP", "NINTHHOURFEELS", "NINTHHOURHUMIDITY",
                       "TENTHHOUR", "TENTHHOURTEMP", "TENTHHOURFEELS", "TENTHHOURHUMIDITY",
                       "ELEVENTHHOUR", "ELEVENTHHOURTEMP", "ELEVENTHHOURFEELS", "ELEVENTHHOURHUMIDITY",
                       "TWELFTHHOUR", "TWELFTHHOURTEMP", "TWELFTHHOURFEELS", "TWELFTHHOURHUMIDITY",
                       "THIRTEENTHHOUR", "THIRTEENTHHOURTEMP", "THIRTEENTHHOURFEELS", "THIRTEENTHHOURHUMIDITY",
                       "FOURTEENTHHOUR", "FOURTEENTHHOURTEMP", "FOURTEENTHHOURFEELS", "FOURTEENTHHOURHUMIDITY",
                       "FIFTEENTHHOUR", "FIFTEENTHHOURTEMP", "FIFTEENTHHOURFEELS", "FIFTEENTHHOURHUMIDITY",
                       "SIXTEENTHHOUR", "SIXTEENTHHOURTEMP", "SIXTEENTHHOURFEELS", "SIXTEENTHHOURHUMIDITY"]
        data = pd.DataFrame()
        data['Time'] = [int(x.replace('\n', '').split(':')[0]) for x in timee]
        data['Time'] = data['Time'].astype(int)
        data['Temp'] = [int(x.split('°')[0]) for x in temp]
        data['Feels'] = [int(x.split('°')[0]) for x in feels]
        data['Humidity'] = [x.split('%')[0] for x in humidity]
        data['Temp'] = data['Temp'].astype(int)
        data['Feels'] = data['Feels'].astype(int)
        data['Humidity'] = data['Humidity'].astype(int)

        new = pd.concat([pd.DataFrame(data.iloc[x,:]).T for x in range(len(data.index))], axis='columns')
        new.fillna(method='ffill', inplace=True)
        alt_data = pd.DataFrame([new.values[-1]],columns=col_headers, index = [str(date).split('.')[0]])

        try:
            alt_data.to_sql(name, engine, if_exists='append', index=True, index_label="CURRENTTIME")
            data_entry_forecast(c2, name, timee, temp, feels, humidity, date)
            conn.commit()
            logging.info('{} WEATHER FORECAST table updated! Local time: {}'.format(nameofcity.upper(), date))
        except Exception as q:
            logging.info(str(q))
            logging.info(
                '{} WEATHER FORECAST FAILED! Trying again in 5 minutes. Local time: {}'.format(nameofcity.upper(),
                                                                                               date))
            time.sleep(300)
            try:
                alt_data.to_sql(name, engine, if_exists='append', index=True, index_label="CURRENTTIME")
                data_entry_forecast(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                logging.info('{} WEATHER FORECAST table updated! Local time: {}'.format(nameofcity.upper(), date))
            except Exception as i:
                logging.info(str(i))
                logging.info(
                    '{} WEATHER FORECAST FAILED! Trying again in 2.5 minutes. Local time: {}'.format(nameofcity.upper(),
                                                                                                     date))
                time.sleep(150)
                try:
                    alt_data.to_sql(name, engine, if_exists='append', index=True, index_label="CURRENTTIME")
                    data_entry_forecast(c2, name, timee, temp, feels, humidity, date)
                    conn.commit()
                    logging.info('{} WEATHER FORECAST table updated! Local time: {}'.format(nameofcity.upper(), date))
                except Exception as ii:
                    logging.info(str(ii))
                    send_email(text='Error in {} WEATHER FORECAST script | {}'.format(nameofcity.upper(), str(i)),
                               html='Error in {} WEATHER FORECAST script | {}'.format(nameofcity.upper(), str(i)))
    except Exception as e:
        logging.info(str(e))
        send_email(text='Error in {} WEATHER FORECAST script'.format(nameofcity.upper()),
                   html='Error in {} WEATHER FORECAST script'.format(nameofcity.upper()))
def gather_weather_forecasts():
    """

    runs 'gatherweatherforecastupdated' for each city

    :return: nothing
    """
    for x in citiesdict.keys():
        gather_weather_forecast_hourly(citiesdict[str(x)]['timezone'], x, citiesdict[str(x)]['url'])

# send an email
def send_email(text, html):
    """

    Logs on to gmail via smtp and sends an email containing the html verison along with the subject to the senders in the function

    if hmtl version doesn't send for some reason, reverts to the text version.

    :param text: body or message of the email in natural text
    :param html: body or message of the email in html formatting
    :return: nothing
    """
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    curtime = datetime.datetime.now()  # current time and date

    # list of who to send the email to
    TO = ['jragbeer@oxfordproperties.com']
    SUBJECT = 'Error in a Weather script'  # subject line of the email

    TEXT = text
    HTML = html

    # Gmail Sign In
    gmail_sender = 'julienwork789@gmail.com'  # senders email
    gmail_passwd = '12fork34'  # senders password

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    part1 = MIMEText(TEXT, 'plain')  # add the 2 parts of the email (one plain text, one html)
    part2 = MIMEText(HTML, 'html')
    msg.attach(part1)  # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part2)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to the GMAIL server
    server.login(gmail_sender, gmail_passwd)  # login to the GMAIL server

    try:
        server.sendmail(gmail_sender, TO, msg.as_string())  # send email
        logging.info('email sent')  # confirm email is sent, and the time
    except Exception as e:
        logging.info(str(e))  # print error if not sent
        logging.info('error sending mail')  # confirm that email wasn't sent

    server.quit()

#for the weather forecasts
citiesdict = {'Boston': {'url':'USMA0046:1:US', 'timezone': 'America/Toronto'},
              'Berlin': {'url':'10785:4:GM', 'timezone': 'Europe/Berlin'},
              'Vancouver':{'url':'CAXX0518:1:CA', 'timezone': 'America/Vancouver'},
              'Toronto': {'url':'CAXX0504:1:CA', 'timezone': 'America/Toronto'},
              'Mississauga': {'url':'CAXX0295:1:CA', 'timezone': 'America/Toronto'},
              'Edmonton': {'url':'CAXX0126:1:CA', 'timezone': 'America/Edmonton'},
              'Montreal': {'url':'CAXX0301:1:CA', 'timezone': 'America/Toronto'},
              'Gatineau': {'url':'CAXX0158:1:CA', 'timezone': 'America/Toronto'},
              'Calgary': {'url':'CAXX0054:1:CA', 'timezone': 'America/Edmonton'},
              'Washington DC': {'url':'USDC0001:1:US', 'timezone': 'America/Toronto'},
                'Brossard': {'url':'CAXX1183:1:CA', 'timezone': 'America/Toronto'},
            'Quebec City': {'url':'CAXX0385:1:CA', 'timezone': 'America/Toronto'},
            'New York City': {'url':'10022:4:US', 'timezone': 'America/Toronto'}}

# for the previous day's official weather
citydict = {
'Toronto':{'stationid': 48549, 'tablename': 'Toronto_City_Center'},
'Vancouver':{'stationid': 888, 'tablename': 'Vancouver_Harbour_CS'},
'Calgary':{'stationid': 50430, 'tablename': 'Calgary_INTL_A'},
'Edmonton':{'stationid': 53718, 'tablename': 'Edmonton_South_Campus'},
'Brossard':{'stationid': 48374, 'tablename': 'Montreal_St_Hubert'},
'Montreal':{'stationid': 30165, 'tablename': 'Montreal_Pierre_Elliot_Trudeau_INTL'},
'Gatineau':{'stationid': 50719, 'tablename': 'Ottawa_Gatineau_A'},
'Quebec City':{'stationid': 51457, 'tablename': 'Quebec_INTL_A'},
'Mississauga':{'stationid': 51459, 'tablename': 'Toronto_INTL_A'}}

