from selenium import webdriver
import traceback
import time
import bs4 as bs
import datetime
import pandas as pd
import re
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.firefox.options import Options
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import logging
import pickle
import smtplib
import socket
import urllib
import sys
import pytz
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing as mp


def error_handling():
    """

    This function returns a string with all of the information regarding the error

    :return: string with the error information
    """
    return traceback.format_exc()


def grab_soup(url_, browser="firefox"):
    """
    This function enables a driver (using Firefox or Chrome), goes to the URL, and retrieves the data after the JS is loaded.

    :param url_: url to go to to retrieve data
    :param browser: browser to use, defaults to firefox (requires geckodriver.exe on path)
    :return:

    soup - the data of the page
    driver - the browser (process) instance
    """
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        firefoxOptions = Options()
        firefoxOptions.set_preference("browser.download.folderList", 2)
        firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
        firefoxOptions.set_preference("browser.download.dir", path.replace('/', '\\') + 'data\\downloads\\')
        firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                      "application/octet-stream,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        driver = webdriver.Firefox(options=firefoxOptions)

    driver.get(url_)  # go to the URL
    html = driver.page_source
    time.sleep(1)  # sleep for 1 second  to ensure all JS scripts are loaded
    html = driver.execute_script("return document.body.outerHTML;")  # execute javascript code
    soup_ = bs.BeautifulSoup(html, 'lxml')  # read the data as html (using lxml driver)
    return soup_, driver


def hourly_forecast_24(citytimezone, nameofcity, url, q):
    try:
        datee = datetime.datetime.now().astimezone(pytz.timezone(citytimezone))
        name = '{}_Weather_Forecast_24'.format(nameofcity.replace(' ', '_'))
        soup, web_driver = grab_soup(url, )
        # allow all elements to load
        time.sleep(22)
        web_driver.find_element_by_xpath("""//*[@id="twc-scrollabe"]/div/button""").click()
        # allow all elements to load
        time.sleep(23)
        timee = []
        temp = []
        feels = []
        humidity = []
        precip = []
        wind = []
        # reload html after JS interaction
        html_after_click = web_driver.page_source
        soup = bs.BeautifulSoup(html_after_click, 'html.parser')
        # find the table and parse it
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
                if y.get('headers') == ['precip']:
                    precip.append(y.text)
                if y.get('headers') == ['wind']:
                    wind.append(y.text)
        # these variables are for the weather data
        timee = [int(x.replace('\n', '').split(':')[0]) for x in timee]
        temp = [int(x.split('°')[0]) for x in temp]
        feels = [int(x.split('°')[0]) for x in feels]
        humidity = [int(x.split('%')[0]) for x in humidity]
        precip = [int(x.split('%')[0]) for x in precip]
        wind = [0 if x.upper() == 'CALM' else int(x.split('km/h')[0].split(' ')[1].strip()) for x in wind]
        # wind = [int(x.split('km/h')[0].split(' ')[1].strip()) for x in wind]
        # wind = [int(x.split('km/h')[0]) for x in wind]
        # create names of columns in dataframe
        hours = ['current', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth',
                 'nineth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth',
                 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twentyfirst',
                 'twentysecond', 'twentythird']
        capture_list = ['hour', 'temp', 'feels', 'humidity', 'precip', 'wind']
        column_names = ["CURRENT_TIME"] + [str(x + '_hour_' + i).upper() for x in hours for i in capture_list]
        # create blank data frame from column names
        df = pd.DataFrame({ii: 0 for ii in column_names}, index=[0])
        all_values = [each_list[hr] for hr in range(len(timee)) for each_list in
                      [timee, temp, feels, humidity, precip, wind]]
        # update each column with data, including current time
        for x in range(1, len(df.columns)):
            df.iloc[0, x] = all_values[x - 1]
        df.iloc[0, 0] = str(datee).split('.')[0]
        print(nameofcity)
        print(df.to_string())
        # df.to_sql(name, engine, if_exists='append', index=False)
        web_driver.quit()  # after all files are downloaded, close the browser instance
        try:
            q.put('over')  # message to send to the queue - if run in standalone, does nothing.
        except:
            pass
    except:
        web_driver.quit()
        print(error_handling())
        sys.exit()


def extract():
    """
    This function runs each of the data extraction scripts concurrently.
    :return: nothing
    """
    q = mp.Queue()  # put each process on a queue, so when finished,
    new = {}
    for city in citiesdict.keys():
        URL = f'https://weather.com/en-CA/weather/hourbyhour/l/{citiesdict[city]["url"]}'
        new[city] = Process(target=hourly_forecast_24,
                     args=(citiesdict[city]["timezone"], city, URL, q,))  # assign process X the function
        new[city].start()  # start processes

    procs = []
    while True:  # check if processes are finished every 8 seconds
        time.sleep(1)
        procs.append(q.get())
        if len(procs) == len(list(citiesdict.keys())):  # once all processes are complete, break loop
            break
    if procs == ['over' * len(list(citiesdict.keys()))]:  # if all 3 processes finish successfully, terminate them
        for x in new:
            new[x].terminate()
    # join the processes so that they (and the parent process) finish and release resources at the same time
    for x in new:
        new[x].join()
    q.close()  # close the queue (release resources)


citiesdict = {'Toronto': {'url': 'CAXX0504:1:CA', 'timezone': 'America/Toronto'},
              'Boston': {'url': 'USMA0046:1:US', 'timezone': 'America/Toronto'},
              'Berlin': {'url': '10785:4:GM', 'timezone': 'Europe/Berlin'},
              'Vancouver': {'url': 'CAXX0518:1:CA', 'timezone': 'America/Vancouver'},
              'Mississauga': {'url': 'CAXX0295:1:CA', 'timezone': 'America/Toronto'},
              'Edmonton': {'url': 'CAXX0126:1:CA', 'timezone': 'America/Edmonton'},
              'Montreal': {'url': 'CAXX0301:1:CA', 'timezone': 'America/Toronto'},
              'Gatineau': {'url': 'CAXX0158:1:CA', 'timezone': 'America/Toronto'},
              'Calgary': {'url': 'CAXX0054:1:CA', 'timezone': 'America/Edmonton'},
              'Washington DC': {'url': 'USDC0001:1:US', 'timezone': 'America/Toronto'},
              'Brossard': {'url': 'CAXX1183:1:CA', 'timezone': 'America/Toronto'},
              'Quebec City': {'url': 'CAXX0385:1:CA', 'timezone': 'America/Toronto'},
              'New York City': {'url': '10022:4:US', 'timezone': 'America/Toronto'}}


# for x in citiesdict.keys():
#     URL = f'https://weather.com/en-CA/weather/hourbyhour/l/{citiesdict[x]["url"]}'
#     hourly_forecast_24(citiesdict[x]["timezone"], x, URL)
path = 'C:/Users/J_Ragbeer/PycharmProjects/final/'
if __name__ == '__main__':

    ouch = datetime.datetime.now()

    extract()
    print(datetime.datetime.now()-ouch)
