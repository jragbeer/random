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
import pytz

def hmdxx(x, y):
    # x is air temp in Celsius
    # y is dewpoint in Celsius
    return x + (0.5555 * (6.11 * np.exp(5417.7530 * ((1 / 273.16) - (1 / (273.15 + y)))) - 10))
def clean_weather(weather):
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
    weather['Temp'] = weather['Temp (°C)']
    weather['Dew Point Temp'] = weather['Dew Point Temp (°C)']
    weather.drop(['Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)',
                  'Wind Spd Flag', 'Visibility (km)', 'Visibility Flag', 'Temp Flag', 'Dew Point Temp Flag',
                  'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx Flag', 'Wind Chill', 'Rel Hum (%)', 'Hmdx',
                  'Dew Point Temp',
                  'Wind Chill Flag', 'Weather', 'Temp (°C)', 'Dew Point Temp (°C)'], 1, inplace=True)
    return weather
def newdegdays(df):
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
def create_table(nameOfTable):
    c2.execute("CREATE TABLE IF NOT EXISTS {}(DATETIME TEXT, YEAR SMALLINT, MONTH TINYINT, DAY TINYINT, HOUR TINYINT, TEMP REAL, DEW_TEMP REAL, REL_HUM REAL, HUMIDEX REAL)".format('"'+nameOfTable+'"'))
def data_entry(c2,nameOfTable, DATETIME, YEAR, MONTH, DAY, HOUR, TEMP, DEW_TEMP, REL_HUM, HUMIDEX):
    c2.execute('INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{},{})'.format('"'+nameOfTable+'"', DATETIME, YEAR, MONTH, DAY, HOUR, TEMP, DEW_TEMP, REL_HUM, HUMIDEX))
def getnewdata(stationid):
    date = datetime.datetime.now()
    datastring = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe=1&submit=Download+Data".format(
        stationid, date.year, date.month)
    df = pd.read_csv(datastring, encoding='utf-8', skiprows=17, header=None,
                     names=['Date/Time', 'Year', 'Month', 'Day', 'Time', 'Temp (C)', 'Temp Flag',
                            'Dew Point Temp (C)', 'Dew Point Temp Flag', 'Rel Hum (%)', 'Rel Hum Flag',
                            'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)', 'Wind Spd Flag',
                            'Visibility (km)', 'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag',
                            'Hmdx', 'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather'])

    Wdata = df[['Year', 'Day', 'Month', 'Date/Time', 'Temp (C)', 'Dew Point Temp (C)', 'Rel Hum (%)']]
    Wdata.fillna(method='ffill', inplace=True)
    Wdata.fillna(method='bfill', inplace=True)
    Wdata.set_index('Date/Time', inplace=True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()
    return Wdata
def getpreviousdayweather(city,stationid, tablename):
    try:
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + '{}weather.db'.format(city.replace(' ', '')))
        c2 = conn.cursor()
        date = datetime.datetime.now()
        Wdata = getnewdata(stationid)
        Wdata['Hour'] = Wdata.index.hour
        Wdata['Humidex'] = pd.Series([hmdxx(x[4], x[5]) for x in Wdata.itertuples()], index=Wdata.index)

        Wdata2 = Wdata[Wdata['Day'] == date.day-1]

        nameofTable = tablename

        for x in Wdata2.itertuples():
            data_entry(c2,nameofTable, DATETIME= x[0], YEAR=x[1], MONTH=x[3], DAY=x[2], HOUR=x[7], TEMP=x[4], DEW_TEMP=x[5], REL_HUM=x[6], HUMIDEX=x[8])
        conn.commit()
        conn.close()
        print(date, '{} got yesterday\'s data!'.format(city.upper()))
    except Exception as e:
        print(str(e))
        sendemail(text='Error in {} WEATHER PREVIOUS script'.format(city.upper()), html='Error in {} WEATHER PREVIOUS script'.format(city.upper()))
def gatherpreviousdayweather():
    for x in citydict.keys():
        getpreviousdayweather(x, citydict[x]['stationid'], citydict[x]['tablename'])
def data_entry2(c2, nameOfTable, timee, temp, feels, humidity, date):
    c2.execute('INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})'.format('"'+nameOfTable+'"', str(date).split('.')[0],
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
def gatherweatherforecast():
    try:
        date = datetime.datetime.now()
        name = 'Toronto_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Torontoweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0504:1:CA').read()
        soup = bs.BeautifulSoup(graphsource,'html.parser') #actual and predicted data
        timee=[]
        temp=[]
        feels = []
        humidity=[]
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
        #these variables are for the weather data
        timee= [int(x.replace('\n','').split(':')[0]) for x in timee]
        temp = [int(x.split('°')[0]) for x in temp]
        feels = [int(x.split('°')[0]) for x in feels]
        humidity = [x.split('%')[0] for x in humidity]
        maxxx = np.argmax(temp)

        # for x in range(len(temp)):
        #     print(temp[x], feels[x], humidity[x], timee[x])

        try:
            data_entry2(c2, name, timee, temp, feels, humidity, date)
            conn.commit()
            print(date, 'table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            data_entry2(c2, name, timee, temp, feels, humidity, date)
            conn.commit()
            print(date, 'table updated!')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in TORONTO WEATHER FORECAST script', html = 'Error in TORONTO WEATHER FORECAST script')
def sendemail(text, html):
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    curtime = datetime.datetime.now()  # current time and date

    # list of who to send the email to
    TO = ['jragbeer@oxfordproperties.com']
    SUBJECT = 'Error in script'  # subject line of the email

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
        print(curtime, 'email sent')  # confirm email is sent, and the time
    except Exception as e:
        print(str(e))  # print error if not sent
        print(curtime, 'error sending mail')  # confirm that email wasn't sent

    server.quit()
def create_table2(nameOfTable):
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
                SIXTEENTHHOUR SMALLINT, SIXTEENTHHOURTEMP SMALLINT, SIXTEENTHHOURFEELS SMALLINT, SIXTEENTHHOURHUMIDITY SMALLINT)""".format('"'+nameOfTable+'"'))
def gatherweatherforecastupdated(citytimezone, nameofcity, url):
    try:
        date = datetime.datetime.now().astimezone(pytz.timezone(citytimezone))
        name = '{}_Weather_Forecast'.format(nameofcity.replace(' ', '_'))
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + '{}weather.db'.format(nameofcity.replace(' ', '')))
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/{}'.format(url)).read()
        soup = bs.BeautifulSoup(graphsource,'html.parser') #actual and predicted data
        timee=[]
        temp=[]
        feels = []
        humidity=[]
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
        #these variables are for the weather data
        timee= [int(x.replace('\n','').split(':')[0]) for x in timee]
        temp = [int(x.split('°')[0]) for x in temp]
        feels = [int(x.split('°')[0]) for x in feels]
        humidity = [x.split('%')[0] for x in humidity]
        maxxx = np.argmax(temp)

        # for x in range(len(temp)):
        #     print(temp[x], feels[x], humidity[x], timee[x])

        try:
            data_entry2(c2, name, timee, temp, feels, humidity, date)
            conn.commit()
            print(date, '{} WEATHER FORECAST table updated!'.format(nameofcity.upper()))
        except Exception as q:
            print(str(q))
            print(date, '{} WEATHER FORECAST FAILED! Trying again in 5 minutes.'.format(nameofcity.upper()))
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, '{} WEATHER FORECAST table updated!'.format(nameofcity.upper()))
            except Exception as i:
                print(str(i))
                sendemail(text='Error in {} WEATHER FORECAST script'.format(nameofcity.upper()),
                          html='Error in {} WEATHER FORECAST script'.format(nameofcity.upper()))
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in {} WEATHER FORECAST script'.format(nameofcity.upper()), html = 'Error in {} WEATHER FORECAST script'.format(nameofcity.upper()))
def weatherforecastscripts():
    for x in citiesdict.keys():
        gatherweatherforecastupdated(citiesdict[str(x)]['timezone'], x, citiesdict[str(x)]['url'])

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

print('Running...') #when code is started, display this in the console
sched = BlockingScheduler() #set up a scheduling object

sched.add_job(gatherpreviousdayweather, 'cron', hour=6) #run the weather ingest every morning at 5am
sched.add_job(weatherforecastscripts, 'cron', minute=30) #run the weather forecast ingest every half an hour

sched.start() #start the scheduler

#