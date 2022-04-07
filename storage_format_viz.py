import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# pd.set_option('display.max_rows', 1200000)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.float_format', lambda x: '%.5f' % x)

def thing(f = 'data.txt'):
    ok = []
    with open(f, 'r') as file:
        for each in file:
            ok.append(json.loads(each.replace("'", '"')))
    df = pd.DataFrame(ok)
    df['time'] = pd.to_timedelta(df['time']).dt.seconds
    # print(df)
    for each in ["data_1_list", "data_5_list", "data_15_list"]:
        kdf = df[df['file'] == each].copy()
        kdf['count'] = 1
        kdf = kdf.sort_values('time', ascending=False)
        print(kdf)
        # kdf = kdf.iloc[:5, :]
        idf = kdf.groupby(['method']).agg({'rows':'mean', 'file':'max','time':'mean','count':'count',}).sort_values("time", ascending = True)
        print(idf)
        idf['time'].plot(kind = 'bar')
        plt.title(f"{each.upper()} Dataset / Write Operation")
        plt.show()
def thing2(f = 'data_write.txt'):
    ok = []
    with open(f, 'r') as file:
        for each in file:
            ok.append(json.loads(each.replace("'", '"')))
    df = pd.DataFrame(ok)
    df['time'] = pd.to_timedelta(df['time'])
    df['time'] = np.round(df['time'].dt.seconds + df['time'].dt.microseconds/1000000,1)

    # print(df)
    for aa in sorted(df['operation'].unique())[::1]:
        print(aa.upper())
        pdf = df[df['operation'] == aa].copy()
        for each in ["data_1_list", "data_5_list", "data_15_list"]:
            kdf = pdf[pdf['file'] == each].copy()
            kdf['count'] = 1
            kdf = kdf.sort_values('time', ascending=False)
            inner = []
            for z in kdf['method'].unique():
                inner.append(kdf[kdf['method'] == z].copy().sort_values('time', ascending = True).iloc[:5,:])
            kdf = pd.concat(inner)
            idf = kdf.groupby(['method']).agg({'rows':'mean', 'file':'max','time':'mean','count':'count',}).sort_values("time", ascending = True)
            # print(kdf)
            print(idf)
            idf['time'].plot(kind = 'barh', orientation = 'horizontal')
            plt.title(f"{each.upper()} Dataset / {aa.upper()} Operation")
            plt.show()
        print("*" * 8)

thing()
print("*"*8)
# thing2()