import numpy as np
import pandas as pd
import os
from pprint import pprint
import itertools
from tqdm import tqdm

pd.options.mode.chained_assignment = None  # default='warn'

# setting up the game totals dataframe
game_output_df_template = pd.DataFrame({'a':range(1, 21+1)})
game_output_df_template['frame'] = (game_output_df_template['a']%2 + game_output_df_template['a'])/2
game_output_df_template['ball_in_frame'] = (game_output_df_template['a'] + 1)%2 + 1
game_output_df_template.drop(columns=['a'], inplace=True)
# last ball of the game, special case
game_output_df_template['frame'].iloc[max(game_output_df_template.index)] = 10
game_output_df_template['ball_in_frame'].iloc[max(game_output_df_template.index)] = 3

balls = {"PIN"+str(x): 1 for x in range(1,11)}
comb = itertools.combinations(balls.keys(), 2)

def create_game(game_output_df_template):
    ph = []
    for i in game_output_df_template.itertuples():
        if i.ball_in_frame == 1:
            z = np.random.randint(0,10)
            fun = list(itertools.combinations(balls.keys(), z))[0]
            ph.append(fun)
        elif i.ball_in_frame == 2:
            list_of_pins_left = [kk for kk in balls.keys() if kk not in ph[len(ph)-1]]
            z = np.random.randint(0, len(list_of_pins_left)+1)
            fun = list(itertools.combinations(list_of_pins_left, z))
            ph.append(fun[0])
        elif i.ball_in_frame == 3:
            last_ball = len(ph[len(ph)-1])
            last_last_ball = len(ph[len(ph)-2])
            if last_ball + last_last_ball == 10:
                z = np.random.randint(0, 10)
                fun = list(itertools.combinations(balls.keys(), z))[0]
                ph.append(fun)
            else:
                ph.append(tuple())

    game_output_df_template["pins_hit"] = ph
    game_output_df_template['ball_score'] = [len(i) for i in game_output_df_template['pins_hit']]
    return game_output_df_template
def find_marks(game_df):
    special_score = []
    for frame in sorted(game_df['frame'].unique()):
        tmp = game_df[game_df['frame'] == frame].copy()
        if tmp['ball_score'].sum() == 10:
            if tmp[tmp['ball_in_frame'] == 1]['ball_score'].sum() == 10:
                special_score.append('STRIKE')
                special_score.append('')
            else:
                special_score.append('')
                special_score.append('SPARE')
        else:
            special_score.append('')
            special_score.append('')
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

        if i.special == 'SPARE':
            game_df['added_score1'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+1]

        elif i.special == "STRIKE":
            try:
                game_df['added_score1'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+1]
            except:
                pass
            try:
                game_df['added_score2'].iloc[i.Index] = game_df['ball_score'].iloc[i.Index+2]
            except:
                pass
    game_df['total_ball_score'] = game_df['ball_score'] + game_df['added_score1'] + game_df['added_score2']
    game_df['running_score'] = game_df['total_ball_score'].cumsum()
    return game_df


num_games_to_simulate = 10000
games = {}
for rrr in tqdm(range(1, num_games_to_simulate+1)):
    zz = get_scores(find_marks(create_game(game_output_df_template))).copy()
    if rrr > 1:
        for k in list(games.keys()):
            if not zz['pins_hit'].equals(games[k]['pins_hit']):
                games[rrr] = zz
    else:
        games[rrr] = zz
print(len(games.keys()))

def find_best_game(games):
    best_score = 0
    index_of_best_game = 0
    for k,v in games.items():
        tmp = v["running_score"].max()
        if tmp > best_score:
            best_score = tmp
            index_of_best_game = k
    return index_of_best_game

print(games[find_best_game(games)])

