import numpy as np
import pandas as pd
import re
import os
import datetime
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle, Spinner, RangeSlider
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
import requests
import bs4 as bs
from bs4 import BeautifulSoup
from pprint import pprint
import pyarrow
import bs4 as bs
from urllib.request import urlopen, Request
from selenium import webdriver
import urllib.request
import requests
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options
import datetime, time

#jragbeer
#better123

# team 1 is home

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'Soccer Predictions'

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
            driver = webdriver.Chrome('C:/Users/Julien/PycharmProjects/practice/chromedriver85', options=chromeOptions)
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
        print(url)
        soup, web_driver = grab_soup(url, "chrome" )
        # allow all elements to load
        time.sleep(1)
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

def download_odds():
    url = "https://www.oddsportal.com/soccer/england/premier-league/west-brom-tottenham-Ao6VwJq3/#double;2"
    soup = get_html_from_page(url)
    df = pd.read_html(str(soup.find_all('div', {'class': "table-container"})))[0]
    print(df.to_string())
def download_538_data():
    df = pd.read_csv("https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv")
    df = df[df['league_id'].isin([2411, 1951, 1869, 1843, 1845, 1854, 1818, 1820])] # EPL, Serie A, La Liga, Ligue 1, MLS, Bundesliga, Europa, UCL
    file_name = today.date().strftime("%Y%m%d") + f"_{today.hour}"
    df.to_parquet(path + f"soccer_betting/538_data_{file_name}.parquet")
    df.to_parquet(path + f"soccer_betting/latest.parquet")

def clean_df():
    df = pd.read_parquet(path + "soccer_betting/latest.parquet", )
    df['date'] = pd.to_datetime(df['date'])
    df.drop(columns = ['league_id', "importance1", "importance2"], inplace=True)
    return df
def per_team(df_, team = 'Manchester City', season = None, ):
    try:
        if season:
            df_ = df_[df_['season'] == season]
        df = df_[(df_['team1'] == team) | (df_['team2'] == team)].copy()
        df = df[df['date'] <= today]
        df['prob_win_tie'] = [i.prob1 if i.team1 == team else i.prob2 for i in df.itertuples()] + df['probtie']
        df['win_tie'] = [i.score1 >= i.score2 if i.team1 == team else i.score2 >= i.score1 for i in df.itertuples()]
        df['won_bet'] = [i.win_tie if i.prob_win_tie > 0.7 else np.nan for i in df.itertuples()]
        print(df.to_string())
        df.dropna(inplace=True)
        print(df.to_string())
        print()
        output = {'wins':len([x for x in df['won_bet'].dropna() if x ]), 'num_bets':len([x for x in df['won_bet'].dropna()])}
        output['pct'] = output['wins'] / output['num_bets']
        return {team:output}
    except:
        print(team, season)
        return {team:{}}
def all_teams(df_, season = 2020, bet = 10, odds = 1.3, win_prob = 0.75):
    odds_bet = odds*bet
    df = df_[df_['season'] == season].copy()
    df.dropna(inplace=True)
    df['prob_win_tie'] = df['prob1'] + df['probtie']
    df['team1_win_tie'] = [i.score1 >= i.score2 for i in df.itertuples()]
    df['won_bet'] = [i.team1_win_tie if i.prob_win_tie > win_prob else np.nan for i in df.itertuples()]
    df.dropna(inplace=True)
    df = df.sort_values('date')
    wow = f"total bets: {len(df.index)}, winning bets: {df['won_bet'].sum()}, win pct: {df['won_bet'].sum()/len(df.index):.2f}" +\
        f" money spent on bets: {bet*len(df.index)}, money won off of bets: {odds_bet*df['won_bet'].sum()}, difference: {odds_bet*df['won_bet'].sum()-bet*len(df.index)}, pct up: {100*((odds_bet*df['won_bet'].sum())-(bet*len(df.index)))/(bet*len(df.index)):.2f}"
    return wow

def update(year, odds, win_prob, league, bet):
    data_ = data[data['league'] == league].copy()
    answer = wrap_in_paragraphs(all_teams(data_, year[0], bet, odds, win_prob))
    div.text = answer

def update_league(attr, old, new):
    update(year_slider.value, odds_spinner.value, win_prob_slider.value, new, bet_spinner.value)
def update_win_prob(attr, old, new):
    update(year_slider.value, odds_spinner.value, new, select_league.value, bet_spinner.value)
def update_spinner(attr, old, new):
    update(year_slider.value, odds_spinner.value, win_prob_slider.value, select_league.value, new)
def update_odds(attr, old, new):
    update(year_slider.value, new, win_prob_slider.value, select_league.value, bet_spinner.value)
def update_year(attr, old, new):
    update(new, odds_spinner.value, win_prob_slider.value, select_league.value, bet_spinner.value)

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True) #prevent numpy exponential notation on print
path = os.getcwd().replace("\\", "/") + "/data/"
today = datetime.datetime.now()

data = clean_df()
data = data[data['league'] == 'Barclays Premier League']

t = {}
for each in data.team1.unique():
    t.update(per_team(data, each, 2020))
pprint(t)

for i in [0.79]:
    for y in range(2016, 2021):
        print()
        print(y, i )
        all_teams(data, y, odds = 1.18, win_prob=i, )


select_league = Select(title='League', value=f"Barclays Premier League", options=sorted(data['league'].unique().tolist()), width=200)
select_league.on_change('value', update_league)

win_prob_slider = Slider(start=0.7, end=1, step=0.01, value=0.75, title="Win Probability", width=200)
win_prob_slider.on_change('value', update_win_prob)

odds_spinner = Spinner(low=1.1, high=1000, step=0.100, value=1.3, title="Odds", width=200)
odds_spinner.on_change('value', update_odds)

bet_spinner = Spinner(title="Bet ($)", low=10, high=100000, step=10, value=5, width=200)
bet_spinner.on_change('value', update_spinner)

year_slider = RangeSlider(start=2016, end=2020, value=(2016,2020), step=1, title="Season", width=200)
year_slider.on_change('value', update_year)

chart = figure(plot_width=600, plot_height=500, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Year", y_axis_label="Win Percentage (%)", toolbar_location="right", title=f"Data")
src = ColumnDataSource({'x':[], 'y':[]})
chart.vbar('x', top='y', source=src, width=0.6, alpha=0.75, name='bars', fill_color='orangered', line_color = 'orangered', line_width = 2)

div = Div(text = wrap_in_paragraphs(all_teams(data[data['league'] == "Barclays Premier League"].copy(), year_slider.value[-1], bet_spinner.value, odds_spinner.value, win_prob_slider.value,  )))

widgets = column([select_league, win_prob_slider, odds_spinner, bet_spinner, year_slider])
dashboard = row([widgets, column([chart, div])])
curdoc().add_root(dashboard)
show(dashboard)
