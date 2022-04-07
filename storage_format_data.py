import numpy as np
import pandas as pd
import os
import datetime
import sqlite3
import gc
import pymongo
import sqlalchemy

path = os.getcwd().replace("\\", "/") + "/"
data_path = path + 'data/'
today = datetime.datetime.now()
print(today)

file="data_15_list"

#DATABASE CONNECTIONS
engine = sqlalchemy.create_engine('mssql+pyodbc://localhost/storage_medium?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
sqlite_db = sqlite3.connect(f"{file}.db") # local db
mongodb = pymongo.MongoClient('localhost', 27017)

def make_df_to_work_on(rows= 15_000_000):
    df = pd.DataFrame({
    'a':np.random.randint(1,10, rows)*0.1,
    'aa':np.random.randint(1,10, rows)*2.8,
    'aaa':np.random.randint(1,10, rows)*3.2,
    'aaqa':np.random.randint(1,10, rows)*3.2,
    'b':pd.date_range('2000-01-01', freq='1T', periods = rows),
    'bb':np.random.randint(1,10, rows),
    'bbb':np.random.randint(1,10, rows),
    'bbbbbb':np.random.randint(1,10, rows),
    'bbbbb':np.random.randint(1,10, rows),
    'bbbb':np.random.randint(1,10, rows),
    'c':[np.random.choice(['a', 'b', 'c',], 3) for i in range(rows)],
    })
    df.info()
    df.to_pickle(f'data_{str(rows)[0]}_list.pickle')
def write(file="data_15_list", method = 'csv'):
    df = pd.read_pickle(f'{file}.pickle', )
    print(df.tail().to_string())
    xxx = datetime.datetime.now()
    print(xxx-today)

    if method == 'sql_server':
        df['c'] = df['c'].astype(str)
        # method = 'sql_server'
        df.to_sql(f'{file}', engine, index=False, if_exists='replace',)
    if method == 'sqlite':
        df['c'] = df['c'].astype(str)
        # method = 'sql_server'
        df.to_sql(f'{file}', sqlite_db, index=False, if_exists='replace',)
    if method == 'csv':
    # method = 'csv'
        df.to_csv(f'{file}.csv', index=False)
    if method == 'parquet':
    # method = 'parquet'
        df.to_parquet(f'{file}.parquet')
    if method == 'mongo_records':
        mongo_db = mongodb['col'][file]
        wow = df.to_dict('records')
        print(type(wow))
        mongo_db.insert_many(wow)

    info = {'rows': len(df.index),
           'size': np.round(df.memory_usage(deep=True).sum()/1024/1024,1),
           'method':method,
            'file':file}
    info['time'] = str(datetime.datetime.now()-xxx)
    print(info)
    with open('data.txt', 'a') as file:
        file.write(str(info) + '\n')
def read(size=1, storage='parquet', ):
    xxx = datetime.datetime.now()
    # print(xxx-today)
    file = f'data_{size}_list'
    if storage == "parquet":
        df = pd.read_parquet(file + '.parquet')
    elif storage == "csv":
        df = pd.read_csv(file + '.csv')
    elif storage == 'mongo_records':
        mongo_db = mongodb['col'][file]
        df = pd.DataFrame(mongo_db.find({}))
    elif storage == 'sqlite':
        db = sqlite3.connect(f"{file}.db") # local db
        df = pd.read_sql(f"select * from {file}", db)
    elif storage == 'sql_server':
        df = pd.read_sql(f"select * from {file}", engine)
    # print(df.head().to_string())
    yyy = datetime.datetime.now()
    # print(yyy-today)
    info = {'rows': len(df.index),
           'size': np.round(df.memory_usage(deep=True).sum()/1024/1024,1),
           'method':storage,
            'file':file,
            "operation":'read'}
    info['time'] = str(datetime.datetime.now()-xxx)
    print(info)
    with open('data_write.txt', 'a') as f:
        f.write(str(info) + '\n')
    del info
    del df
    gc.collect()
def read_query(size=1, storage='parquet', ):
    xxx = datetime.datetime.now()
    # print(xxx-today)
    file = f'data_{size}_list'
    if storage == "parquet":
        df = pd.read_parquet(file + '.parquet', columns = ['a', 'bbb'])
        out = [df['a'].max(), df['bbb'].sum(), len(df.index), ]
        print(out)
    elif storage == "csv":
        df = pd.read_csv(file + '.csv')
        out = [df['a'].max(), df['bbb'].sum(), len(df.index), ]
        print(out)
    elif storage == 'mongo_records':
        mongo_db = mongodb['col'][file]
        # pipe = db.collection.aggregate();
        query = mongo_db.aggregate([{"$group" : {"_id": None, "max": { "$max" : "$a" }, "sum": { "$sum" : "$bbb" }, "count": { "$sum" : 1 }}}])
        df = pd.DataFrame(query)
        # out = [df['a'].max(),df['bbb'].sum(),len(df.index),]
        print(df)
    elif storage == 'sqlite':
        db = sqlite3.connect(f"{file}.db") # local db
        df = pd.read_sql(f"select max(a), sum(bbb), count(*) from {file}", db)
        print(df)
    elif storage == 'sql_server':
        df = pd.read_sql(f"select max(a), sum(bbb), count(*) from {file}", engine)
        print(df)
    # print(df.head().to_string())
    yyy = datetime.datetime.now()
    # print(yyy-today)
    info = {'rows': len(df.index),
           'size': np.round(df.memory_usage(deep=True).sum()/1024/1024,1),
           'method':storage,
            'file':file,
            "operation":'read_query'}
    info['time'] = str(datetime.datetime.now()-xxx)
    print(info)
    with open('data_write.txt', 'a') as f:
        f.write(str(info) + '\n')
    del info
    del df
    gc.collect()
def read_complex_query(size=1, storage='parquet', ):
    xxx = datetime.datetime.now()
    # print(xxx-today)
    file = f'data_{size}_list'
    sql = f"""select 11.5 * sum(a)/count(*) as mean, sum(bbb), count(*), c from (
    select * from {file}
    where bbbb < 8 and bbbb > 4) as temp
    group by c
    order by c desc"""

    if storage == "parquet":
        df = pd.read_parquet(file + '.parquet', columns = ['c', 'bbb', 'bbbb'])
        yyy = datetime.datetime.now()
        print('read: ' ,yyy-xxx)
        df = df[(df['bbbb'] > 4) & (df['bbbb'] < 8)].copy()
        df['c'] = df['c'].astype(str)
        df = df.groupby(['c']).agg({'bbb':'sum', 'bbbb':'count'}).reset_index()
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.sort_values('c')
        # print(df)
    elif storage == "csv":
        df = pd.read_csv(file + '.csv')
        yyy = datetime.datetime.now()
        print('read: ' ,yyy-xxx)
        df = df[(df['bbbb'] > 4) & (df['bbbb'] < 8)].copy()
        df['c'] = df['c'].astype(str)
        df = df.groupby(['c']).agg({'bbb':'sum', 'bbbb':'count'}).reset_index()
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.sort_values('c')
        # print(df)
    elif storage == 'mongo_records':
        mongo_db = mongodb['col'][file]
        query = mongo_db.aggregate(
            [{"$group": {"_id": "$c", "bbb": {"$sum": "$bbb"}, "bbbb": {"$sum": 1}, }}])
        df = pd.DataFrame(query)
        # out = [df['a'].max(),df['bbb'].sum(),len(df.index),]
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.rename(columns={'_id':'c'})
        df = df.sort_values('c')
        # print(df)
    elif storage == 'sqlite':
        db = sqlite3.connect(f"{file}.db") # local db
        df = pd.read_sql(sql, db)
        # print(df)
    elif storage == 'sql_server':
        df = pd.read_sql(sql, engine)
        # print(df)
    print(df.head().to_string())
    yyy = datetime.datetime.now()
    # print(yyy-today)
    info = {'rows': len(df.index),
           'size': np.round(df.memory_usage(deep=True).sum()/1024/1024,1),
           'method':storage,
            'file':file,
            "operation":'read_complex_query'}
    info['time'] = str(datetime.datetime.now()-xxx)
    print(info)
    with open('data_write.txt', 'a') as f:
        f.write(str(info) + '\n')
    del info
    del df
    gc.collect()
def read_interesting_query(size=1, storage='parquet', ):
    xxx = datetime.datetime.now()
    # print(xxx-today)
    file = f'data_{size}_list'
    sql = f"""select 11.5 * sum(a)/count(*) as mean, sum(bbb), count(*), c from (
    select * from {file}
    where bbbb < 8 and bbbb > 4) as temp
    group by c
    order by c desc"""

    if storage == "parquet":
        df = pd.read_parquet(file + '.parquet', columns = ['c', 'bbb', 'bbbb'])
        yyy = datetime.datetime.now()
        print('read: ' ,yyy-xxx)
        df = df[(df['bbbb'] > 4) & (df['bbbb'] < 8)].copy()
        df['c'] = df['c'].astype(str)
        df = df.groupby(['c']).agg({'bbb':'sum', 'bbbb':'count'}).reset_index()
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.sort_values('c')
        # print(df)
    elif storage == "csv":
        df = pd.read_csv(file + '.csv')
        yyy = datetime.datetime.now()
        print('read: ' ,yyy-xxx)
        df = df[(df['bbbb'] > 4) & (df['bbbb'] < 8)].copy()
        df['c'] = df['c'].astype(str)
        df = df.groupby(['c']).agg({'bbb':'sum', 'bbbb':'count'}).reset_index()
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.sort_values('c')
        # print(df)
    elif storage == 'mongo_records':
        mongo_db = mongodb['col'][file]
        query = mongo_db.aggregate(
            [{"$group": {"_id": "$c", "bbb": {"$sum": "$bbb"}, "bbbb": {"$sum": 1}, }}])
        df = pd.DataFrame(query)
        # out = [df['a'].max(),df['bbb'].sum(),len(df.index),]
        df['mean'] = 11.5*df['bbb']/df['bbbb']
        df = df.rename(columns={'_id':'c'})
        df = df.sort_values('c')
        # print(df)
    elif storage == 'sqlite':
        db = sqlite3.connect(f"{file}.db") # local db
        df = pd.read_sql(sql, db)
        # print(df)
    elif storage == 'sql_server':
        df = pd.read_sql(sql, engine)
        # print(df)
    print(df.head().to_string())
    yyy = datetime.datetime.now()
    # print(yyy-today)
    info = {'rows': len(df.index),
           'size': np.round(df.memory_usage(deep=True).sum()/1024/1024,1),
           'method':storage,
            'file':file,
            "operation":'read_complex_query'}
    info['time'] = str(datetime.datetime.now()-xxx)
    print(info)
    with open('data_write.txt', 'a') as f:
        f.write(str(info) + '\n')
    del info
    del df
    gc.collect()
# for x in ['parquet', 'sqlite', 'csv', 'sql_server', 'mongo_records']:
# write("data_15_list", 'mongo_records')


print(datetime.datetime.now()-today)

for z in range(5):
    for x in [
        'parquet',
        'sqlite', 'csv',
        'sql_server',
              'mongo_records'
              ]:
        for y in [
            1,
                  5,
                  15,
        ]:
                read_query(y, x)
    print(datetime.datetime.now() - today)
print(datetime.datetime.now()-today)
