import numpy as np
import pandas as pd
import datetime
import os
from pprint import pprint
import itertools
from tqdm import tqdm
import logging
import pickle



# pandas settings for setingwarning
pd.options.mode.chained_assignment = None  # default='warn'
# pandas settings for terminal output
pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

# comment / uncomment StreamHandler() to see logging information in the terminal during execution
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s, %(message)s",
    handlers=[
        logging.FileHandler("bowling_analysis.log"),
        logging.StreamHandler(),
    ],
)

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
today = datetime.datetime.now()
logging.info(today)
# code version
app_version_number = "0.1"
logging.info(f"Version:  {app_version_number}")

def create_game(game_output_df_template):
    ph = []
    for i in game_output_df_template.itertuples():
        if i.ball_in_frame == 1:
            num_pins_down = np.random.randint(0,11)
            all_combos = list(itertools.combinations(balls.keys(), num_pins_down))
            ph.append(all_combos[0])
        elif i.ball_in_frame == 2:
            list_of_pins_left = [kk for kk in balls.keys() if kk not in ph[len(ph)-1]]
            num_pins_down = np.random.randint(0, len(list_of_pins_left)+1)
            all_combos = list(itertools.combinations(list_of_pins_left, num_pins_down))
            ph.append(all_combos[0])
        elif i.ball_in_frame == 3:
            last_ball = len(ph[len(ph)-1])
            last_last_ball = len(ph[len(ph)-2])
            if last_ball + last_last_ball == 10:
                num_pins_down = np.random.randint(0, 10)
                all_combos = list(itertools.combinations(balls.keys(), num_pins_down))
                ph.append(all_combos[0])
            else:
                ph.append(tuple())

    game_output_df_template["pins_hit"] = ph
    game_output_df_template['ball_score'] = [len(i) for i in game_output_df_template['pins_hit']]
    return game_output_df_template
def find_marks(game_df):
    special_score = []
    for frame in sorted(game_df['frame'].unique()):
        tmp = game_df[game_df['frame'] == frame].copy()
        # if the score == 10 aka a MARK
        if tmp['ball_score'].sum() == 10:
            # of the first ball == 10 aka a STRIKE
            if tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
                special_score.append('')
            elif tmp[tmp['ball_in_frame'] <= 2]['ball_score'].sum() == 10:
                # if not just the first ball, it's a SPARE
                special_score.append('')
                special_score.append('SPARE')
        else:
            special_score.append('')
            special_score.append('')
        # special handling for the last ball of the game
        if frame == 10:
            if tmp[tmp['ball_in_frame'] == 3]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
            else:
                special_score.append('')

    game_df['special'] = special_score
    return game_df
def get_scores(game_df):
    game_df['added_score1'] = 0
    game_df['added_score2'] = 0
    for i in game_df.itertuples():
        # if it's a spare, get the next ball and add it to the added_score1 column
        if i.special == 'SPARE':
            game_df['added_score1'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+1]
        # if it's a strike, get the next ball and add it to the added_score1 column and add the next ball to
        # added_score2 column, handling for if there isn't a next score at later points in the game
        elif i.special == "STRIKE":
            try:
                game_df['added_score1'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+1]
            except:
                pass
            try:
                game_df['added_score2'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+2]
            except:
                pass
    # calculate the ball by ball score and the total score
    game_df['total_ball_score'] = game_df['ball_score'] + game_df['added_score1'] + game_df['added_score2']
    game_df['running_score'] = game_df['total_ball_score'].cumsum()
    return game_df
def find_best_game(games):
    best_score = 0
    index_of_best_game = 0
    number_of_games_with_strike = 0
    game_with_a_strike = None
    for k,v in games.items():
        tmp = v["running_score"].max()
        if tmp > best_score:
            best_score = tmp
            index_of_best_game = k
        if 'STRIKE' in [pp for pp in v['special'].tolist()]:
            number_of_games_with_strike = number_of_games_with_strike + 1
            game_with_a_strike = k
    return index_of_best_game, number_of_games_with_strike, game_with_a_strike
def create_game_template():
    # setting up the game totals dataframe
    game_output_df_template = pd.DataFrame({'a':range(1, 21+1)}) # max number of balls that can be thrown in 1 game
    game_output_df_template['frame'] = (game_output_df_template['a']%2 + game_output_df_template['a'])/2
    game_output_df_template['ball_in_frame'] = (game_output_df_template['a'] + 1)%2 + 1
    # last ball of the game, special case
    game_output_df_template['frame'].iloc[max(game_output_df_template.index)] = 10
    game_output_df_template['ball_in_frame'].iloc[max(game_output_df_template.index)] = 3
    return game_output_df_template.drop(columns=['a'])



# each pin for easier analysis, and it's # of points as the value
balls = {"PIN"+str(x): 1 for x in range(1,11)}

game_template = create_game_template()
num_games_to_simulate = 1000

games = {1: get_scores(find_marks(create_game(game_template))).copy()}

for game_no in tqdm(range(2, num_games_to_simulate+1)):
    each_game = get_scores(find_marks(create_game(game_template))).copy()
    for k in list(games.keys()):
        if not each_game['pins_hit'].equals(games[k]['pins_hit']):
            games[game_no] = each_game

best_game,number_strikes, c = find_best_game(games)

# save the simulations
pickle_out = open("latest_bowling_games_dict.pickle","wb")
pickle.dump(games, pickle_out)
pickle_out.close()

# log the info to a log file
logging.info(f"Number of games simulated: {num_games_to_simulate}")
logging.info(f"Number of unique games: {len(games.keys())}")
logging.info(f"Number of games with a strike: {number_strikes}")
logging.info("Best game: ")
logging.info(f"\n{games[best_game]}")

end_time = datetime.datetime.now()
logging.info(end_time-today)
logging.info('*******')
