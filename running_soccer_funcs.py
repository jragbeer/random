from sports_betting_data_eng import *
import atexit
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(message)s', handlers=[logging.FileHandler(path + "log.txt"), logging.StreamHandler()])

# read in 538 prediction data
idata = clean_df()
idata.dropna(subset=['league'], inplace=True)
idata = idata.sort_values(['league', 'date', 'team1',])
bet = 10
win_prob = 0.75
data = feature_eng(idata, win_prob)

# odds data
odf = pd.concat([pd.read_sql('select * from historical_odds', local_engine, parse_dates=['date']),pd.read_sql('select * from current_season_odds', local_engine, parse_dates=['date'])])
odf.replace("-", np.nan, inplace=True)
odf.dropna(inplace=True)


make_data_tables(data,odf,  date1 = datetime.datetime(2016, 8,1), date2=datetime.datetime(2017, 8,1))
make_data_tables(data,odf, date1 = datetime.datetime(2017, 8,1), date2=datetime.datetime(2018, 8,1))
make_data_tables(data, odf,date1 = datetime.datetime(2018, 8,1), date2=datetime.datetime(2019, 8,1))
make_data_tables(data,odf, )


# update_soccer_betting()

# remote_engine = personal_db_engine('sports_betting')
# for each in ['links_to_skip', 'current_season_odds', 'historical_odds', 'most_recent_soccer_links', 'last_downloaded_soccer_links']:
#     new = pd.read_sql(f"select * from {each}", local_engine, )
#     new.to_sql(each, remote_engine, index=False, if_exists='replace')
#     print(each, ' done')

