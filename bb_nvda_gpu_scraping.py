import numpy as np
import pandas as pd
import re, os, sys
import datetime, time
import traceback
import pickle
from pprint import pprint
import pyarrow
from sqlalchemy import create_engine
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options
from dateutil import parser
from tqdm import tqdm
import sqlite3
import calendar
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib


path = os.getcwd().replace("\\", "/") + "/data/"
timee = datetime.datetime.now()
print(timee)

#SQLITE3 DATABASE (matchup)
engine = sqlite3.connect(path + 'bb_nvda_drops_data.db')



def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""
def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()
def get_html_from_page(url,):
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
            chromeOptions = chrome_options()
            chromeOptions.add_experimental_option("prefs", {
                "download.default_directory": r"C:\Users\J_Ragbeer\Downloads",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
            chromeOptions.add_argument("--disable-gpu")
            chromeOptions.add_argument("--headless")
            chromeOptions.add_argument('--no-sandbox')
            chromeOptions.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome("C:/Users/Julien/PycharmProjects/practice/chromedriver93", options=chromeOptions)
        else:
            firefoxOptions = firefox_options()
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
    try:
        soup, web_driver = grab_soup(url, "chrome" )
        # allow all elements to load
        time.sleep(6)
        # reload html after JS interaction
        html_ = web_driver.page_source
        soup = bs.BeautifulSoup(html_, 'html.parser')
        try:
            return soup
        except:
            print('ERROR')
            return soup.text
    except:
        web_driver.quit()
        print(error_handling())
        sys.exit()
def get_newest_best_buy_page():
    soup = get_html_from_page("https://blog.bestbuy.ca/best-buy/nvidia")
    post_views = soup.find('div', {"class": 'td-post-views'}).text
    posted_date = soup.find_all('span', {"class": 'td-post-date'})
    posted_dates = [each.text for each in posted_date]
    stuff = soup.text
    ok = stuff[stuff.find('Here are the'):stuff.find('Here are the') + 400]
    drop_date = None
    matches = re.findall(r'(\w+ \d+(th|rd|st|nd)? )', ok)
    for m in matches:
        try:
            if parser.parse(m[0]):
                drop_date = m[0]
        except:
            error_handling()
    output_df = pd.DataFrame({'query_time':str(datetime.datetime.now()), 'drop_date':drop_date, 'post_views':post_views, 'posted_dates':repr(posted_dates)}, index = [0])
    # print(output_df.to_string())
    output_df.to_sql('scraped_data', engine, if_exists='append', index=False)
def verify_if_new_drop_date():
    df = pd.read_sql('select * from scraped_data order by query_time desc limit 3', engine).sort_values('query_time', ascending=True)
    assert df.iloc[len(df.index)-1, df.columns.get_loc('post_views')] >= df.iloc[len(df.index)-2, df.columns.get_loc('post_views')]
    prev_date = parser.parse(df.iloc[len(df.index)-2, df.columns.get_loc('drop_date')])
    next_date = parser.parse(df.iloc[len(df.index)-1, df.columns.get_loc('drop_date')])
    query_date = df.iloc[len(df.index)-1, df.columns.get_loc('query_time')]
    if next_date > prev_date:
        print("NEW DROP DATE")
        print(next_date)
        sendemail_(f'NEW DROP DATE: {next_date}. It is {next_date.strftime("%B %d, %Y")}. Queried: {parser.parse(query_date)} ET',
                   wrap_in_paragraphs(f'WOO NEW DROP DATE: {next_date}. <br><br>It is {next_date.strftime("%B %d, %Y")}.<br><br>Queried: {parser.parse(query_date)} ET'))
    else:
        print("NOT A NEW DROP DATE")
        print(prev_date, next_date)
def sendemail_(TEXT, HTML):
    """

    This function sends emails to the email list depending on the para

    :param TEXT: text to send in an email
    :param HTML: text to send in an email, but in HTML (default)
    :param week_start: integer that indicates if this is the email sent weekly (start of the week, monday at 7am)
    :param error_email: if this is an error email, send an alert with a different message
    :return:
    """
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    # current date, and a date 5 days away
    curtime = datetime.datetime.now().date()
    week_from_today = curtime + datetime.timedelta(days=5)

    SUBJECT = 'NEW BEST BUY / NVIDIA DROP DATE!'
    TO = [my_email,
          petrits_email,
          ]

    # Gmail Sign In
    gmail_sender = senders_email
    gmail_passwd = senders_pswd

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    # add the 2 parts of the email (one plain text, one html)
    part1 = MIMEText(TEXT, 'plain')
    part2 = MIMEText(HTML, 'html')
    # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part1)
    msg.attach(part2)

    # connect to the GMAIL server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # login to the GMAIL server
    server.login(gmail_sender, gmail_passwd)

    try:
        # send email and confirm email is sent / time it is sent
        server.sendmail(gmail_sender, TO, msg.as_string())
        logging.info(str(curtime) + ' email sent')
    except Exception as e:
        # print error if not sent, and confirm it wasn't sent
        logging.info(str(e))
        logging.info(error_handling())
        logging.info(str(curtime) + ' error sending mail')

    server.quit()

get_newest_best_buy_page()
verify_if_new_drop_date()

