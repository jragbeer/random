import datetime
import pandas as pd
import numpy as np
import time
import os
import glob
from dateutil import parser
from os.path import dirname, join
import pickle
import calendar
import sqlite3
from shutil import copyfile, copy2

def make_dataframes_from_EnernocCsvs():
    path = r'xx'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    meters = [pd.read_csv(f,encoding = 'utf-8', nrows=1, header = None, names = ['a','b'])['b'].values[0].split('(')[0].strip() for f in all_files]
    meters = [x.replace(' ', '').replace('-', '').replace('.', '').replace(',', '').replace('#', '') for x in meters]
    mets= {str(x):pd.DataFrame(columns = ['Date/Time', 'Energy']) for x in meters}
    # print(all_files)

    for a in all_files:
        for b in meters:
            if pd.read_csv(a,encoding = 'utf-8', nrows=1, header = None, names = ['a','b'])['b'].values[0].split('(')[0].strip().replace(' ', '').replace('-', '').replace('.', '').replace(',', '').replace('#', '') == b:
                mets[b] = pd.concat([mets[b] , pd.read_csv(a, encoding = 'utf-8', skiprows=2, header = None, names = ['Date/Time', 'Energy'])])
    for x in mets:
        mets[x]['Date/Time'] = pd.to_datetime(mets[x]['Date/Time'])
        mets[x].drop_duplicates(inplace=True)
        mets[x].reset_index(inplace=True)
        mets[x]['Date/Time'] = pd.Series([(p - datetime.datetime(1970,1,1)).total_seconds() for p in mets[x]['Date/Time']] , index = mets[x].index)
    oo, mets = count_missing_vals(mets)

    return mets, oo
def create_table(nameOfTable):
    c2.execute("CREATE TABLE IF NOT EXISTS {}(INTERVAL_DTTM TEXT, MEMBER_ID REAL, CHANNEL_ID REAL, QTR_HOUR_AGGREGATE_ID REAL, LAST_UPDATED_DTTM REAL, ANAMOLY_TYPE_ID REAL, ESTIMATED_DATA_IND REAL, MEASURE_QTY REAL, MIN_VALUE REAL, MAX_VALUE REAL, SUM_VALUE REAL)".format('"'+nameOfTable+'"'))
def data_entry(nameOfTable, INTERVAL_DTTM, MEMBER_ID, CHANNEL_ID, QTR_HOUR_AGGREGATE_ID, LAST_UPDATED_DTTM, ANOMALY_TYPE_ID, ESTIMATED_DATA_IND, MEASURE_QTY, MIN_VALUE, MAX_VALUE, SUM_VALUE):
    c2.execute("INSERT INTO {} VALUES({},{},{},{},{},{},{},{},{},{},{})".format('"'+nameOfTable+'"', INTERVAL_DTTM, MEMBER_ID, CHANNEL_ID, QTR_HOUR_AGGREGATE_ID, LAST_UPDATED_DTTM, ANOMALY_TYPE_ID, ESTIMATED_DATA_IND, MEASURE_QTY, MIN_VALUE, MAX_VALUE, SUM_VALUE))
    # conn.commit()
def make_db_tables():
    for y in bigdict:
        bigdict[y].fillna(0, inplace=True)
    for x in bigdict:
        conn.execute('BEGIN')
        create_table(str(x))
        print(x, datetime.datetime.now()-timee)
        for y in bigdict[x].itertuples():
            data_entry(x, '"'+y[1]+'"', y[2],y[3],y[4],'"'+y[5]+'"',y[6],y[7],y[8], y[9], y[10], y[11])
        conn.commit()

def intodatetime(date):
    return parser.parse(date.split()[0]+" "+date.split()[1].replace('.', ':')[:8]+" "+date.split()[2])

def intoenernoc(date):
    return date.strftime('%d-%b-%y %I.%M.%S.000000000 %p').upper()

def fifteenMinInterval(date):
    newdate = intodatetime(date)
    return intoenernoc(newdate + datetime.timedelta(minutes = 15))

conn = sqlite3.connect(path + 'x.db')
c = conn.cursor()

copy2(path + 'x.db', path + 'x.db')
print('copy successful')
conn2 = sqlite3.connect(path + 'x.db')
c2 = conn2.cursor()
# print('SELECT YOUR DATE TO INGEST FROM (this date/time will be included in starting data): ')
# date1 = input('input DATE as dd-mmm-yy : ')
# time1 = input('input HOUR (24) : ')
# mins1 = input('input MINS as (0, 15, 30, 45) : ')
#
# date2 = date1+" "+time1+":"+mins1
#
# print('date Parse: ', parser.parse(date2))
# date = intoenernoc(parser.parse(date2))
date = '01-JAN-17 03.15.00.000000000 PM' #SAFE DATE

time.sleep(2)
for x in namesReal:
    c2.execute('SELECT ROWID FROM "{}" where INTERVAL_DTTM = {}'.format(x, '"' + date + '"'))
    dat = c2.fetchall()
    print(x, dat)

    c2.execute('SELECT * FROM "{}" where ROWID < {}'.format(x, dat[0][0]))
    newdat = c2.fetchall()
    c2.execute('DROP TABLE "{}"'.format(x))

    print(x, 'table dropped')
    conn2.commit()
    time.sleep(1)
    create_table(x)
    print('table {} created'.format(x))
    conn2.commit()
    for y in newdat:
        data_entry(x, '"' + y[0] + '"', y[1],y[2], y[3],'"' + y[4] + '"', y[5],y[6], y[7],y[8], y[9],y[10])
    conn2.commit()
    print(x,'data entered')
conn2.commit()

my_date = intodatetime(date)

while True:
    for x in namesReal:

        c.execute('SELECT * FROM {} where INTERVAL_DTTM = "{}"'.format('"' + x + '"', date))
        data = c.fetchall()
        print(data)
        time.sleep(3)
        if len(data) > 0:
            c2.execute("INSERT INTO {} VALUES({},{},{},{},{},{},{},{},{},{},{})".format('"' + x + '"', '"' + data[0][0]+ '"',
                                                                                        data[0][1], data[0][2],
                                                                                        data[0][3], '"' + data[0][4]+ '"',
                                                                                        data[0][5], data[0][6],
                                                                                        data[0][7], data[0][8], data[0][9],
                                                                                        data[0][10]))
            conn2.commit()
            print(date, x, 'actual row appended')
        else:
            c2.execute('INSERT INTO {} VALUES("{}",{},{},{},{},{},{},{},{},{},{})'.format('"' + x + '"', date, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
            conn2.commit()
            print(date, x, 'fake data appended')
        # print(x,data)

    d = input('continue? type "no" if not')
    if d == 'no':
        break
    date = fifteenMinInterval(date)

conn2.close()
conn.close()

# if os.path.exists(path + 'x.db'):
#     os.remove(path + 'x.db')
# else:
#     print("The file does not exist")
# print('db copy is destroyed')
