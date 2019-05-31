import numpy as np
import pandas as pd
import urllib
import sqlite3
import datetime
timee = datetime.datetime.now()

# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-01.csv

path = "C:/Users/J_Ragbeer/Desktop/"
path2 = "C:/Users/J_Ragbeer/PycharmProjects/NYCTaxi/data/"
db = 'NYC_Taxi_Data.db'
conn = sqlite3.connect(path2 + db)

# # Download data from AWS S3
# for yr in range(6,9):
#     for month in range(1,13):
#         urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/trip+data/"
#                                    "yellow_tripdata_201{}-{0:0=2d}.csv".format(yr,month),
#                                    path2+ "nyc.201{}-{}.csv".format(yr,month))


# create database and add data to it
# chunksize =100000
# for yr in range(7,9):
#     for month in range(1, 13):
#         print(yr, month)
#         fp = path2+"nyc.201{}-{}.csv".format(yr,month)
#         dfcolumns = pd.read_csv(fp, nrows=1)
#         df = pd.read_csv(fp,header=None, skiprows=1, usecols=list(range(len(dfcolumns.columns))), names=dfcolumns.columns)
#         df.rename(columns={c: c.replace(' ', '_') for c in df.columns})
#         df['pickup_hour'] = [int(str(x)[11:13]) for x in df['tpep_pickup_datetime']]
#         df['dropoff_hour'] = [int(str(x)[11:13]) for x in df['tpep_dropoff_datetime']]
#         df.to_sql('Trip_Data', conn, if_exists='append', index=False)
#         print('done')
#         print('month', datetime.datetime.now() - timee)
#     print('year', datetime.datetime.now() - timee)

df = pd.read_sql('select PULocationID, DOLocationID, passenger_count, pickup_hour from Trip_Data where pickup_hour >= 18 and pickup_hour < 21', conn)
print(df.sample(26).to_string())
print(datetime.datetime.now()-timee)
print('over')