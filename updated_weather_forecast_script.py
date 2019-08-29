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
        driver = webdriver.Firefox(firefox_options=firefoxOptions)

    driver.get(url_)  # go to the URL
    html = driver.page_source
    time.sleep(1)  # sleep for 1 second  to ensure all JS scripts are loaded
    html = driver.execute_script("return document.body.outerHTML;")  # execute javascript code
    soup_ = bs.BeautifulSoup(html, 'lxml')  # read the data as html (using lxml driver)
    return soup_, driver

citiesdict = {'Toronto': {'url':'CAXX0504:1:CA', 'timezone': 'America/Toronto'},
              'Boston': {'url':'USMA0046:1:US', 'timezone': 'America/Toronto'},
              'Berlin': {'url':'10785:4:GM', 'timezone': 'Europe/Berlin'},
              'Vancouver':{'url':'CAXX0518:1:CA', 'timezone': 'America/Vancouver'},
              'Mississauga': {'url':'CAXX0295:1:CA', 'timezone': 'America/Toronto'},
              'Edmonton': {'url':'CAXX0126:1:CA', 'timezone': 'America/Edmonton'},
              'Montreal': {'url':'CAXX0301:1:CA', 'timezone': 'America/Toronto'},
              'Gatineau': {'url':'CAXX0158:1:CA', 'timezone': 'America/Toronto'},
              'Calgary': {'url':'CAXX0054:1:CA', 'timezone': 'America/Edmonton'},
              'Washington DC': {'url':'USDC0001:1:US', 'timezone': 'America/Toronto'},
                'Brossard': {'url':'CAXX1183:1:CA', 'timezone': 'America/Toronto'},
            'Quebec City': {'url':'CAXX0385:1:CA', 'timezone': 'America/Toronto'},
            'New York City': {'url':'10022:4:US', 'timezone': 'America/Toronto'}}
URL = f'https://weather.com/en-CA/weather/hourbyhour/l/{citiesdict["Toronto"]["url"]}'
path = 'C:/Users/J_Ragbeer/PycharmProjects/final/'

try:
    soup, web_driver = grab_soup(URL)
    time.sleep(3)
    web_driver.find_element_by_xpath("""//*[@id="twc-scrollabe"]/div/button""").click()
    time.sleep(3)
    timee = []
    temp = []
    feels = []
    humidity = []
    precip = []
    wind = []
    html_after_click = web_driver.page_source
    soup = bs.BeautifulSoup(html_after_click, 'html.parser')
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
    wind = [int(x.split('km/h')[0].split(' ')[1].strip()) for x in wind]

    for x in range(len(timee)):
        print(timee[x], temp[x], feels[x], humidity[x], precip[x], wind[x])

    web_driver.quit()  # after all files are downloaded, close the browser instance
except:
    web_driver.quit()
    print(error_handling())
    pass