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
from urllib.request import HTTPError, URLError
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
def newdegdays(df):
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
def getnewdatahourly(stationid, year=None, month = None):
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
    df = pd.read_csv(datastring, encoding='utf-8', skiprows=17, header=None,
                     names=['DATETIME', 'YEAR', 'MONTH', 'DAY', 'Time', 'TEMP', 'Temp Flag',
                            'DEW_TEMP', 'Dew Point Temp Flag', 'REL_HUM', 'Rel Hum Flag',
                            'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                            'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                            'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])

    Wdata = df[['DATETIME', 'YEAR', 'MONTH', 'DAY','TEMP','REL_HUM', 'DEW_TEMP']]
    Wdata.fillna(method='ffill', inplace=True)
    Wdata.fillna(method='bfill', inplace=True)
    Wdata.set_index('DATETIME', inplace=True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()
    Wdata['HOUR'] = Wdata.index.hour
    Wdata['HUMIDEX'] = pd.Series([hmdxx(x.TEMP, x.DEW_TEMP) for x in Wdata.itertuples()], index=Wdata.index)
    Wdata['REL_HUM'] = Wdata['REL_HUM'].astype(np.int64)
    return Wdata
def load2019data():
    """

    appends to database hourly weather data from jan 1, 2019 onward
    :return: nothing


    """
    for z in citydict.keys():
        today = datetime.datetime.now()
        bigdf = getnewdatahourly(citydict[z]['stationid'], 2019, 1)
        bigdf = bigdf[bigdf.index < datetime.datetime(today.year, today.month, today.day-1, 5)]
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + '{}weather.db'.format(z.replace(' ', '')))
        bigdf.to_sql(citydict[z]['tablename'], conn, index=True, if_exists='append')
        print(z, 'done')
def loadolddataintodb():
    """
    replaces database for weather with all data from 2011 - 2018 that is available. Hourly
    :return: nothing
    """
    for z in citydict.keys():
        dfs = {}
        for x in range(2011, 2019):
            for y in range(1, 13):
                try:
                    dfs['{}_{}'.format(x, y)] = getnewdatahourly(citydict[z]['stationid'], x, y)
                    print('ok', x, y)
                except Exception as e:
                    print(str(e))
                    pass
        bigdf = pd.concat([x for x in dfs.values()])
        bigdf.drop_duplicates(inplace=True)
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + '{}weather.db'.format(z.replace(' ', '')))
        bigdf.to_sql(citydict[z]['tablename'], conn, index=True, if_exists='replace')
        print(z, 'done')
def getnewdatadaily(stationid, year=None):
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
    Wdata.rename({'DATE/TIME': 'DATETIME'},axis = 'columns', inplace = True)
    Wdata.fillna(method='ffill', inplace=True)
    Wdata.fillna(method='bfill', inplace=True)
    Wdata.set_index('DATETIME', inplace=True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()
    return Wdata

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

