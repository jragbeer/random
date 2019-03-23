from selenium import webdriver
import time
import bs4 as bs
import re
import datetime
import pandas as pd

path = 'C:/Users/xxx/PycharmProjects/nba/salary data/'
def main(year1, year2):
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

    URL = "https://hoopshype.com/salaries/players/{}-{}/".format(year1, year2)

    soup, driver = grab_soup(URL)
    players = [x.text.strip() for x in soup.findAll('table')[0].findAll('td', {'class': 'name'})]
    salaries = [x.text.strip().replace('$', '').replace(',', '') for x in soup.findAll('table')[0].findAll('td', {'class': 'hh-salaries-sorted'})]
    adjusted_salaries = [x.text.strip().replace('$', '').replace(',', '') for x in soup.findAll('table')[0].findAll('td', {'class': ''})]
    df = pd.DataFrame(data = dict(Player = players[1:], Salary = salaries[1:], AdjustedSalary = adjusted_salaries[1:], Season = ['{}-{}'.format(year1, year2) for x in range(len(players)-1)]))
    driver.quit()
    return df
    # pprint.pprint(souptext)
    # eachline = [x for x in souptext.splitlines() if x != '']
    # matches = [line for line in eachline if re.search(r'^[C][l][o].+$', line)]
    # try:
    #     date = matches[0].split('$')[0]
    #     cost = float(matches[0].split('$')[1])
    # except Exception as e:
    #     logging.info(str(e))
    #     logging.info('len of matches: {}'.format(len(matches)))
    # outdict = {str(datetime.datetime.now()): {'cost':cost, 'date': date}}
    # logging.info(outdict)
    # driver.quit()
timee = datetime.datetime.now()
print(timee)
dataframes = []
for x in range(2006, 2019):
    dataframes.append(main(x, x+1))
bigdf = pd.concat(dataframes)
bigdf.to_csv(path + 'playersalaries.csv', index = False)
print(datetime.datetime.now()-timee)



