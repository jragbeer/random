import numpy as np
import pandas as pd
import urllib
import sqlite3
import datetime
import sys
import pickle
import holidays
import copy
from pprint import pprint
import itertools
import cProfile
import numpy as np
import io
import pstats
import datetime
import dask
from dask.distributed import Client, progress
import dask.array as da
from tqdm import tqdm
import gc

if __name__ == '__main__':

    def profile(fnc):
        """A decorator that uses cProfile to profile a function"""

        def inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            retval = fnc(*args, **kwargs)
            pr.disable()
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
            return retval

        return inner

    # client = Client(threads_per_worker=8, n_workers=1)
    # client.restart()

    @profile
    def main():

        true = []

        timee = datetime.datetime.now()
        print(timee)

        print(datetime.datetime.now()-timee)
        df_one = {}

        pu_do_data = {"Pick-Up": {}, "Drop-Off": {}}
        for colr in ['yellow', 'green', "fhv", "all", ]:
            pickle_in = open("pulocationid_{}_full.pickle".format(colr),"rb")
            pu_data = pickle.load(pickle_in)
            pickle_in = open("dolocationid_{}_full.pickle".format(colr),"rb")
            do_data = pickle.load(pickle_in)
            pu_data.columns = ['value']
            do_data.columns = ['value']
            pu_do_data['Pick-Up'][str(colr)] = pu_data
            pu_do_data['Drop-Off'][str(colr)] = do_data

        # @dask.delayed
        def transform(data_frame, each, tipo, yr, hr, mth, day, hlday, ):
            rrtt = data_frame[tipo].copy()
            if yr != 'all':
                rrtt = rrtt[rrtt['year'] == yr]
            else:
                pass
            if hr != 'all' and each == 'pulocationid':
                rrtt = rrtt[rrtt['pickup_hour'] == hr]
            elif hr != 'all' and each == 'dolocationid':
                rrtt = rrtt[rrtt['dropoff_hour'] == hr]
            else:
                pass
            if mth != 'all':
                rrtt = rrtt[rrtt['month'] == mth]
            else:
                pass
            if day != 'all':
                rrtt = rrtt[rrtt['day_of_week'] == day]
            else:
                pass
            if hlday != 'all':
                rrtt = rrtt[rrtt['holiday'] == hlday]
            else:
                pass
            rr = pd.DataFrame(rrtt[each].value_counts())
            rr.columns = ['value']
            for i in all_points:
                if i not in list(rr.index):
                    rr.append(pd.DataFrame(data={'value': 0}, index=[i]))
            # print(datetime.datetime.now() - timee)
            # so_far = [each, tipo, yr, hr, mth, day, hlday, 'over']
            # print(so_far)
            # true.append(so_far)
            #
            # pickle_out = open("true.pickle", "wb")
            # pickle.dump(true, pickle_out)
            # pickle_out.close()
            return rr


        all_points = pu_do_data['Pick-Up']['fhv'].index

        for colour in ['yellow', 'green', 'fhv']:
            #
            # pickle_in = open("data_{}_cut.pickle".format(colour),"rb")
            # df = pickle.load(pickle_in)
            # print(df.columns)
            # df.rename({"tpep_dropoff_datetime": "dropoff_datetime", "tpep_pickup_datetime": "pickup_datetime", }, axis = 'columns', inplace = True)
            # df.rename({"lpep_dropoff_datetime": "dropoff_datetime", "lpep_pickup_datetime": "pickup_datetime", }, axis = 'columns',
            #               inplace=True)
            # print(df.columns)
            # df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
            # df['day'] = [x.day for x in df['pickup_datetime']]
            # df.drop([x.lower() for x in df.columns if x not in ['pickup_datetime', 'dropoff_datetime', 'pulocationid',
            #    'dolocationid', 'pickup_hour', 'dropoff_hour', 'year', 'month', 'day',
            #    'day_of_week', 'weekend', 'holiday', 'colour']], 1, inplace=True)
            pickle_in = open("data_{}1.pickle".format(colour),"rb")
            df_one[colour] = pickle.load(pickle_in)
            print(datetime.datetime.now()-timee)

        big_dict = {'pulocationid': {}, "dolocationid": {}}
        # pickle_in = open("all_data001.pickle", "rb")
        # big_dict = pickle.load(pickle_in)
        print()
        df_one['all'] = pd.concat([df_one[x] for x in ['yellow', 'green', 'fhv']], sort=False)
        print(df_one['all'].sample(20).to_string())
        # for each in ['pulocationid', "dolocationid"]:
        for each in ['pulocationid']:
            for tipo in tqdm(['yellow', 'green', 'fhv', 'all']):
                big_dict[each][tipo] = {}
                for yr in [2016, 2017, 2018, 'all']:
                    big_dict[each][tipo][str(yr)] = {}
                    for hr in [18, 19, 20, "all"]:
                        big_dict[each][tipo][str(yr)][str(hr)] = {}
                        for mth in list(range(1,13)) + ['all']:
                            big_dict[each][tipo][str(yr)][str(hr)][str(mth)] = {}
                            for day in list(range(1,8)) + ['all']:
                                big_dict[each][tipo][str(yr)][str(hr)][str(mth)][str(day)] = {}
                                for hlday in [0, 1, 'all']:
                                    zz = [each, tipo, yr, hr, mth, day, hlday, 'over']
                                    print(zz)
                                    big_dict[each][tipo][str(yr)][str(hr)][str(mth)][str(day)][str(hlday)] = transform(df_one, each, tipo, yr, hr, mth, day, hlday)

                                    pickle_out = open("progress0.pickle", "wb")
                                    pickle.dump(big_dict, pickle_out)
                                    pickle_out.close()
                                    gc.collect()
        # result_dict = dask.compute(big_dict)
        # pprint(result_dict)
        pickle_out = open("final0.pickle", "wb")
        pickle.dump(big_dict, pickle_out)
        pickle_out.close()
        print(datetime.datetime.now()-timee)

    main()