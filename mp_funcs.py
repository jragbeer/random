import dask
from dask.distributed import Client
import pandas as pd
import numpy as np
import time

@dask.delayed
def do_work():
    time.sleep(50)
    return np.random.randint(0,10)

if __name__ == '__main__':
    def mp():
        Client(threads_per_worker=3, n_workers = 3, memory_limit = '5GB')
        out = []
        for x in range(20):
            out.append(do_work())
        out= dask.compute(*out)
        df = pd.DataFrame({'a':out})
        df.to_csv("C:/Users/Julien/PycharmProjects/practice/data/tmp_table.csv",)
    mp()

