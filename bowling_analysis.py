import pickle
import gc
import ray
from jragbeer_common import *




# pandas settings for setingwarning
pd.options.mode.chained_assignment = None  # default='warn'
# pandas settings for terminal output
pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
today = datetime.datetime.now()


load_dotenv(path + '.env')
secrets = dict(dotenv_values(path + ".env"))

# logger
dagster_logger = logging.getLogger("logger")
dagster_logger.setLevel(logging.INFO)
# create console handler
handler = logging.StreamHandler()
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s, %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
dagster_logger.addHandler(handler)
# create console handler
handler2 = logging.FileHandler(path + "bowling_analysis.log")
# add the handler to the logger
dagster_logger.addHandler(handler2)
dagster_logger.info(today)
# code version
app_version_number = "0.1"
dagster_logger.info(f"Version:  {app_version_number}")


# parameters for the simulation
num_games_to_simulate = 3000000

compare_column = 'ball_score'  # ball_score or pins_hit

# each pin for easier analysis, and it's # of points as the value
balls = {"PIN"+str(x): 1 for x in range(1, 11)}
base_games_by_score = {x:[] for x in range(301)}

# compare_column = "pins_hit"

# simulate game funcs


def create_game_template() -> pd.DataFrame:
    # setting up the game totals dataframe
    game_output_df_template = pd.DataFrame({'a':range(1, 22)}) # max number of balls that can be thrown in 1 game
    game_output_df_template['frame'] = (game_output_df_template['a']%2 + game_output_df_template['a'])/2
    game_output_df_template['ball_in_frame'] = (game_output_df_template['a'] + 1)%2 + 1
    # last ball of the game, special case
    game_output_df_template.loc[max(game_output_df_template.index), 'frame'] = 10
    game_output_df_template.loc[max(game_output_df_template.index), 'ball_in_frame'] = 3
    game_output_df_template['frame'] = game_output_df_template['frame'].astype(int)
    return game_output_df_template.drop(columns=['a'])
def simulate_game(game_template_df: pd.DataFrame) -> pd.DataFrame:
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
def find_marks(game_df: pd.DataFrame) -> pd.DataFrame:
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
def get_scores(game_df: pd.DataFrame) -> pd.DataFrame:
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
def first_attempt(game_template: pd.DataFrame, compare_column:str = compare_column, num_games_to_simulate:int = num_games_to_simulate) -> None:
    """
    This function simulates a bowling game and then compares it to the database (a dictionary) of already simulated
    games to ensure that the game is unique. The comparison involves checking each game in the database one-by-one
    against the most-recently simulated game. This way of checking means that the time it takes to check if a game is
    unique increases over time and is unfeasable for larger numbers. Some stats are logged at the end of the function.

    :param game_template: the starting template for a bowling game as a dataframe
    :param compare_column: the column to compare to check whether the games/dataframes are the same
    :param num_games_to_simulate: the number of bowling games to simulate
    :return: None
    """
    first_game_ = get_scores(find_marks(simulate_game(game_template.copy()))).copy()
    games = {1: first_game_}

    for game_no in tqdm(range(2, num_games_to_simulate + 1)):
        # run a simulation and find it's final score
        each_game = get_scores(find_marks(simulate_game(game_template))).copy()
        for k in list(games.keys()):
            # if the game is unique (by comparing game against every other game already simulated), add it to the game
            # dictionary
            if not each_game[compare_column].equals(games[k][compare_column]):
                games[game_no] = each_game
    # quickly find the best game, and how many games had a strike in them
    best_game, number_strikes, random_game_with_a_strike = find_best_game(games)

    # log the info to a log file
    logging.info(f"Number of games simulated: {num_games_to_simulate}")
    logging.info(f"Number of unique games: {len(games.keys())}")
    logging.info(f"Number of games with a strike: {number_strikes}")
    logging.info(f"Compare Column: {compare_column}")
    logging.info("Best game: ")
    logging.info(f"\n{games[best_game]}")
def second_attempt(game_template: pd.DataFrame, compare_column:str = compare_column, num_games_to_simulate:int = num_games_to_simulate) -> None:
    """
    This function simulates a bowling game and then compares it to the database (a dictionary) of already simulated
    games to ensure that the game is unique. The comparison involves using another dictionary **games_by_score**
    sort the already-simulated games by their score. **games_by_score** (keys is scores, values are a list of games with
    that score) is consulted and all games in the values list of that dictionary are checked against the most-recently
    simulated game for uniqueness. This results in the comparison process being much faster. Some stats are logged at
    the end of the function.

    :param game_template: the starting template for a bowling game as a dataframe
    :param compare_column: the column to compare to check whether the games/dataframes are the same
    :param num_games_to_simulate: the number of bowling games to simulate
    :return: None
    """
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
def third_attempt() -> None:
    pairs = []
    # all possible scores from a single throw of a ball
    first_ball_choices = list(range(11))
    for first_ball in first_ball_choices:
        for second_ball in first_ball_choices:
            # max score in a frame is 10
            if second_ball + first_ball <= 10:
                # add each possible frame to the list of all possible frame scores
                pairs.append((first_ball,second_ball))
    pprint(sorted(pairs))
    print(len(pairs))
    possible_gms = []
    spares = []
    strikes = []
    # number_of_frames is how deep the tree is
    number_of_frames = 5
    for each_frame in range(1, number_of_frames):
        end = itertools.product(pairs, repeat = each_frame)
        solution = [x for x in end]
        print(each_frame)
        print(solution[0], solution[-2], solution[-1])
        print(len(solution))

        gms = sorted(solution)
        pprint(gms[:10])
        pprint(gms[-10:])
        possible_gms.append(len(solution))

        # counting how many spares/strikes in last ball of each frame
        stk = []
        spr = []
        for x in gms:
            # if at least a spare in the last frame
            if sum(x[-1]) == 10:
                spr.append(x)
                # if there's a strike in the last frame
                if x[-1][0] == 10:
                    stk.append(x)
        spares.append(len(spr))
        strikes.append(len(stk))
        gc.collect()
        print("________________________")
    # create a dataframe to see the stats
    ddf = pd.DataFrame({'possible_gms': possible_gms,
                        "possible_last_frame_strikes": strikes,
                        "possible_last_frame_spares": spares, },
                       index = range(1,number_of_frames))

    ddf['spares_per_strike'] = ddf['possible_last_frame_spares'] / ddf['possible_last_frame_strikes']
    ddf['shifted'] = ddf['possible_gms'].shift()
    ddf['first_div'] = ddf['possible_gms'] / ddf['shifted']
    ddf['first_diff'] = ddf['possible_gms']-ddf['shifted']
    ddf['shifted2'] = ddf['first_diff'].shift()
    ddf['second_diff'] = ddf['first_diff'] - ddf['shifted2']

    ddf['extra_games_due_to_mark_at_end'] = (11*ddf['possible_last_frame_spares'])
    ddf['total_games_as_last_frame'] = ddf['possible_gms'] - ddf['possible_last_frame_spares'] + ddf['extra_games_due_to_mark_at_end']
    print(ddf)
def fourth_attempt():
    kdf = pd.DataFrame({'possible_gms': [66**n for n in range(1, 11)]}, index = range(1,11))
    kdf['possible_last_frame_strikes'] = kdf['possible_gms'].shift()
    kdf["possible_last_frame_strikes"].iloc[0] = 1
    kdf["possible_last_frame_spares"] = kdf['possible_last_frame_strikes'] * 11
    kdf['extra_games_due_to_mark_at_end'] = kdf["possible_last_frame_spares"] * 11
    kdf['total_games_as_last_frame'] = kdf['possible_gms'] - kdf['possible_last_frame_spares'] + kdf['extra_games_due_to_mark_at_end']
    for x in kdf.columns:
        kdf[x] = pd.to_numeric(kdf[x], downcast="integer")
    # 4.18 quintillion games possible
    print(kdf)

def simulate_multiple_games(games_by_score: dict,
                  game_template: pd.DataFrame,
                  compare_column:str = compare_column,
                  num_games_to_simulate:int = num_games_to_simulate,
                            ) -> tuple:
    num_games_simulate = range(1, num_games_to_simulate + 1)
    games_database = {x: pd.DataFrame() for x in num_games_simulate}

    for game_no in range(1, num_games_to_simulate + 1):
        # run a simulation and find it's final score
        each_game = get_scores(find_marks(simulate_game(game_template))).copy()
        each_game_max_score = each_game['running_score'].max()
        games_database[game_no] = each_game
        g_s = games_by_score[each_game_max_score]
        g_s.append(game_no)
        # iterate through each game
        for index, sub_each in enumerate(g_s):
            try:
                # find the latest game to compare current with
                compare_game = games_database[g_s[index]]
                counter = 0
                if not each_game[compare_column].equals(compare_game[compare_column]):
                    counter = counter + 1
                # if each_game is unique, then add it to the game database and score database
                if counter == len(g_s):
                    games_database[game_no] = each_game
                    g_s.append(game_no)
            except Exception as eee:
                pass
    return games_database, games_by_score

@ray.remote(num_gpus = max(0.001,1/num_games_to_simulate))
def ray_simulate_multiple_games(games_by_score: dict,
                  game_template: pd.DataFrame,
                  compare_column:str = compare_column,
                  num_games_to_simulate:int = num_games_to_simulate,
                            ) -> tuple:
    num_games_simulate = range(1, num_games_to_simulate + 1)
    games_database = {x: pd.DataFrame() for x in num_games_simulate}

    for game_no in range(1, num_games_to_simulate + 1):
        # run a simulation and find it's final score
        each_game = get_scores(find_marks(simulate_game(game_template))).copy()
        each_game_max_score = each_game['running_score'].max()
        games_database[game_no] = each_game
        g_s = games_by_score[each_game_max_score]
        g_s.append(game_no)
        # iterate through each game
        for index, sub_each in enumerate(g_s):
            try:
                # find the latest game to compare current with
                compare_game = games_database[g_s[index]]
                counter = 0
                if not each_game[compare_column].equals(compare_game[compare_column]):
                    counter = counter + 1
                # if each_game is unique, then add it to the game database and score database
                if counter == len(g_s):
                    games_database[game_no] = each_game
                    g_s.append(game_no)
            except Exception as eee:
                pass
    return games_database, games_by_score

def ray_attempt(num_splits = 100):

    ray.init(_node_ip_address="192.168.2.13")

    input_list = list(range(num_games_to_simulate))
    # Calculate the size of each split
    split_size = len(input_list) // num_splits
    split_size = max(1, split_size)

    print(f'Doing {num_splits} batches')
    delayed_results = []
    for _ in range(num_splits):
        delayed_results.append(ray_simulate_multiple_games.remote(games_by_score=base_games_by_score,
                                                          game_template=base_game_template,
                                                          compare_column=compare_column,
                                                          num_games_to_simulate=split_size, )
        )
    output = ray.get(delayed_results)

    gdb_list = []
    scores_list = []
    for x in output:
        gdb_list.append(x[0])
        scores_list.append(x[1])
    new_games_database = {}
    ran_num = 0
    for i, game_batch in enumerate(gdb_list):
        game_batch = {k + ran_num: v for k, v in game_batch.items()}
        new_games_database.update(game_batch)
        ran_num = ran_num + len(game_batch)
    # pprint(new_games_database)
    best_game_id, number_strikes, a_game_with_a_strike = find_best_game(new_games_database)

    # log the info to a log file
    dagster_logger.info(f"Number of games simulated: {num_games_to_simulate}")
    dagster_logger.info(f"Number of unique games: {len(new_games_database.keys())}")
    dagster_logger.info(f"Number of games with a strike: {number_strikes}")
    dagster_logger.info(f"Compare Column: {compare_column}")
    dagster_logger.info("Best game: ")
    dagster_logger.info(f"\n{new_games_database[best_game_id]}")
    dagster_logger.info(f"{datetime.datetime.now()-today}")
def dask_attempt(num_splits = 1000, parallel = 'distributed'):
    if __name__ == '__main__':
        input_list = list(range(num_games_to_simulate))
        # Calculate the size of each split
        split_size = len(input_list) // num_splits
        split_size = max(1, split_size)

        # Create the splits using Dask
        dagster_logger.info(f"{num_splits} splits each of around {split_size} size made. {len(input_list)} in total.")

        if parallel == 'distributed':
            with sqlalchemy.create_engine(os.getenv('home_connection_string')).begin() as conn:
                running_cluster_location = pd.read_sql("""SELECT var, value FROM
                 environment_variables WHERE
                 var = 'distributed_dask_cluster'""", conn)['value'].values[0]
                client = dask.distributed.get_client(running_cluster_location)
            dagster_logger.info(str(running_cluster_location))
            dagster_logger.info(f"Using Distributed Dask Cluster : {str(client)}")

        elif parallel == 'local':
            from dask.distributed import Client, LocalCluster
            client = LocalCluster(n_workers=8, threads_per_worker=1).get_client()  # set up local cluster on your laptop
            dagster_logger.info(f"Using Local Dask Cluster : {str(client)}")
        elif parallel == 'local_gpu':
            from dask_cuda import LocalCUDACluster
            from dask.distributed import Client
            cluster = LocalCUDACluster()
            client = Client(cluster)
            dagster_logger.info(f"Using Local GPU Dask Cluster : {str(client)}")

        # Create Dask delayed objects for each split and apply the provided function
        delayed_results = []
        for split in range(num_splits):
            delayed_results.append(
                dask.delayed(simulate_multiple_games)(games_by_score= base_games_by_score,
                          game_template= base_game_template,
                          compare_column= compare_column,
                          num_games_to_simulate= split_size,)
            )

        # Compute the results using Dask's parallel processing capabilities
        output = dask.compute(*delayed_results, priority=1, )

        # save the simulations
        pickle_out = open("new_bowling_output.pickle", "wb")
        pickle.dump(output, pickle_out)
        pickle_out.close()

        gdb_list = []
        scores_list = []
        for x in output:
            gdb_list.append(x[0])
            scores_list.append(x[1])
        new_games_database = {}
        ran_num = 0
        for i, game_batch in enumerate(gdb_list):
            game_batch = {k + ran_num: v for k, v in game_batch.items()}
            new_games_database.update(game_batch)
            ran_num = ran_num + len(game_batch)
        # pprint(new_games_database)
        best_game_id, number_strikes, a_game_with_a_strike = find_best_game(new_games_database)

        # log the info to a log file
        dagster_logger.info(f"Number of games simulated: {num_games_to_simulate}")
        dagster_logger.info(f"Number of unique games: {len(new_games_database.keys())}")
        dagster_logger.info(f"Number of games with a strike: {number_strikes}")
        dagster_logger.info(f"Compare Column: {compare_column}")
        dagster_logger.info("Best game: ")
        dagster_logger.info(f"\n{new_games_database[best_game_id]}")
        dagster_logger.info(f"{datetime.datetime.now()-today}")

# post-simulation stats funcs
def find_best_game(games: dict) -> tuple[int, int, int]:
    best_score = 0
    index_of_best_game = 0
    number_of_games_with_strike = 0
    game_with_a_strike = None
    for k,v in games.items():
        if not v.empty:
            tmp = v["running_score"].max()
            if tmp > best_score:
                best_score = tmp
                index_of_best_game = k
            if 'STRIKE' in [pp for pp in v['special'].tolist()]:
                number_of_games_with_strike = number_of_games_with_strike + 1
                game_with_a_strike = k
    return index_of_best_game, number_of_games_with_strike, game_with_a_strike



# kill_and_redeploy_dask_home_setup()
#
# move_secrets_to_remote_env(os.getenv('cluster_server_1_address'),
#                            os.getenv('cluster_server_1_username'),
#                            os.getenv('cluster_server_1_password'),
#                            )
#
# move_secrets_to_remote_env(os.getenv('cluster_server_2_address'),
#                            os.getenv('cluster_server_2_username'),
#                            os.getenv('cluster_server_2_password'),
#                            )


base_game_template = create_game_template()
# ray_attempt()
dask_attempt(num_splits=100, parallel='distributed')
# dask_attempt(num_splits=1000, parallel='local')


end_time = datetime.datetime.now()
logging.info(end_time-today)
logging.info('*******')
