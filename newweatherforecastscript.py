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

def create_table2(c2,nameOfTable):
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
def gatherweatherforecastVancouver():
    try:
        date = datetime.datetime.now().astimezone(pytz.timezone('America/Vancouver'))
        name = 'Vancouver_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Vancouverweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0518:1:CA').read()
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
            print(date, 'VANCOUVER WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'VANCOUVER WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'VANCOUVER WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in VANCOUVER WEATHER FORECAST script',
                          html='Error in VANCOUVER WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in VANCOUVER WEATHER FORECAST script', html = 'Error in VANCOUVER WEATHER FORECAST script')
def gatherweatherforecastBerlin():
    try:
        date = datetime.datetime.now().astimezone(pytz.timezone('Europe/Berlin'))
        name = 'Berlin_West_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Berlinweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/10785:4:GM').read()
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
            print(date, 'BERLIN WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'BERLIN WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'BERLIN WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in BERLIN WEATHER FORECAST script',
                          html='Error in BERLIN WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in BERLIN WEATHER FORECAST script', html = 'Error in BERLIN WEATHER FORECAST script')
def gatherweatherforecastCalgary():
    try:
        date = datetime.datetime.now().astimezone(pytz.timezone('America/Edmonton'))
        name = 'Calgary_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Calgaryweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0054:1:CA').read()
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
            print(date, 'CALGARY WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'CALGARY WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'CALGARY WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in CALGARY WEATHER FORECAST script',
                          html='Error in CALGARY WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in CALGARY WEATHER FORECAST script', html = 'Error in CALGARY WEATHER FORECAST script')
def gatherweatherforecastEdmonton():
    try:
        date = datetime.datetime.now().astimezone(pytz.timezone('America/Edmonton'))
        name = 'Edmonton_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Edmontonweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0126:1:CA').read()
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
            print(date, 'EDMONTON WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'EDMONTON WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'EDMONTON WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in EDMONTON WEATHER FORECAST script',
                          html='Error in EDMONTON WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in EDMONTON WEATHER FORECAST script', html = 'Error in EDMONTON WEATHER FORECAST script')
def gatherweatherforecastQuebecCity():
    try:
        date = datetime.datetime.now()
        name = 'Quebec_City_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'QuebecCityweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0385:1:CA').read()
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
            print(date, 'QUEBEC CITY WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'QUEBEC CITY WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'QUEBEC CITY WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in QUEBEC CITY WEATHER FORECAST script',
                          html='Error in QUEBEC CITY WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in QUEBEC CITY WEATHER FORECAST script', html = 'Error in QUEBEC CITY WEATHER FORECAST script')
def gatherweatherforecastMississauga():
    try:
        date = datetime.datetime.now()
        name = 'Mississauga_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Mississaugaweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0295:1:CA').read()
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
            print(date, 'MISSISSAUGA WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'MISSISSAUGA WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'MISSISSAUGA WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in MISSISSAUGA WEATHER FORECAST script',
                          html='Error in MISSISSAUGA WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in MISSISSAUGA WEATHER FORECAST script', html = 'Error in MISSISSAUGA WEATHER FORECAST script')
def gatherweatherforecastGatineau():
    try:
        date = datetime.datetime.now()
        name = 'Gatineau_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Gatineauweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/caxx0158:1:ca').read()
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
            print(date, 'GATINEAU WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'GATINEAU WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'GATINEAU WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in GATINEAU WEATHER FORECAST script',
                          html='Error in GATINEAU WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in GATINEAU WEATHER FORECAST script', html = 'Error in GATINEAU WEATHER FORECAST script')
def gatherweatherforecastNewYorkCity():
    try:
        date = datetime.datetime.now()
        name = 'New_York_City_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'NewYorkCityweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/10022:4:us').read()
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
            print(date, 'NYC WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'NYC WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'NYC WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in NYC WEATHER FORECAST script', html='Error in NYC WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in NYC WEATHER FORECAST script', html = 'Error in NYC WEATHER FORECAST script')
def gatherweatherforecastMontreal():
    try:
        date = datetime.datetime.now()
        name = 'Montreal_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Montrealweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0301:1:CA').read()
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
            print(date, 'MONTREAL WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'MONTREAL WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'MONTREAL WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in MONTREAL WEATHER FORECAST script',
                          html='Error in MONTREAL WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in MONTREAL WEATHER FORECAST script', html = 'Error in MONTREAL WEATHER FORECAST script')
def gatherweatherforecastBrossard():
    try:
        date = datetime.datetime.now()
        name = 'Brossard_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Brossardweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX1183:1:CA').read()
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
            print(date, 'BROSSARD WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'BROSSARD WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'BROSSARD WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in BROSSARD WEATHER FORECAST script',
                          html='Error in BROSSARD WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in BROSSARD WEATHER FORECAST script', html = 'Error in BROSSARD WEATHER FORECAST script')
def gatherweatherforecastWashingtonDC():
    try:
        date = datetime.datetime.now()
        name = 'Washington_DC_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'WashingtonDCweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/USDC0001:1:US').read()
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
            print(date, 'WASHINGTON DC WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'WASHINGTON DC WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'WASHINGTON DC WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in WASHINGTON DC WEATHER FORECAST script',
                          html='Error in WASHINGTON DC WEATHER FORECAST script')

    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in WASHINGTON DC WEATHER FORECAST script', html = 'Error in WASHINGTON DC WEATHER FORECAST script')
def gatherweatherforecastBoston():
    try:
        date = datetime.datetime.now()
        name = 'Boston_Weather_Forecast'
        path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
        conn = sqlite3.connect(path + 'Bostonweather.db')
        c2 = conn.cursor()


        #parse the Weather Channel's webpage and pulls forecasted weather data
        graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/USMA0046:1:US').read()
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
            print(date, 'BOSTON WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'BOSTON WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'BOSTON WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in BOSTON WEATHER FORECAST script',
                          html='Error in BOSTON WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in BOSTON WEATHER FORECAST script', html = 'Error in BOSTON WEATHER FORECAST script')
def gatherweatherforecastToronto():
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
            print(date, 'TORONTO WEATHER FORECAST table updated!')
        except Exception as q:
            print(str(q))
            print(date, 'TORONTO WEATHER FORECAST FAILED! Trying again in 5 minutes.')
            time.sleep(300)
            try:
                data_entry2(c2, name, timee, temp, feels, humidity, date)
                conn.commit()
                print(date, 'TORONTO WEATHER FORECAST table updated!')
            except Exception as i:
                print(str(i))
                sendemail(text='Error in TORONTO WEATHER FORECAST script',
                          html='Error in TORONTO WEATHER FORECAST script')
    except Exception as e:
        print(str(e))
        sendemail(text = 'Error in TORONTO WEATHER FORECAST script', html = 'Error in TORONTO WEATHER FORECAST script')

def sendemail(text, html):
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    curtime = datetime.datetime.now()  # current time and date

    # list of who to send the email to
    TO = ['xx']
    SUBJECT = 'Error in script'  # subject line of the email

    TEXT = text
    HTML = html

    # Gmail Sign In
    gmail_sender = 'xx'  # senders email
    gmail_passwd = 'xx'  # senders password

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


# date = datetime.datetime.now()
# name = 'Toronto_Weather_Forecast'
# path = r'C:/Users/J_Ragbeer/PycharmProjects/weatherdata/'
# conn = sqlite3.connect(path + 'Berlinweather.db')
# c2 = conn.cursor()
# tablename = 'Berlin_West_Weather_Forecast'
# create_table2(c2, tablename)
