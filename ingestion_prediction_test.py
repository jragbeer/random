import datetime
import pandas as pd
import numpy as np
import time
import os
import glob
from dateutil import parser
from os.path import dirname, join
import matplotlib.pyplot as plt
from matplotlib import style
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import pickle
style.use('ggplot')

def hmdxx(x, y):
    return x + (0.5555 * (6.11 * np.exp(5417.7530 * ((1 / 273.16) - (1 / (273.15 + y)))) - 10))
def clean_weather(weather):
    weather.index = pd.to_datetime(weather.index)
    weather.fillna(method='ffill', inplace=True)
    weather['Humidex'] = pd.Series([hmdxx(x[5], x[7]) for x in weather.itertuples()], index=weather.index)
    weather['Hour'] = pd.Series([int(x[0].hour) for x in weather.itertuples()], index=weather.index)
    weather['Weekday'] = pd.Series([int(x[0].weekday()) for x in weather.itertuples()], index=weather.index)
    weather['wd_sin'] = np.sin(weather['Weekday'] * (2. * np.pi / 7))
    weather['wd_cos'] = np.cos(weather['Weekday'] * (2. * np.pi / 7))
    weather['hr_sin'] = np.sin(weather['Hour'] * (2. * np.pi / 24))
    weather['hr_cos'] = np.cos(weather['Hour'] * (2. * np.pi / 24))
    weather['mnth_sin'] = np.sin((weather['Month'] - 1) * (2. * np.pi / 12))
    weather['mnth_cos'] = np.cos((weather['Month'] - 1) * (2. * np.pi / 12))
    weather['Temp'] = weather['Temp (°C)']
    weather['Dew Point Temp'] = weather['Dew Point Temp (°C)']
    weather.drop(['Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)',
                  'Wind Spd Flag', 'Visibility (km)', 'Visibility Flag', 'Temp Flag', 'Dew Point Temp Flag',
                  'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx Flag', 'Wind Chill', 'Rel Hum (%)', 'Hmdx',
                  'Dew Point Temp',
                  'Wind Chill Flag', 'Weather', 'Temp (°C)', 'Dew Point Temp (°C)'], 1, inplace=True)
    return weather
def make_wdata():
    path = r'C:/Users/J_Ragbeer/PycharmProjects/STCBaselines/data/Weather Data/Toronto Weather/'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f,encoding = 'utf-8', skiprows=17, header = None, names = ['Date/Time','Year','Month',	'Day',	'Time',	'Data Quality',	'Temp (C)',	'Temp Flag',	'Dew Point Temp (C)',	'Dew Point Temp Flag',	'Rel Hum (%)',	'Rel Hum Flag',	'Wind Dir (10s deg)',	'Wind Dir Flag',	'Wind Spd (km/h)',	'Wind Spd Flag',	'Visibility (km)',	'Visibility Flag'	,'Stn Press (kPa)',	'Stn Press Flag',	'Hmdx',	'Hmdx Flag',	'Wind Chill',	'Wind Chill Flag',	'Weather']) for f in all_files)
    Wdata = pd.concat(df_from_each_file, ignore_index=True, sort = False)
    Wdata = Wdata[['Year','Day','Month','Date/Time', 'Temp (C)', 'Dew Point Temp (C)']]
    Wdata.fillna(method='ffill', inplace =True)
    Wdata.fillna(method='bfill', inplace =True)
    Wdata.set_index('Date/Time', inplace = True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()
    return Wdata
def make_wdata2018():
    path = r'C:/Users/J_Ragbeer/PycharmProjects/STCBaselines/data/Weather Data/Toronto 2018 Weather/'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f,encoding = 'utf-8', skiprows=17, header = None, names = ['Date/Time','Year','Month',	'Day',	'Time',	'Temp (C)',	'Temp Flag',	'Dew Point Temp (C)',	'Dew Point Temp Flag',	'Rel Hum (%)',	'Rel Hum Flag',	'Wind Dir (10s deg)',	'Wind Dir Flag',	'Wind Spd (km/h)',	'Wind Spd Flag',	'Visibility (km)',	'Visibility Flag'	,'Stn Press (kPa)',	'Stn Press Flag',	'Hmdx',	'Hmdx Flag',	'Wind Chill',	'Wind Chill Flag',	'Weather']) for f in all_files)
    Wdata = pd.concat(df_from_each_file, ignore_index=True, sort = False)
    Wdata = Wdata[['Year','Day','Month','Date/Time', 'Temp (C)', 'Dew Point Temp (C)']]
    Wdata.fillna(method='ffill', inplace =True)
    Wdata.fillna(method='bfill', inplace =True)
    Wdata.set_index('Date/Time', inplace = True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata.sort_index()
    return Wdata
def newdegdays(df):
    newdata = [i[4] for i in df.itertuples()]
    heatdays = [6-x for x in newdata]
    cooldays = [x-6 for x in newdata]
    newheatdays=[]
    newcooldays=[]
    for x in heatdays:
        if x < 0:
            newheatdays.append(0)
        else:
            newheatdays.append(x)
    for x in cooldays:
        if x < 0:
            newcooldays.append(0)
        else:
            newcooldays.append(x)
    return newheatdays,newcooldays
def weather1():
    df = pd.concat([make_wdata(), make_wdata2018()])
    df['Humidex'] = pd.Series([hmdxx(x[4], x[5]) for x in df.itertuples()], index=df.index)
    hdd,cdd = newdegdays(df)
    df['HDD'] = pd.Series(hdd, index = df.index)
    df['CDD'] = pd.Series(cdd, index = df.index)
    return df
def make_data(a):
    df = pd.read_excel(str(a))
    df.set_index('INTERVAL_DTTM',inplace =True)
    df.index = [parser.parse(y.split()[0] + ' ' + y.split()[1].split('.')[0] + ':' + y.split()[1].split('.')[1] + ':' + y.split()[1].split('.')[2] + ' ' + y.split()[2]) for y in df.index]
    df.index = pd.to_datetime(df.index)
    return df
def make_charts(name, a, weath):

    df = make_data(a)

    df = df.resample('D').sum()
    weat = weath.resample('D').mean()

    updateddf = pd.merge(df, weat, left_index=True, right_index=True)
    updateddf['Year'] = pd.Series([i.year for i in updateddf.index], index = updateddf.index)

    updateddf2016 = updateddf[updateddf['Year'] == 2016]
    updateddf2017 = updateddf[updateddf['Year'] == 2017]
    updateddf2018 = updateddf[updateddf['Year'] == 2018]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    plt.suptitle(name+' Plots (Daily)')
    ax3.plot(df.index, df['SUM_VALUE'], color='purple', alpha=0.4)
    ax3.set_title(str(name) + ' Line Chart')

    ax1.hist(df['SUM_VALUE'], color='red', alpha=0.8, rwidth=0.75)
    ax1.set_title(str(name) + ' Histogram')

    ax2.scatter(updateddf2016['Humidex'], updateddf2016['SUM_VALUE'], color='red', alpha=0.8, s=5, label='2016')
    ax2.scatter(updateddf2017['Humidex'], updateddf2017['SUM_VALUE'], color='blue', alpha=0.8, s=5, label='2017')
    ax2.scatter(updateddf2018['Humidex'], updateddf2018['SUM_VALUE'], color='green', alpha=0.8, s=5, label='2018')
    ax2.legend()
    ax2.set_title(str(name) + ' Scatterplot')
def runAR2(data,cut=10):
    # print('             AR')
    X = data.values[:-cut]
    train = X

    test = data[-cut:].tolist()

    model = AR(train)
    model_fit = model.fit()
    window = model_fit.k_ar
    # print('window: ', window)
    coef = model_fit.params

    history = train[len(train) - window:]
    history = [history[i] for i in range(len(history))]
    predictions = list()
    for t in range(len(test)):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        obs = test[t]
        predictions.append(yhat)
        history.append(obs)
        # print('predicted=%f, expected=%f' % (yhat, obs))

    # error = mean_squared_error(test, predictions)
    # print('Test MSE: %.3f' % error)
    # print('sum of predicted: ', sum(predictions))
    # print('sum of test set', sum(test))
    # print('error: ', sum(predictions) / sum(test))

    return predictions, test
def runAR(data):
    # print('             AR')
    train = data.values
    model = AR(train)
    model_fit = model.fit()
    window = model_fit.k_ar
    # print('window: ', window)
    coef = model_fit.params
    new = model_fit.predict(start = len(train), end = len(train)+1)
    # print('PREDICTION: ',new)
    return new
def sorting(dict1, tick=1):
    xx=[]
    yy=[]
    aq = sorted(dict1, key = dict1.get, reverse=True)
    for prop in aq:
        xx.append(prop)
        yy.append(dict1[prop])
    if tick == 1:
        yy = [y for y in yy if y > 0]
    xx = xx[:len(yy)]
    return xx, yy
def doStuff(newdf, dt,color1, color2):

    print(newdf)
    a = newdf.loc[dt].CDD
    print(newdf.loc[dt])

    e_ = 0.05
    e = 1-e_
    ee = 1+e_

    p = {pd.to_datetime(x[0]):[x[-1], x[-9]] for x in newdf.itertuples() if a*e <= x[-1] <= a*ee}
    qq = {pd.to_datetime(x[0]):x[-9] for x in newdf.itertuples() if a*e <= x[-1] <= a*ee}
    print(p)
    k = [x[1] for x in p.values()]
    o = list(p.keys())
    r, z = sorting(qq) #descending order
    z = z[:int(len(z)*0.9)] #values of sums
    r = r[:int(len(r)*0.9)] #datetimes

    plt.scatter([pd.to_datetime(dt)][-2:], newdf.loc[dt].SUM_VALUE, s = 30, alpha = 0.6)
    plt.plot([pd.to_datetime(x.date()) for x in o][-2:], [np.mean(k) for x in k][-2:], color = color1, alpha = 0.8)
    plt.plot([pd.to_datetime(x.date()) for x in r][-2:], [np.mean(z) for x in z][-2:], color = color2, alpha = 0.3)


path = r'C:/Users/J_Ragbeer/PycharmProjects/Metrocentredata/data/'
all_files = glob.glob(os.path.join(path, "*.xlsx"))
names = [i.split('\\')[1].split('(')[0].strip() for i in all_files]
print(names)
weather = weather1()
#weather = weather1().resample('D').sum()
num = 3
# make_charts(names[num],all_files[num], weather)
print(names[num])
df = make_data(all_files[num])

df = df.resample('H').sum()
df['DIFFS'] = pd.Series([df['SUM_VALUE'][x] - df['SUM_VALUE'][x-1] for x in range(len(df))], index = df.index)
newdf = pd.merge(df, weather, left_index=True, right_index=True)


# pickle_in = open("dict1.pickle","rb")
# newdf = pickle.load(pickle_in)
newdf.index = pd.to_datetime([x for x in newdf.index])

def slow_ingest(datee, timestep=3):
    kk = parser.parse(datee) + datetime.timedelta(hours=1)
    t = newdf.loc[:datee] #train data
    rr = newdf.loc[kk:] #dataframe containing next values to load in
    standlist = []
    diffslist = []
    standerror = []
    diffserror = []
    count = 0
    for x in rr.iterrows():
        count = count+1
        kk = parser.parse(datee) + datetime.timedelta(hours=count) #look ahead one hour
        kko = parser.parse(datee) + datetime.timedelta(hours=count+1)
        ww = x[1].to_frame().T
        t = t.append(ww) # attach next row to train data

        preds, obs = runAR2(t.SUM_VALUE, 10)
        preds2, obs2 = runAR2(t.DIFFS, 10)

        standard = np.sqrt(mean_squared_error(obs, preds))
        diffs = np.sqrt(mean_squared_error(obs, np.cumsum([t.SUM_VALUE[-11]+preds2[0]] + preds2[1:])))
        # print('STANDARD: ',standard)
        # print('DIFFS: ',diffs)

        standlist.append(standard)
        diffslist.append(diffs)

        # print(standlist)
        # print(diffslist)

        standerr = standard*100 / np.mean(preds)
        diffserr = diffs * 100 / np.mean(np.cumsum([t.SUM_VALUE[-11]+preds2[0]] + preds2[1:]))
        print('-'*15)
        print(kko)
        standerror.append(standerr)
        diffserror.append(diffserr)
        # print(standerror)
        # print(diffserror)
        newpred = runAR(t.SUM_VALUE)[0]
        print('PREDICTION: {}, ACTUAL: {}'.format(newpred, newdf.loc[str(kko)].SUM_VALUE))
        qt = np.abs(newdf.loc[str(kko)].SUM_VALUE - newpred)
        errorpercent = qt * 100 / newdf.loc[str(kko)].SUM_VALUE

        # print(newpred, t.loc[str(kk)].SUM_VALUE[0])
        # qt = np.abs(t.loc[str(kk)].SUM_VALUE[0] - newpred)
        # errorpercent = qt * 100 / t.loc[str(kk)].SUM_VALUE[0]
        print('ERROR: {:.1f}, ERROR PERCENT: {:.1f}'.format(qt, errorpercent))
        if errorpercent > 10:
            print('*' * 15)
            print("SEND AN EMAIL ALERT")
            print('*' * 15)
        time.sleep(timestep)

        if count == 50:
            break

slow_ingest('2018-07-10',5)

# doStuff(newdf, '2018-07-10', 'orange', 'orange')
# doStuff(newdf, '2018-07-11', 'purple', 'purple')
# doStuff(newdf, '2018-07-12', 'blue', 'blue')
# doStuff(newdf, '2018-07-13', 'red', 'red')
# plt.show()
# df['DIFFS'] = pd.Series([df['SUM_VALUE'][x] - df['SUM_VALUE'][x-1] for x in range(len(df))], index = df.index)
#
# # plt.hist(df['DIFFS'], color='red', alpha=0.8, rwidth=0.75)
# plt.plot(df['DIFFS'], color = 'red')
# preds = runAR2(df['DIFFS'])
#
# preds2 = runAR2(df['SUM_VALUE'])
#
# print('-'*15)
#
# for x in range(len(preds)):
#     print(preds[x], preds2[x], )
#
# print(df['DIFFS'].mean())
#
# plt.show()
