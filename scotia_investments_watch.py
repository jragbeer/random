from selenium import webdriver
import time
import bs4 as bs
import re
import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
logging.basicConfig(level=logging.INFO, format = '%(asctime)s,%(message)s',
                    handlers=[logging.FileHandler("scotia_investment_log.txt"),
                              logging.StreamHandler()])
def main():
    def grab_soup(url, browser = "firefox"):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        html = driver.page_source
        time.sleep(1)
        html = driver.execute_script("return document.body.outerHTML;")
        soup = bs.BeautifulSoup(html, 'lxml')
        return soup, driver

    URL = "https://www.scotiafunds.com/scotiafunds/en/fund-overviews/scotia-selected-portfolios/scotia-selected-maximum-growth-portfolio.html"

    soup, driver = grab_soup(URL)
    souptext = soup.text
    eachline = [x for x in souptext.splitlines() if x != '']
    matches = [line for line in eachline if re.search(r'^[C][l][o].+$', line)]
    try:
        date = matches[0].split('$')[0]
        cost = float(matches[0].split('$')[1])
    except Exception as e:
        logging.info(str(e))
        logging.info('len of matches: {}'.format(len(matches)))
    outdict = {str(datetime.datetime.now()): {'cost':cost, 'date': date}}
    logging.info(outdict)
    driver.quit()

logging.info('Running...') #when code is started, display this in the console
sched = BlockingScheduler() #set up a scheduling object
sched.add_job(main, 'cron', minute=22) #run the weather forecast ingest every half an hour
sched.start() #start the scheduler


