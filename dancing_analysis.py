import numpy as np
import requests
import pandas as pd
import polars as pl
from dateutil import parser
import re
from io import StringIO
import datetime
import os


def extract_style(text:str) -> str:
    if 'salsa' in text:
        return 'salsa'
    elif 'bachata' in text:
        return 'bachata'
    else:
        return text

def extract_dance_style(df_series):
    return df_series.apply(extract_style)

def filter_df(xdf, filters_to_use=None):
    if filters_to_use:
        for x in filters_to_use:
            if x == 'first_month':
                xdf = xdf[xdf['payment_method']=="one month pass - promo for new students only"]
            if x == 'not_first_month':
                xdf = xdf[(xdf['payment_method'] != "one month pass - promo for new students only")]
            if x == 'attended':
                xdf = xdf[xdf['status']=='signed in']
            if x == 'cancelled':
                xdf = xdf[xdf['status'] =='late cancel']
            if x == 'salsa':
                xdf = xdf[xdf['class_type'].str.contains('salsa')]
            if x == 'bachata':
                xdf = xdf[xdf['class_type'].str.contains('bachata')]
            if x == 'level_1':
                xdf = xdf[xdf['class_level']=="1"]
            if x == 'level_2':
                xdf = xdf[xdf['class_level']=="2"]
            if x == 'level_3':
                xdf = xdf[xdf['class_level'] == "3"]
    return xdf

def info_string(xdf):
    return f"""I've attended {len(filter_df(xdf, ['attended']).index)} classes out of {len(xdf.index)} that I signed up for. {len(filter_df(xdf, ['cancelled']).index)} I cancelled late."""


today = datetime.datetime.now()
path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
data_path = path + 'data/'

with open(data_path + "html_data.txt", 'r+') as filee:
    html = filee.read()

# DATA CLEANING

idf = pd.read_html(StringIO(str(html)))[3]
idf = idf.dropna(axis=1, how='all')
# fix the column names
idf.columns = [i.lower().replace(" ", "_") for i in idf.columns]
new_cols = [f'time{x}' for x in range(2)]
idf.columns = ['date'] + new_cols + list(idf.columns)[2:-1]
# create a timestamp column
idf = idf.drop(columns=['time0'])
idf['timestamp'] = pd.to_datetime([a + ' ' + b for a,b in zip(idf['date'], idf['time1'])])
cl = []
ct = []
for i in idf['class_type']:
    try:
        new = i.split(',')
        cl.append(new[1])
        ct.append(new[0])
    except:
        cl.append(i)
        ct.append(i)
idf['class_level'] = cl
idf['class_type'] = ct

for x in ['class_type', "class_level", "status", "payment_method"]:
    idf[x] = idf[x].str.lower()

# remove columns that aren't so useful and sort the df
idf = idf.sort_values("timestamp", ascending=True)
idf = idf[["timestamp","teacher","class_type","class_level", "payment_method","status",
           #"web","payment_ref_#","date","time1",
           ]]
idf['class_name'] = idf['class_type']
# remove assessments and private lessons
idf = idf[~idf['class_name'].isin(['private lesson'])]
idf = idf[~idf['class_name'].str.contains('assessment')]
# fix the class_level column
temp_df = idf[idf['class_level'].str.contains('all')]
idf.loc[temp_df.index,'class_level'] = "1-2-3-4-5"
idf['class_level'] = idf['class_level'].str.extract(r'(\d)')
idf['class_type'] = extract_dance_style(idf['class_type'])
idf['day_of_week'] = idf['timestamp'].dt.day_name()
idf['year'] = idf['timestamp'].dt.year
idf['month'] = idf['timestamp'].dt.month

print(idf.tail(15).to_string())

# ANALYSIS
dataframes = {}
dataframes['attended'] = filter_df(idf, [ 'attended'])
dataframes['not_first_month'] = filter_df(idf, ['not_first_month', 'attended'])
dataframes['first_month'] = filter_df(idf, ['first_month', 'attended'])
dataframes['first_month_salsa'] = filter_df(idf, ['first_month', 'salsa', 'attended'])
dataframes['first_month_bachata'] = filter_df(idf, ['first_month', 'bachata', 'attended'])
dataframes['bachata'] = filter_df(idf, ['bachata', 'attended'])
dataframes['salsa'] = filter_df(idf, ['salsa', 'attended'])
dataframes['level_1'] = filter_df(idf, ['level_1', 'attended'])
dataframes['level_2']= filter_df(idf, ['level_2', 'attended'])
dataframes['level_3'] = filter_df(idf, ['level_3', 'attended'])

for x in idf['teacher'].unique():
    dataframes[x] = idf[idf['teacher']==x].copy()

per_month_dfs = {}
per_month_dfs['bachata'] = dataframes['bachata'].groupby(['year', 'month']).agg(bachata=pd.NamedAgg(column="class_type", aggfunc="count"))
per_month_dfs['salsa'] = dataframes['salsa'].groupby(['year', 'month']).agg(salsa=pd.NamedAgg(column="class_type", aggfunc="count"))
per_month_dfs['level_1'] = dataframes['level_1'].groupby(['year', 'month']).agg(level_1=pd.NamedAgg(column="class_type", aggfunc="count"))
per_month_dfs['level_2'] = dataframes['level_2'].groupby(['year', 'month']).agg(level_2=pd.NamedAgg(column="class_type", aggfunc="count"))
per_month_dfs['level_3'] = dataframes['level_3'].groupby(['year', 'month']).agg(level_3=pd.NamedAgg(column="class_type", aggfunc="count"))

for x in idf['teacher'].unique():
    per_month_dfs[x] = dataframes[x].groupby(['year', 'month']).agg(teacher=pd.NamedAgg(column="class_type", aggfunc="count"))
    per_month_dfs[x][x] =per_month_dfs[x]['teacher']
    per_month_dfs[x] = per_month_dfs[x].drop(columns=['teacher'])

per_month = pd.concat(per_month_dfs.values(), axis=1).fillna(0).astype(int)
for x in per_month.columns:
    per_month[x+"_cumsum"] = per_month[x].cumsum()


pp = info_string(idf)
print("\r\rOverall: " + pp)
print(dataframes['attended']['class_type'].value_counts())
print(dataframes['attended']['teacher'].value_counts())
print(dataframes['attended']['class_level'].value_counts())
print("")
pp = info_string(dataframes['not_first_month'])
print("\r\rNot First Month: " + pp)
print(dataframes['not_first_month']['class_type'].value_counts())
print(dataframes['not_first_month']['teacher'].value_counts())
print(dataframes['not_first_month']['class_level'].value_counts())
print("")

pp = info_string(dataframes['first_month'])
print("\r\rFirst Month: " + pp)
print(dataframes['first_month']['class_type'].value_counts())
print(dataframes['first_month']['teacher'].value_counts())
print(dataframes['first_month']['class_level'].value_counts())
print("")
pp = info_string(dataframes['first_month_salsa'])
print("\r\rFirst Month + Salsa: " + pp)
print(dataframes['first_month_salsa']['class_type'].value_counts())
print(dataframes['first_month_salsa']['teacher'].value_counts())
print(dataframes['first_month_salsa']['class_level'].value_counts())
print("")
pp = info_string(dataframes['first_month_bachata'])
print("\r\rFirst Month + Bachata: " + pp)
print(dataframes['first_month_bachata']['class_type'].value_counts())
print(dataframes['first_month_bachata']['teacher'].value_counts())
print(dataframes['first_month_bachata']['class_level'].value_counts())


print(per_month.to_string())


print("")
print(datetime.datetime.now()-today)

