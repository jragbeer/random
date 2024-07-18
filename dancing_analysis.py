import numpy as np
import requests
import pandas as pd
import polars as pl
from dateutil import parser
import re
from io import StringIO
import datetime
import os

def extract_dance_style(df_series):
    def extract_style(text):
        if 'salsa' in text:
            return 'salsa'
        elif 'bachata' in text:
            return 'bachata'
        else:
            return text
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
            if x == 'salsa':
                xdf = xdf[xdf['class_type'].str.contains('salsa')]
            if x == 'bachata':
                xdf = xdf[xdf['class_type'].str.contains('bachata')]
    return xdf

def info_string(xdf):
    return f"""I've attended {len(filter_df(xdf, ['attended']).index)} classes out of {len(xdf.index)} that I signed up for."""


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
print(idf.head().to_string())

# ANALYSIS
not_first_month_df = filter_df(idf, ['not_first_month'])
first_month_df = filter_df(idf, ['first_month'])
first_month_salsa_df = filter_df(idf, ['first_month', 'salsa'])
first_month_bachata_df = filter_df(idf, ['first_month', 'bachata'])

pp = info_string(idf)
print("\r\rOverall: " + pp)
print(filter_df(idf, ['attended'])['class_type'].value_counts())
print(filter_df(idf, ['attended'])['teacher'].value_counts())
print(filter_df(idf, ['attended'])['class_level'].value_counts())

pp = info_string(first_month_df)
print("\r\rNot First Month: " + pp)
print(filter_df(idf, ['not_first_month', 'attended'])['class_type'].value_counts())
print(filter_df(idf, ['not_first_month', 'attended'])['teacher'].value_counts())
print(filter_df(idf, ['not_first_month', 'attended'])['class_level'].value_counts())


pp = info_string(first_month_df)
print("\r\rFirst Month: " + pp)
print(filter_df(idf, ['first_month', 'attended'])['class_type'].value_counts())
print(filter_df(idf, ['first_month', 'attended'])['teacher'].value_counts())
print(filter_df(idf, ['first_month', 'attended'])['class_level'].value_counts())

pp = info_string(first_month_salsa_df)
print("\r\rFirst Month + Salsa: " + pp)
print(filter_df(idf, ['first_month', 'attended', 'salsa'])['class_type'].value_counts())
print(filter_df(idf, ['first_month', 'attended', 'salsa'])['teacher'].value_counts())
print(filter_df(idf, ['first_month', 'attended', 'salsa'])['class_level'].value_counts())

pp = info_string(first_month_bachata_df)
print("\r\rFirst Month + Bachata: " + pp)
print(filter_df(idf, ['first_month', 'attended', 'bachata'])['class_type'].value_counts())
print(filter_df(idf, ['first_month', 'attended', 'bachata'])['teacher'].value_counts())
print(filter_df(idf, ['first_month', 'attended', 'bachata'])['class_level'].value_counts())