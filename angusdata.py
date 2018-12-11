import calendar
import numpy as np
import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt


def make_chart(idf, colour):
    w = {}
    for y in idf['RequestType'].unique():
        pp = []
        for x in idf.itertuples():
            if y == x.RequestType:
                pp.append(str(datetime.date(x.Date.year, x.Date.month, x.Date.day)))
        w[str(y)] = {'vals': {str(x): pp.count(x) for x in pp}}
        w[str(y)]['count'] = len(pp)
    for x in w.keys():
        for y in [str(datetime.date(x.year, x.month, x.day)) for x in
                  pd.date_range(datetime.date(2000, 1, 1), datetime.date(2000, 12, 31))]:
            if y not in w[x]['vals'].keys():
                w[x]['vals'][str(y)] = 0
    ytho = [c for c in w.keys() if c.startswith('HVAC')]
    print(ytho)
    print(w.values())
    for q in sorted(ytho[-2:], key=lambda x: w[x]['count']):
        plt.figure()
        plt.title(str(q))
        r = []
        o = []
        print(q)
        print(str(q))
        for x in sorted(w[str(q)]['vals'].keys()):
            r.append(x)
            o.append(w[str(q)]['vals'][x])

        plt.bar(r, o, color = colour)
def make_season_column(idf):
    y = []
    for x in idf['Month']:
        if x in [1,2,12]:
            y.append('Winter')
        elif x in [6,7,8,9]:
            y.append('Summer')
        elif x in [3,4,5]:
            y.append('Spring')
        else:
            y.append('Fall')
    return pd.Series(y)

df = pd.read_csv('metrocentreAngusdata.csv', engine = 'python')
df.drop(['Property'], 1, inplace = True)

df.rename(columns = {'Request Type':'RequestType', 'Date Closed': 'DateClosed'}, inplace = True)
print(df.columns)
df['DateClosed'] = pd.to_datetime(df['DateClosed'])
df['Year'] = [x.year for x in df['DateClosed']]
df['Month'] = [x.month for x in df['DateClosed']] # months are numbered 1-12
df['Date'] = [datetime.datetime(2000, x.month, x.day) for x in df['DateClosed']] # yearless dates (more accurately year = 2000 for normalization)

df['Season'] = make_season_column(df)
df['Weekday'] = [x for x in df['DateClosed'].dt.dayofweek] #0 is monday, 6 is sunday
# print(df.to_string())
df['RequestType'] = pd.Series([x.upper() for x in df['RequestType']], index = df.index)
info = [[df['RequestType'].value_counts().index[i],
         float('{:.1f}'.format(100 * df['RequestType'].value_counts().values[i] / len(df)))] for i in
        range(len(df['RequestType'].value_counts()))][:10]
p = []
for x in info[:10]:
    print(x)
    p.append(x[1])
startdate = df['DateClosed'].min()
enddate = df['DateClosed'].max()
print('Starting date', startdate)
print('Ending date', enddate)
print('Number of Days in total', (enddate-startdate).days)
print('Number of Weekdays where calls are made', len([x for x in pd.date_range(startdate, enddate) if x.weekday() < 5])) #0 is monday, 6 is sunday
print('{:.1f} calls per day'.format(len(df.index)/787))
metrocentreking = df[df['Building'] == '225 King St. West'].copy()
metrocentrewellington = df[df['Building'] == '200 Wellington St. West'].copy()

print(df.groupby(['Building'])['Date'].count()/787)

print('Top 10 Request types account for {}% of all tickets'.format(sum(p)))

# print(df.Tenant.value_counts())
df2017 = df[df['Year'] == 2017].copy()
# print(df2017.Tenant.value_counts())
# make_chart(metrocentreking, 'red')
# make_chart(metrocentrewellington, 'blue')
plt.show()
