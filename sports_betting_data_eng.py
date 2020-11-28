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
from dask.distributed import Client, LocalCluster
import dask.delayed
from bokeh.models import ColumnDataSource
from credentials import personal_db_engine
import sqlite3

def convert_unix_timestamp_to_pandas_date(input_date):
    return pd.to_datetime(datetime.datetime.fromtimestamp(input_date/1000).date())
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
def download_538_data():
    df = pd.read_csv("https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv")
    df = df[df['league_id'].isin([2411, 1869, 1843, 1845, 1854, 1818, 1820])] # EPL, Serie A, La Liga, Ligue 1, Bundesliga, Europa, UCL
    file_name = today.date().strftime("%Y%m%d") + f"_{today.hour}"
    df.to_parquet(data_path + f"/538_data_historical/538_data_{file_name}.parquet")
    df.to_parquet(data_path + f"latest_538_data.parquet")
# @dask.delayed
def get_odds_as_record(df_, link, league):
    try:
        a = get_odds_of_game(link, league)
        tmp_odds_df = a['odds']
        # team names may not map, (team 1 in OddsPortal may not be team 1 in 538) this fixes names across the two datasets
        haha = pd.concat([pd.DataFrame(tmp_odds_df.loc['Average', :]).T.rename(columns={i: 'avg_' + i for i in tmp_odds_df.columns}),
                         pd.DataFrame(tmp_odds_df.loc['Highest', :]).T.rename(columns={i: 'max_' + i for i in tmp_odds_df.columns})], axis=1).fillna(method='ffill').fillna(method='bfill').drop_duplicates(subset=['avg_1X', 'max_1X'])
        ind = find_index(df_, a)
        output = pd.concat([haha, ind], axis=1).fillna(method='ffill').fillna(method='bfill').drop_duplicates(keep = 'last').reset_index(drop=True)
        output['link'] = link
        if output.at[0, 'team1'] == a['fixed_team1'] or output.at[0, 'team2'] == a['fixed_team2']:
            pass
        elif output.at[0, 'team1'] == a['fixed_team2']:
            output.rename(columns={'avg_1X': 'avg_2X', 'high_1X': 'high_2X',
                                'avg_2X': 'avg_1X', 'high_2X': 'high_1X'}, inplace=True)
        else:
            print("THIS MEANS NO TEAMS MATCH")
            outer.append(link)
            raise Exception
        return output
    except:
        print(error_handling())
        pprint(a)
        print()
        return pd.DataFrame()
def get_games(league, szn, page):
    try:
        if szn != '':
            szn_ = '-' + str(szn)
        else:
            szn_ = szn
        country = nation_league_mapper[league]
        url = f"https://www.oddsportal.com/soccer/{country}/{league.replace(' ', '-')}{szn_}/results/#/page/{page}/"
        soup = get_html_from_page(url)
        links = soup.find_all('td', {'class': 'name table-participant'})
        hrefs = [x.find('a',href=True)['href'] for x in links]
        return hrefs
    except:
        print('No Data')
        print(url)
        return []
def get_odds_of_game(url, league):
    try:
        URL = "https://www.oddsportal.com" + url + "#double;2"
        soup = get_html_from_page(URL)
        table = soup.find('div', {'id': 'odds-data-table'})
        df = pd.read_html(str(table))[0]
        df = df[(df['Bookmakers'] == "Average") | (df['Bookmakers'] == "Highest")][['Bookmakers', '1X', '12', 'X2']]
        game = soup.find('h1').string
        event_date = parser.parse(soup.find('p', {'class': 'date'}).string.split(',')[1]).date()
        t1 = game.split(' - ')[0]
        t2 = game.split(' - ')[1]
        try:
            odds_team1 = team_name_mapper[t1.split("(")[0].strip()]
        except:
            odds_team1 = t1
        try:
            odds_team2 = team_name_mapper[t2.split("(")[0].strip()]
        except:
            odds_team2 = t2
        return {'odds':df.set_index("Bookmakers", drop=True), 'game':game, 'date':event_date, 'league':league, 'team1': t1,'team2': t2, "fixed_team2": odds_team2, "fixed_team1": odds_team1, 'url':url}
    except:
        print('No Data')
        print(url)
        return []
def feature_eng(df, win_prob = 0.75):
    df['prob1_win_tie'] = df['prob1'] + df['probtie']
    df['team1_win_tie'] = [i.score1 >= i.score2 for i in df.itertuples()]
    df['prob2_win_tie'] = df['prob2'] + df['probtie']
    df['team2_win_tie'] = [i.score1 <= i.score2 for i in df.itertuples()]
    k = []
    win = []
    for i in df.itertuples():
        if i.prob1_win_tie > i.prob2_win_tie:
            if i.prob1_win_tie > win_prob:
                k.append(i.team1_win_tie)

            else:
                k.append(np.nan)
        elif i.prob2_win_tie > i.prob1_win_tie:
            if i.prob2_win_tie > win_prob:
                k.append(i.team2_win_tie)
            else:
                k.append(np.nan)
        else:
            k.append(np.nan)

        if i.score1 > i.score2:
            win.append(i.team1)
        elif i.score1 < i.score2:
            win.append(i.team2)
        else:
            win.append("Tie")
    df['won_bet'] = k
    df['game_winner'] = win
    df['prob_win_tie'] = df[["prob1_win_tie", "prob2_win_tie"]].max(axis=1)
    # df = df.dropna(subset=[i for i in df.columns if i != 'won_bet']).sort_values('date')
    return df
def clean_df():
    df = pd.read_parquet(data_path + "latest_538_data.parquet", )
    df['date'] = pd.to_datetime(df['date'])
    df['league'] = df['league'].map(league_mapper)
    df.drop(columns = ['league_id', "importance1", "importance2"], inplace=True)
    return df
def per_team(df_, team = 'Manchester City', season = (2016, 2020), ):
    try:
        df_ = df_[(df_['season'] >= season[0]) & (df_['season'] <= season[1])].copy()
        df = df_[(df_['team1'] == team) | (df_['team2'] == team)].copy()
        df = df[df['date'] <= today]
        df['prob_win_tie'] = [i.prob1 if i.team1 == team else i.prob2 for i in df.itertuples()] + df['probtie']
        df['win_tie'] = [i.score1 >= i.score2 if i.team1 == team else i.score2 >= i.score1 for i in df.itertuples()]
        df['won_bet'] = [i.win_tie if i.prob_win_tie > 0.7 else np.nan for i in df.itertuples()]
        # print(df.to_string())
        df.dropna(inplace=True)
        # print(df.to_string())
        # print()
        output = {'wins':len([x for x in df['won_bet'].dropna() if x ]), 'num_bets':len([x for x in df['won_bet'].dropna()])}
        output['pct'] = output['wins'] / output['num_bets']
        return {team:output}
    except:
        print(team, season)
        print(error_handling())
        return {}
def gather_game_links_serial():
    haha = {}
    for t in nation_league_mapper.keys():
        haha[t] = {}
        for yr in years:
            haha[t][yr] = []
            for page in range(1, 10):
                haha[t][yr].append(get_games(t, yr, page))
        print(t, datetime.datetime.now() - today)
        pickle_out = open(data_path + "soccer_links.pickle", "wb")
        pickle.dump(haha, pickle_out)
        pickle_out.close()
    for ligue in haha.keys():
        for yr in haha[ligue].keys():
            haha[ligue][yr] = [item for sublist in haha[ligue][yr] for item in sublist]
        haha[ligue]['2020-2021'] = haha[ligue]['']
        del haha[ligue]['']
    pickle_out = open(data_path + "soccer_links.pickle", "wb")
    pickle.dump(haha, pickle_out)
    pickle_out.close()
def find_index(df, a):
    try:
        wow = df[df['league'] == a['league']].copy()
        wow = wow[wow['date'] == pd.to_datetime(a['date'])]
        wow = wow[(wow['team1'] == a['fixed_team1']) | (wow['team1'] == a['fixed_team1']) | (wow['team2'] == a['fixed_team2']) | (wow['team2'] == a['fixed_team2'])]
        return wow[['league','date','team1','team2']]
    except:
        print(wow)
def gather_new_game_links():
    now = datetime.datetime.now()
    tmp_dict = {}
    for t in nation_league_mapper.keys():
        tmp_dict[t] = []
        for pg in range(1, 10):
            tmp_dict[t].append(get_games(t, '', pg)) # settings are page 1 and no year (current year)
            print(pg, ' done')
        try:
            tmp_dict[t] = [item for sublist in tmp_dict[t] for item in sublist]
        except:
            pass
        print(t, datetime.datetime.now() - today)
    output = pd.DataFrame(tmp_dict)
    print(output.to_string())
    file_name = now.date().strftime("%Y%m%d") + f"_{now.hour}"
    pickle_out = open(data_path + f"soccer_links_20201122_20.pickle", "wb")
    pickle.dump(tmp_dict, pickle_out)
    pickle_out.close()
    pickle_in = open(data_path + f"soccer_links_20201122_20.pickle", "rb")
    lol = pickle.load(pickle_in)
    pprint(lol)
    list_ting = []
    for key, each in lol.items():
        e = pd.DataFrame({'values': each})
        e['league'] = key
        list_ting.append(e)
    output = pd.concat(list_ting).reset_index(drop=True)
    print(output.to_string())
    output.to_sql("last_downloaded_soccer_links", local_engine, index=False, if_exists='replace')
def reduce_soccer_links_to_only_most_recent():
    ddf = pd.read_sql("select * from last_downloaded_soccer_links", local_engine)
    links = pd.read_sql("select link from current_season_odds", local_engine)
    rr = pd.DataFrame({'yes':pd.concat([ddf['values'], links['link']])})
    rr.drop_duplicates(keep=False, inplace=True)
    output = pd.merge(ddf, rr, left_on='values', right_on='yes', how='inner')[['values', 'league']]
    print(output.to_string())
    output.to_sql("most_recent_soccer_links", local_engine, index=False, if_exists='replace')
def update_soccer_betting():
    gather_new_game_links()
    reduce_soccer_links_to_only_most_recent()
    final_step()
def get_full_cut_df(data_,odf_, ligue, team_, domestic, season, win_prob_, min_odds, bet):
    data_ = feature_eng(data_, win_prob_)
    fdf= data_[(data_['league'] == ligue) & (data_['prob_win_tie'] >= win_prob_)].copy()
    if domestic == 'Domestic':
        fdf = fdf[fdf['league'] == ligue]
    elif domestic == 'Domestic + Europe':
        fdf = fdf[(fdf['league'] == ligue) | (fdf['league'] == "UEFA Champions League") | (fdf['league'] == "UEFA Europa League")]
    else:
        fdf = fdf[(fdf['league'] == "UEFA Champions League") | (fdf['league'] == "UEFA Europa League")]
    if team_ != 'All':
        fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
    fdf = fdf[(fdf['season'] >= season[0]) & (fdf['season'] <= season[1])].copy()
    fdf.dropna(inplace=True)
    full_data = add_odds_data_to_df(fdf, odf_, bet, min_odds)
    print(full_data.to_string())
    return full_data
def read_pickles_to_df(ligue):
    fun = []
    for i, t in enumerate([f"{ligue.lower().replace('-', '_').replace(' ', '_')}_{i.replace('-', '_').replace(' ', '_')}_season.pickle" for i in [f"{yr}-{yr + 1}" for yr in range(2016, 2025)][:5]]):
        # if i == 4:
        pickle_i = open(data_path + t, "rb")
        fun.append(pickle.load(pickle_i))
    return pd.concat(fun)
def add_odds_data_to_df(df, rdf, bet, min_odds_):
    output = pd.merge(df, rdf, left_on=['league', 'date', 'team1', 'team2'], right_on=['league', 'date', 'team1', 'team2'], how='inner')
    output = output.dropna().reset_index(drop=True)
    qq = []
    odd_list = []
    won = []
    for i in output.itertuples():
        if i.won_bet:
            won.append(True)
            if i.prob1_win_tie == i.prob_win_tie:
                qq.append((bet * float(i.avg_1X)))
                odd_list.append(float(i.avg_1X))
            else:
                qq.append((bet * float(i.avg_X2)))
                odd_list.append(float(i.avg_X2))
        else:
            qq.append(-1 * bet)
            won.append(False)
            if i.prob1_win_tie == i.prob_win_tie:
                odd_list.append(float(i.avg_1X))
            else:
                odd_list.append(float(i.avg_X2))
    data = pd.DataFrame({'per_bet': qq, 'odds': odd_list, 'won_bet': won,}, index=output.index)
    data = data[data['odds']>=min_odds_]
    data['cumsum'] = data['per_bet'].cumsum()
    kk = []
    for t in data.itertuples():
        try:
            if data.at[t.Index - 1, 'cumsum'] < 10:
                kk.append(t.cumsum - bet)
            else:
                kk.append(t.cumsum)
        except:
            kk.append(t.cumsum)
    data['sure'] = kk
    tt = [bet]
    for i in data.itertuples():
        if i.won_bet:
            if tt[-1] == 0:
                tt.append(i.odds * bet)
            elif tt[-1] < 0:
                tt.append(tt[-1] + (bet * i.odds))
            elif tt[-1] > 0:
                tt.append(tt[-1] * i.odds)
        else:
            if tt[-1] == 0:
                tt.append(-bet)
            elif tt[-1] > 0:
                tt.append(0)
            elif tt[-1] == -bet:
                tt.append(-2 * bet)
            else:
                tt.append(1000)
    data['yolo'] = tt[1:]
    data = data.drop(columns=['won_bet'])
    final = data.merge(output, left_index=True, right_index=True)
    final = final.drop(columns=['xg1', "xg2", "nsxg1", "nsxg2", "adj_score1", "adj_score2",])
    return final
def final_step():

    df = clean_df()
    most_recent = pd.read_sql("select * from most_recent_soccer_links", local_engine)
    skip = pd.read_sql("select * from links_to_skip", local_engine).iloc[:, 0].drop_duplicates().tolist()
    collect = []
    for i in tqdm(most_recent.itertuples()):
        if i.values not in skip:
            collect.append(get_odds_as_record(df, i.values, i.league))

    final = pd.concat(collect)
    print(final.to_string())
    final.to_sql('current_season_odds', local_engine, index=False, if_exists='append', )
    links_to_skip = pd.Series(outer)
    links_to_skip.to_sql("links_to_skip", local_engine, index=False, if_exists='append')
    print(datetime.datetime.now()-today)
path = os.getcwd().replace("\\", "/") + "/"
data_path = path + 'data/soccer_betting/'
today = datetime.datetime.now()
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

local_engine = sqlite3.connect(data_path + "sports_betting.db")
# local_engine = personal_db_engine('sports_betting')
# remote_engine = personal_db_engine('sports_betting')
outer = []
# engine = personal_db_engine()

# download latest data
# download_538_data()
# map league to country for URL
nation_league_mapper = {'bundesliga':'germany', 'premier league':'england', 'serie a':'italy', 'ligue 1':'france', 'europa league':'europe', 'champions league':'europe', 'laliga':'spain'}
# maps 538 league : oddsportal name
league_mapper = {'Barclays Premier League': 'premier league',"French Ligue 1": 'ligue 1', "Italy Serie A":"serie a",
                 "German Bundesliga":"bundesliga", "Spanish Primera Division":'laliga', 'UEFA Europa League': 'europa league', "UEFA Champions League":"champions league"}
# maps Oddsportal name : 538 name
team_name_mapper = {'Cadiz CF':'Cadiz','Atl. Madrid':'Atletico Madrid',"Huesca":"SD Huesca","Granada CF":"Granada","Ath Bilbao":"Athletic Bilbao", "Alavés":"Alaves","Alaves":"Alaves", "Betis":"Real Betis","Valladolid":"Real Valladolid",
                    'Sevilla':'Sevilla FC',

                    "Chievo":"Chievo Verona", "Inter":"Internazionale","Pescara":"US Pescara",

                    "Dijon":"Dijon FCO","Paris SG":"Paris Saint-Germain","Monaco":"AS Monaco","Rennes":"Stade Rennes","Nancy":"AS Nancy Lorraine",

                    "Dortmund":"Borussia Dortmund","Wolfsburg":"VfL Wolfsburg","Freiburg":"SC Freiburg","Darmstadt":"SV Darmstadt 98","Schalke":"Schalke 04","Ingolstadt":"FC Ingolstadt 04","Stuttgart":"VfB Stuttgart",
                    "B. Monchengladbach":"Borussia Monchengladbach","Hoffenheim":"TSG Hoffenheim","Augsburg":"FC Augsburg","Hamburger SV":"Hamburg SV","FC Koln":"FC Cologne","Hannover":"Hannover 96",
                    "Dusseldorf":"Fortuna Düsseldorf","Nurnberg":"1. FC Nürnberg","'Union Berlin":"1. FC Union Berlin","Paderborn":"SC Paderborn",


                    'Stoke':'Stoke City',"Huddersfield":"Huddersfield Town","Cardiff":"Cardiff City","Swansea":"Swansea City", "West Brom":"West Bromwich Albion", "Wolves":"Wolverhampton", "Manchester Utd": "Manchester United", "Leicester": "Leicester City", "Norwich":"Norwich City",
                    "Sheffield Utd": "Sheffield United", "West Ham":"West Ham United", "Tottenham":"Tottenham Hotspur", "Brighton":"Brighton and Hove Albion", "Bournemouth":"AFC Bournemouth"}

# read in 5 seasons (starting in 2016-2017) of URLS for each of the Top 5 leagues + Europa/UCL
years = [f"{a}-{a+1}" for a in range(2016, 2025)][:4]
print(today)




# pickle_in = open(data_path + "soccer_links.pickle","rb")
# data = pickle.load(pickle_in)
#
# win_prob = 0.70
#
# # read in 538 prediction data

# print(years)
# done = []
# current_year = ['2020-2021']
# for yrr in current_year:
#     for p in nation_league_mapper.keys():
#         pickle_in = open(data_path + f"{p.replace(' ', '_')}_{yrr.replace('-', '_')}_season.pickle", "rb")
#         tt = pickle.load(pickle_in)
#         done.append(tt)
# final = pd.concat(done).reset_index(drop=True)
# print(final)
# final.to_sql("current_season_odds", local_engine, if_exists='replace', index=False)
# print('done')
pass

# if __name__ == '__main__':
#     # Set-up
#     print(today)
#     cluster = LocalCluster(threads_per_worker=8,)
#     client = Client(cluster)


