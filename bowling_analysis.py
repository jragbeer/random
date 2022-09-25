import numpy as np
import pandas as pd
import datetime
import os
from pprint import pprint
import itertools
from tqdm import tqdm
import logging
import pickle
import gc


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

# simulate game funcs
def create_game_template():
    # setting up the game totals dataframe
    game_output_df_template = pd.DataFrame({'a':range(1, 21+1)}) # max number of balls that can be thrown in 1 game
    game_output_df_template['frame'] = (game_output_df_template['a']%2 + game_output_df_template['a'])/2
    game_output_df_template['ball_in_frame'] = (game_output_df_template['a'] + 1)%2 + 1
    # last ball of the game, special case
    game_output_df_template['frame'].iloc[max(game_output_df_template.index)] = 10
    game_output_df_template['ball_in_frame'].iloc[max(game_output_df_template.index)] = 3
    game_output_df_template['frame'] = game_output_df_template['frame'].astype(int)
    return game_output_df_template.drop(columns=['a'])
def simulate_game(game_template_df):
    game_output_df_template = game_template_df.copy()
    # a list of the pins hit, each item in the list will be a Ball in a Frame
    ph = []
    for i in game_output_df_template.itertuples():
        # Frames 1-9 are similar cases
        # unique circumstances involving Frame 10: Ball 1 and Frame 10: Ball 2
        if i.ball_in_frame == 1:
            num_pins_down = np.random.randint(0,11)
            all_combos = list(itertools.combinations(balls.keys(), num_pins_down))
            # append the first out of the list of returned possible Balls in the Frame
            ph.append(all_combos[0])
        elif i.ball_in_frame == 2:
            # find which pins are hit and only look at the other ones
            list_of_pins_left = [kk for kk in balls.keys() if kk not in ph[len(ph)-1]]
            num_pins_down = np.random.randint(0, len(list_of_pins_left)+1)
            all_combos = list(itertools.combinations(list_of_pins_left, num_pins_down))
            # append the first out of the list of returned possible Balls in the Frame
            ph.append(all_combos[0])
        # Frame 10 is a unique case, 3 possbile balls in the frame
        if i.frame == 10:
            if i.ball_in_frame == 3:
                #  find the two most recent Balls in Frame 10
                last_ball = len(ph[len(ph)-1])
                last_last_ball = len(ph[len(ph)-2])
                #  find out if the third ball can be played (if a mark occurred in first two Balls)
                if last_ball + last_last_ball == 10:
                    num_pins_down = np.random.randint(0, 10)
                    all_combos = list(itertools.combinations(balls.keys(), num_pins_down))
                    ph.append(all_combos[0])
                # if no mark, last Ball can't be thrown
                else:
                    ph.append(tuple())

    game_output_df_template["pins_hit"] = ph
    game_output_df_template['ball_score'] = [len(i) for i in game_output_df_template['pins_hit']]
    return game_output_df_template.copy()
def find_marks(game_df):
    special_score = []
    for frame in sorted(game_df['frame'].unique()):
        tmp = game_df[game_df['frame'] == frame].copy()
        # special handling for the last ball of the game
        if frame == 10:
            # first ball of the frame
            if tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
            else:
                special_score.append('')
            # second ball of the frame
            if tmp[tmp['ball_in_frame'] == 2]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
            elif (tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() + tmp[tmp['ball_in_frame'] == 2]['ball_score'].sum() == 10):
                if (tmp[tmp['ball_in_frame'] == 2]['ball_score'].sum() != 10) and (tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() != 10):
                    special_score.append('SPARE')
                else:
                    special_score.append('')
            else:
                special_score.append('')
            # last ball of the frame
            if tmp[tmp['ball_in_frame'] == 3]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
            elif (tmp[tmp['ball_in_frame'] == 3]['ball_score'].sum() + tmp[tmp['ball_in_frame'] == 2][
                'ball_score'].sum() == 10):
                if tmp[tmp['ball_in_frame'] == 3]['ball_score'].sum() != 10 and (tmp[tmp['ball_in_frame'] == 2]['ball_score'].sum() +tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() != 10) :
                    special_score.append('SPARE')
                else:
                    special_score.append('')
            else:
                special_score.append('')
        else:

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

    game_df['special'] = special_score
    return game_df.copy()
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
                next_valid_ball_offset = 2
                game_df['added_score1'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+next_valid_ball_offset]
            except:
                pass
            try:
                next_next_valid_ball_offset = 3
                try:
                    if game_df['special'].iloc[i.Index + 2] == 'STRIKE':
                        next_next_valid_ball_offset = next_next_valid_ball_offset + 1
                except:
                    pass
                game_df['added_score2'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+next_next_valid_ball_offset]
            except:
                pass
    # calculate the ball by ball score and the total score
    game_df['total_ball_score'] = game_df['ball_score'] + game_df['added_score1'] + game_df['added_score2']
    game_df['running_score'] = game_df['total_ball_score'].cumsum()
    return game_df.copy()

# high-level functions to run
def first_attempt(game_template):
    first_game_ = get_scores(find_marks(simulate_game(game_template.copy()))).copy()
    games = {1: first_game_}

    for game_no in tqdm(range(2, num_games_to_simulate + 1)):
        each_game = get_scores(find_marks(simulate_game(game_template))).copy()
        for k in list(games.keys()):
            if not each_game['pins_hit'].equals(games[k]['pins_hit']):
                games[game_no] = each_game

    best_game, number_strikes, c = find_best_game(games)

    # log the info to a log file
    logging.info(f"Number of games simulated: {num_games_to_simulate}")
    logging.info(f"Number of unique games: {len(games.keys())}")
    logging.info(f"Number of games with a strike: {number_strikes}")
    logging.info(f"Compare Column: {compare_column}")
    logging.info("Best game: ")
    logging.info(f"\n{games[best_game]}")
def second_attempt(game_template):
    first_game = get_scores(find_marks(simulate_game(game_template.copy()))).copy()
    games_database = {1: first_game}
    games_by_score = {first_game['running_score'].max(): [1]}

    for game_no in tqdm(range(2, num_games_to_simulate + 1)):
        # run a simulation and find it's final score
        each_game = get_scores(find_marks(simulate_game(game_template))).copy()
        score = each_game['running_score'].max()
        # if the score is in the score dictionary
        if score in games_by_score.keys():
            # a list of games that all have the same score
            g_s = games_by_score[score]
            # iterate through each game
            for index, sub_each in enumerate(g_s):
                # find the latest game to compare current with
                compare_game = games_database[g_s[index]]
                counter = 0
                if not each_game[compare_column].equals(compare_game[compare_column]):
                    counter = counter + 1
                # if each_game is unique, then add it to the game database and score database
                if counter == len(g_s):
                    games_database[game_no] = each_game
                    g_s.append(game_no)
        # if the score is unique so far, simply add it to the dictionaries
        else:
            games_by_score[score] = [game_no]
            games_database[game_no] = each_game
    pprint(games_by_score)
    best_game, number_strikes, c = find_best_game(games_database)

    # save the simulations
    pickle_out = open("latest_bowling_games_dict.pickle", "wb")
    pickle.dump({"games": games_database, 'scores': games_by_score}, pickle_out)
    pickle_out.close()

    # log the info to a log file
    logging.info(f"Number of games simulated: {num_games_to_simulate}")
    logging.info(f"Number of unique games: {len(games_database.keys())}")
    logging.info(f"Number of games with a strike: {number_strikes}")
    logging.info(f"Compare Column: {compare_column}")
    logging.info("Best game: ")
    logging.info(f"\n{games_database[best_game]}")
def final_attempt():
    pairs = []
    first_ball_choices = list(range(11))
    for f in first_ball_choices:
        for z in first_ball_choices:
            if z + f <= 10:
                pairs.append((f,z))
    pprint(sorted(pairs))
    print(len(pairs))
    possible_gms = []
    spares = []
    strikes = []
    number_of_frames = 5
    for qq in range(1, number_of_frames):
        end = itertools.product(pairs, repeat = qq)
        solution = [x for x in end]
        print(qq)
        print(solution[0], solution[-2], solution[-1])
        print(len(solution))

        fine = sorted(solution)
        pprint(fine[:10])
        pprint(fine[-10:])
        possible_gms.append(len(solution))

        # counting how many spares/strikes in last ball of each frame
        stk = []
        spr = []
        for x in fine:
            if sum(x[-1]) == 10:
                spr.append(x)
                if x[-1][0] == 10:
                    stk.append(x)
        spares.append(len(spr))
        strikes.append(len(stk))
        print("________________________")
        gc.collect()
    ddf = pd.DataFrame({'possible_gms': possible_gms, "possible_last_frame_spares": spares, "possible_last_frame_strikes": strikes}, index = range(1,number_of_frames))

    ddf['spares_per_strike'] = ddf['possible_last_frame_spares'] / ddf['possible_last_frame_strikes']
    ddf['shifted'] = ddf['possible_gms'].shift()
    ddf['first_div'] = ddf['possible_gms'] / ddf['shifted']
    ddf['first_diff'] = ddf['possible_gms']-ddf['shifted']
    ddf['shifted2'] = ddf['first_diff'].shift()
    ddf['second_diff'] = ddf['first_diff'] - ddf['shifted2']

    ddf['extra_games_due_to_mark_at_end'] = (11*ddf['possible_last_frame_spares'])
    ddf['total_games_as_last_frame'] = ddf['possible_gms'] - ddf['possible_last_frame_spares'] + ddf['extra_games_due_to_mark_at_end']
    print(ddf)


# post-simulation stats funcs
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

# each pin for easier analysis, and it's # of points as the value
balls = {"PIN"+str(x): 1 for x in range(1,11)}
base_game_template = create_game_template()

# parameters for the simulation
num_games_to_simulate = 1000
compare_column = 'ball_score'
# compare_column = "pins_hit"

# first_attempt(base_game_template)
# second_attempt(base_game_template)
final_attempt()

end_time = datetime.datetime.now()
logging.info(end_time-today)
logging.info('*******')
pass