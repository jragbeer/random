import numpy as np
import pandas as pd
import sqlite3
import datetime
import traceback
import gc


path = "C:/Users/Julien/PycharmProjects/nyctaxi/data/"
db = 'NYC_Taxi_Data.db'
timee = datetime.datetime.now()
conn = sqlite3.connect(path+db)

switch = {"Green": "Green_Taxi_Trip_Data",
          "Yellow": "Yellow_Taxi_Trip_Data",
          "FHV": "For_Hire_Vehicles_Trip_Data",
          "HVFHV": "HV_FHV",}

def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()

def etl_csv_to_db(df):
    df.columns = [x.replace(' ', '_').lower().replace('lpep_', '').replace("tpep_", '') for x in df.columns]
    print(df.columns)
    df = df[['pickup_datetime', "dropoff_datetime", "pulocationid", "dolocationid"]]
    df['dolocationid'] = pd.to_numeric(df['dolocationid'], errors='coerce', downcast='integer')
    df['pulocationid'] = pd.to_numeric(df['pulocationid'], errors='coerce', downcast='integer')
    df.dropna(how='any', inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df

def create_initial_database_from_csv(year, colour):
    # create database and add data to it
    try:
        print(year, colour)
        fp = path + f"{year}_{switch[colour]}.csv"
        dfcolumns = pd.read_csv(fp, nrows=1)
        df_list = []
        data = pd.read_csv(fp, header=None, skiprows=1, usecols=list(range(1, len(dfcolumns.columns))),
                           chunksize=15_000_000, names=dfcolumns.columns, error_bad_lines=False, engine = 'python')
        n = 1
        for chunk in data:
            print(n)
            df_list.append(etl_csv_to_db(chunk))
            n+=1

        large_df = pd.concat(df_list)
        if 'fhv' in colour.lower():
            large_df.to_sql(f'{year}_FHV', conn, if_exists='append', index=False)
        else:
            large_df.to_sql(f'{year}_{colour.upper()}', conn, if_exists='replace', index=False)
        print('done', datetime.datetime.now() - timee)

    except Exception as e:
        print(error_handling())

for i in ['FHV']:
    for yr in [2018]:
        create_initial_database_from_csv(yr, i)
        gc.collect()
