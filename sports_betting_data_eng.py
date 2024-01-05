import pickle
from dateutil import parser
import calendar
import pymongo
from dotenv import load_dotenv
from jragbeer_common import *

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")+ "/"
data_path = path + 'data/'
today = datetime.datetime.today()

load_dotenv(path + '.env')
secrets = dict(dotenv_values(path + ".env"))

# logger
dagster_logger = logging.getLogger("dagster_logger")
dagster_logger.setLevel(logging.INFO)
# create console handler
handler = logging.StreamHandler()
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s, %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
dagster_logger.addHandler(handler)
# create console handler
handler2 = logging.FileHandler(path + "dagster_logger.log")
# add the handler to the logger
dagster_logger.addHandler(handler2)

# Pyarrow Strings (should be faster)
pd.options.future.infer_string = True
pd.options.mode.string_storage = "pyarrow"


# Polars settings
pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_rows(100)
pl.Config.set_fmt_str_lengths(1000)
pl.Config.set_tbl_dataframe_shape_below(True)
pl.Config.set_tbl_width_chars(1000)

# Azure BLOB Storage
adls_container_name = os.getenv("adls_container_name")
adls_connection_string = os.getenv("adls_connection_string")
adls_blob_account_endpoint = os.getenv("adls_blob_account_endpoint")

# MYSQL Connection Strings
sports_betting_connection_string = f"mysql+pymysql://{os.getenv('local_db_username')}:{os.getenv('local_db_password')}@{os.getenv('local_db_address')}:{os.getenv('local_db_port')}/sports_betting"

# Local MongoDB
mongo_client = pymongo.MongoClient('localhost', 27017)
mongo_db = mongo_client['sports_betting']


# map league to country for URL
nation_league_mapper = {'bundesliga':'germany',
                        'premier league':'england',
                        'serie a':'italy',
                        'ligue 1':'france',
                        'europa league':'europe',
                        'champions league':'europe',
                        'laliga':'spain',
                        }
# maps 538 league : oddsportal name
league_mapper = {'Barclays Premier League': 'premier league',
                 "French Ligue 1": 'ligue 1',
                 "Italy Serie A":"serie a",
                 "German Bundesliga":"bundesliga",
                 "Spanish Primera Division":'laliga',
                 'UEFA Europa League': 'europa league',
                 "UEFA Champions League":"champions league",
                 }
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

# 538 league number mapping
number_league_name_538_mapper = {2411:'premier league',
 1869:'serie a',
 1843:'laliga',
 1845:'ligue 1',
 1854:'bundesliga',
 1818:'europa league',
 1820:'champions league',
 }
# read in 5 seasons (starting in 2016-2017) of URLS for each of the Top 5 leagues + Europa/UCL
years = [f"{a}-{a+1}" for a in range(2016, 2025)][:4]

spi_match_538_link = "https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv"


def pull_538_data(parquet:bool=True, sql:bool=True) -> pd.DataFrame:
    ddf = pd.read_csv(spi_match_538_link)
    ddf = ddf[ddf['league_id'].isin(number_league_name_538_mapper.keys())]
    ddf['query_date'] = str(today.date())
    if parquet:
        file_name = today.date().strftime("%Y%m%d") + f"_{today.hour}"
        ddf.to_parquet(data_path + f"/538_data_historical/538_data_{file_name}.parquet")
        ddf.to_parquet(data_path + f"latest_538_data.parquet")
    if sql:
        sql_engine = sqlalchemy.create_engine(sports_betting_connection_string)
        ddf.to_sql("538_data_latest", sql_engine, if_exists='replace', index=False)
        ddf.to_sql("538_data", sql_engine, if_exists='append', index=False)
    return ddf
def get_clean_538_prediction_data()-> pd.DataFrame:
    """
    This function returns the 538 prediction data from the local parquet file.

    """
    odf = pd.read_parquet(data_path + "soccer_betting/latest_538_data.parquet", )
    odf['date'] = pd.to_datetime(odf['date'])
    odf['league'] = odf['league'].map(league_mapper)
    odf = odf.drop(columns = ['league_id', "importance1", "importance2"], ).sort_values("date")
    return odf


def feature_eng(input_df: pd.DataFrame, win_prob:float = 0.75)-> pd.DataFrame:
    input_df['prob1_win_tie'] = input_df['prob1'] + input_df['probtie']
    input_df['team1_win_tie'] = [i.score1 >= i.score2 for i in input_df.itertuples()]
    input_df['prob2_win_tie'] = input_df['prob2'] + input_df['probtie']
    input_df['team2_win_tie'] = [i.score1 <= i.score2 for i in input_df.itertuples()]
    k = []
    win = []
    for i in input_df.itertuples():
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
    input_df['won_bet'] = k
    input_df['game_winner'] = win
    input_df['prob_win_tie'] = input_df[["prob1_win_tie", "prob2_win_tie"]].max(axis=1)
    return input_df

def get_odds_as_record(df_, link, league):
    outer = []
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
            logging.info("THIS MEANS NO TEAMS MATCH")
            outer.append(link)
            raise Exception
        return output
    except:
        logging.info(error_handling())
        logging.info(a)
        logging.info(' ')
        return pd.DataFrame()
def get_games(league, szn, page):
    try:
        if szn != '':
            szn_ = '-' + str(szn)
        else:
            szn_ = szn
        country = nation_league_mapper[league]
        url = f"https://www.oddsportal.com/football/{country}/{league.replace(' ', '-')}{szn_}/results/#/page/{page}/"
        driver = get_selenium_driver(browser="chrome", dat_path='/home/jay/PycharmProjects/home/data/')
        soup = grab_soup(url, driver=driver)
        links = soup.find_all('div', {'class': 'eventRow flex w-full flex-col text-xs'})
        hrefs = [x.find('a',href=True)['href'] for x in links]
        # make sure that there's a full link and not smaller, useless links
        hrefs = [x for x in hrefs if len(x) > 20]
        print(hrefs)
        return hrefs
    except:
        logging.info(error_handling())
        logging.info('No Data')
        logging.info(url)
        return []
def get_odds_of_game(url, league):
    def inner_func(url, league):
        url = "https://www.oddsportal.com" + url + "#double;2"
        soup, driver = grab_soup(url, browser="chrome", dat_path=data_path)
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
        logging.info(f"{URL} is parsed")
        return {'odds':df.set_index("Bookmakers", drop=True), 'game':game, 'date':event_date, 'league':league, 'team1': t1,'team2': t2, "fixed_team2": odds_team2, "fixed_team1": odds_team1, 'url':url}
    for z in range(1,6):
        try:
            return inner_func(url, league)
        except:
            logging.info(f'No Data (attempt {z})')
            logging.info(url)
            logging.info(error_handling())
    return []


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
def get_full_cut_df(data_,odf_, ligue, team_, domestic, season, win_prob_, min_odds, bet):
    data_ = feature_eng(data_, win_prob_)
    fdf = data_[data_['prob_win_tie'] >= win_prob_].copy()
    fdf = fdf[(fdf['date'] >= convert_unix_timestamp_to_pandas_date(season[0])) & (fdf['date'] <= convert_unix_timestamp_to_pandas_date(season[1]))].copy()
    if ligue != 'all':
        list_of_all_teams = list(data_[data_['league'] == ligue]['team1'].unique())
    else:
        list_of_all_teams = data_['team1'].unique().tolist()
    if domestic == 'Domestic':
        if ligue != 'all':
            fdf = fdf[fdf['league'] == ligue]
        else:
            fdf = fdf
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            fdf = fdf[fdf['team1'].isin(list_of_all_teams) | (fdf['team2'].isin(list_of_all_teams))]
    elif domestic == 'Domestic + Europe':
        if ligue != "all":
            fdf = fdf[(fdf['league'] == ligue) | (fdf['league'] == "champions league") | (fdf['league'] == "europa league")]
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            if ligue != "all":
                list_of_all_teams = list(data[data['league'] == ligue]['team1'].unique())
            else:
                list_of_all_teams = list(data['team1'].unique())
            fdf = fdf[(fdf['team1'].isin(list_of_all_teams)) | (fdf['team2'].isin(list_of_all_teams))]
    else:
        fdf = fdf[(fdf['league'] == "champions league") | (fdf['league'] == "europa league")]
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            fdf = fdf[fdf['team1'].isin(list_of_all_teams) | (fdf['team2'].isin(list_of_all_teams))]
    fdf.dropna(inplace=True)
    full_data = add_odds_data_to_df(fdf, odf_, bet, min_odds).sort_values('date')
    # print(full_data.to_string())
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
    # np.where --- if (first arg) then (second arg) else (third arg)
    final['actual_per_game_return'] = np.where(final['per_bet'] < 0, final['per_bet'], final['per_bet'] - bet)
    final['cumsum'] = final['actual_per_game_return'].cumsum()
    final = final.drop(columns=['xg1', "xg2", "nsxg1", "nsxg2", "adj_score1", "adj_score2",])
    return final
def update_soccer_betting():
    pull_new_game_links()
    reduce_soccer_links_to_only_most_recent()
    final_step()
def pull_new_game_links():
    now = datetime.datetime.now()
    tmp_dict = {}
    # for each league, get a flat list of recent game links
    for liga in nation_league_mapper.keys():
        # settings are page 1 and no year (current year)
        tmp_dict[liga] = [get_games(league=liga, szn='', page=1)]
        try:
            tmp_dict[liga] = [item for sublist in tmp_dict[liga] for item in sublist]
        except:
            pass
        logging.info(f"{liga}, {datetime.datetime.now() - today}")

    file_name = now.date().strftime("%Y%m%d") + f"_{now.hour}"
    pickle_out = open(data_path + f"soccer_links_{file_name}.pickle", "wb")
    pickle.dump(tmp_dict, pickle_out)
    pickle_out.close()
    pprint(tmp_dict)
    list_ting = []
    for key, each in tmp_dict.items():
        e = pd.DataFrame({'values': each})
        e['league'] = key
        list_ting.append(e)
    output = pd.concat(list_ting).reset_index(drop=True)
    sql_engine = sqlalchemy.create_engine(sports_betting_connection_string)
    output.to_sql("last_downloaded_soccer_links", sql_engine, index=False, if_exists='replace')
    logging.info('latest_download_soccer_links table updated!') # all links, whether already parsed or not
def reduce_soccer_links_to_only_most_recent():
    ddf = pd.read_sql("select * from last_downloaded_soccer_links", local_engine) # get all links from latest batch of available links
    links = pd.read_sql("select link from current_season_odds", local_engine) # get links that have already been parsed
    stacked_dfs = pd.DataFrame({'yes':pd.concat([ddf['values'], links['link']])})
    stacked_dfs.drop_duplicates(keep=False, inplace=True) # only links that haven't been used remain
    output = pd.merge(ddf, stacked_dfs, left_on='values', right_on='yes', how='inner')[['values', 'league']]
    output.to_sql("most_recent_soccer_links", local_engine, index=False, if_exists='replace') # links to visit and download from
    logging.info('most_recent_soccer_links table updated!') # only links that haven't been parsed
def final_step():
    df = clean_df()
    most_recent = pd.read_sql("select * from most_recent_soccer_links", local_engine) # links to visit
    skip = pd.read_sql("select * from links_to_skip", local_engine).iloc[:, 0].drop_duplicates().tolist() # links that may be in *most_recent* that shouldn't be visited
    collect = [get_odds_as_record(df, i.values, i.league) for i in most_recent.itertuples() if i.values not in skip] # get the odds
    final = pd.concat(collect)
    final.to_sql('current_season_odds', local_engine, index=False, if_exists='append', ) # add odds data to current season odds
    links_to_skip = pd.Series(outer)
    links_to_skip.to_sql("links_to_skip", local_engine, index=False, if_exists='append')
    logging.info(datetime.datetime.now()-today)

def find_total_return(data_, bet_):
    ret = (data_['actual_per_game_return']+bet_).sum() - bet_ * len(data_.index)
    return ret
def datetime_to_timestamp(dt):
    """Converts a datetime object to UTC timestamp

    naive datetime will be considered UTC.

    """
    return calendar.timegm(dt.utctimetuple())
def get_season_results(data, odf, date1 = datetime.datetime(2019, 8,1), date2=datetime.datetime(2020, 8,1), league = 'premier league', bet=10, win_prob=0.75):
    first = datetime_to_timestamp(date1)*1000
    second = datetime_to_timestamp(date2)*1000
    results = {}
    wow = data[(data['league']== league) & (data['date'] >= convert_unix_timestamp_to_pandas_date(first)) & (data['date'] <= convert_unix_timestamp_to_pandas_date(second))]
    for team in wow['team1'].unique():
        data_ = get_full_cut_df(data, odf, league, team, 'Domestic', (first, second), win_prob, 1.01, bet)
        results[team] = find_total_return(data_, bet)
    qq = [i for i in results.values() if i > 0]
    return len(qq), len(results), len(qq)/len(results), sum(results.values())/len(results), results
def make_data_tables(data,odf, date1 = datetime.datetime(2019, 8,1), date2=datetime.datetime(2020, 8,1)):
    w = []
    for each in nation_league_mapper.keys():
        try:
            a, b, c, d, _ = get_season_results(data,odf, date1, date2, league=each)
            w.append({'League':' '.join([i.capitalize() for i in each.split()]), 'Teams with (+) Return':a,'Total Teams':b,'Percentage (%)':c*100, 'Average Return ($)': np.round(d, 2)})
        except:
            pass
    print(pd.DataFrame(w))
    # print(pd.DataFrame(w).to_html(index = False))
    print()
    print()
