import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet
import matplotlib.ticker as ticker

def viz():
    style.use('seaborn-darkgrid')
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    fig1 = plt.figure()
    ax5 = fig1.add_subplot(221)
    ax6 = fig1.add_subplot(222)
    ax7 = fig1.add_subplot(223)
    ax8 = fig1.add_subplot(224)
    fig2 = plt.figure()
    ax9 = fig2.add_subplot(221)
    ax10 = fig2.add_subplot(222)
    ax11 = fig2.add_subplot(223)
    ax12 = fig2.add_subplot(224)
    
    bx1 = ax1.twinx()
    bx2 = ax2.twinx()
    bx3 = ax3.twinx()
    bx4 = ax4.twinx()
    bx5 = ax5.twinx()
    bx6 = ax6.twinx()
    bx7 = ax7.twinx()
    bx8 = ax8.twinx()
    bx9 = ax9.twinx()
    bx10 = ax10.twinx()
    bx11 = ax11.twinx()
    bx12 = ax12.twinx()

    df.loc[datetime.datetime(2018, 5, 28, 10):datetime.datetime(2018, 7, 16, 22)].plot(ax=ax1, lw=3)
    df.loc[datetime.datetime(2018, 5, 30, 10):datetime.datetime(2018, 5, 30, 22)].plot(ax=ax2, lw=3)
    df.loc[datetime.datetime(2018, 5, 31, 10):datetime.datetime(2018, 5, 31, 22)].plot(ax=ax3, lw=3)
    df.loc[datetime.datetime(2018, 6, 18, 9):datetime.datetime(2018, 6, 18, 22)].plot(ax=ax4, lw=3)
    df.loc[datetime.datetime(2018, 6, 29, 10):datetime.datetime(2018, 6, 29, 22)].plot(ax=ax5, lw=3)
    df.loc[datetime.datetime(2018, 6, 30, 10):datetime.datetime(2018, 6, 30, 22)].plot(ax=ax6, lw=3)
    df.loc[datetime.datetime(2018, 7, 2, 10):datetime.datetime(2018, 7, 2, 22)].plot(ax=ax7, lw=3)
    df.loc[datetime.datetime(2018, 7, 3, 10):datetime.datetime(2018, 7, 3, 22)].plot(ax=ax8, lw=3)
    df.loc[datetime.datetime(2018, 7, 4, 10):datetime.datetime(2018, 7, 4, 22)].plot(ax=ax9, lw=3)
    df.loc[datetime.datetime(2018, 7, 5, 10):datetime.datetime(2018, 7, 5, 22)].plot(ax=ax10, lw=3)
    df.loc[datetime.datetime(2018, 7, 9, 10):datetime.datetime(2018, 7, 9, 22)].plot(ax=ax11, lw=3)
    df.loc[datetime.datetime(2018, 7, 16, 10):datetime.datetime(2018, 7, 16, 22)].plot(ax=ax12, lw=3)

    weather['Humidex'].loc[datetime.datetime(2018, 5, 30, 10):datetime.datetime(2018, 7, 16, 22)].plot(ax=bx1, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 5, 30, 10):datetime.datetime(2018, 5, 30, 22)].plot(ax=bx2, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 5, 31, 10):datetime.datetime(2018, 5, 31, 22)].plot(ax=bx3, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 6, 18, 9):datetime.datetime(2018, 6, 18, 22)].plot(ax=bx4, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 6, 29, 10):datetime.datetime(2018, 6, 29, 22)].plot(ax=bx5, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 6, 30, 10):datetime.datetime(2018, 6, 30, 22)].plot(ax=bx6, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 2, 10):datetime.datetime(2018, 7, 2, 22)].plot(ax=bx7, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 3, 10):datetime.datetime(2018, 7, 3, 22)].plot(ax=bx8, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 4, 10):datetime.datetime(2018, 7, 4, 22)].plot(ax=bx9, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 5, 10):datetime.datetime(2018, 7, 5, 22)].plot(ax=bx10, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 9, 10):datetime.datetime(2018, 7, 9, 22)].plot(ax=bx11, lw=1, color='red', alpha = 0.095)
    weather['Humidex'].loc[datetime.datetime(2018, 7, 16, 10):datetime.datetime(2018, 7, 16, 22)].plot(ax=bx12, lw=1, color='red', alpha = 0.095)

    ylimm = [4000, 10000]
    ax1.set(ylim=ylimm, ylabel='Energy (KW)', title='All Dates')
    ax2.set(ylim=ylimm, title='May 30, 2018 - Hours: 10-9 - Max Humidex: 31.0')
    ax3.set(ylim=ylimm, title='May 31, 2018 - Hours: 10-9 - Max Humidex: 35.8', ylabel='Energy (KWh)')
    ax4.set(ylim=ylimm, title='June 18, 2018 - Hours: 10-9 - Max Humidex: 40.5')
    ax5.set(ylim=ylimm, title='June 29, 2018 - Hours: 10-9 - Max Humidex: 33.4', ylabel='Energy (KWh)')
    ax6.set(ylim=ylimm, title='June 30, 2018 - Hours: 9:30-9 - Max Humidex: 41.5')
    ax7.set(ylim=ylimm, title='July 2, 2018 - Hours: 11-6 - Max Humidex: 40.2', ylabel='Energy (KWh)')
    ax8.set(ylim=ylimm, title='July 3, 2018 - Hours: 10-9 - Max Humidex: 31.5')
    ax9.set(ylim=ylimm, title='July 4, 2018 - Hours: 10-9 - Max Humidex: 35.6', ylabel='Energy (KWh)')
    ax10.set(ylim=ylimm, title='July 5, 2018 - Hours: 10-9 - Max Humidex: 39.6')
    ax11.set(ylim=ylimm, title='July 9, 2018 - Hours: 10-9 - Max Humidex: 33.2', ylabel='Energy (KWh)')
    ax12.set(ylim=ylimm, title='July 16, 2018 - Hours: 10-9 - Max Humidex: 36.7')
    ylimm2=[24, 45]
    bx1.set(ylim = ylimm2)
    bx2.set(ylim=ylimm2, ylabel = 'Humidex (C)')
    bx3.set(ylim=ylimm2)
    bx4.set(ylim=ylimm2, ylabel = 'Humidex (C)')
    bx5.set(ylim=ylimm2)
    bx6.set(ylim=ylimm2, ylabel = 'Humidex (C)')
    bx7.set(ylim=ylimm2)
    bx8.set(ylim=ylimm2, ylabel = 'Humidex (C)')
    bx9.set(ylim=ylimm2)
    bx10.set(ylim=ylimm2, ylabel = 'Humidex (C)')
    bx11.set(ylim=ylimm2)
    bx12.set(ylim=ylimm2, ylabel = 'Humidex (C)')



    ax1.axvspan(datetime.datetime(2018, 6, 28, 10), datetime.datetime(2018, 7, 5, 22), facecolor='y', alpha=0.195)
    ax1.axvspan(datetime.datetime(2018, 6, 16, 10), datetime.datetime(2018, 6,18, 22), facecolor='y', alpha=0.195)
    ax1.axvspan(datetime.datetime(2018, 5, 28, 10), datetime.datetime(2018, 6, 1, 22), facecolor='y', alpha=0.195)

    ax10.axvspan(datetime.datetime(2018, 7, 5, 15), datetime.datetime(2018, 7, 5, 16), facecolor='r', alpha=0.095)
    ax9.axvspan(datetime.datetime(2018, 7, 4, 18), datetime.datetime(2018, 7, 4, 19), facecolor='r', alpha=0.095)
    ax8.axvspan(datetime.datetime(2018, 7, 3, 18), datetime.datetime(2018, 7, 3, 19), facecolor='r', alpha=0.095)
    ax12.axvspan(datetime.datetime(2018, 7, 16, 11), datetime.datetime(2018, 7, 16, 12), facecolor='r', alpha=0.095)
    ax4.axvspan(datetime.datetime(2018, 6, 18, 9), datetime.datetime(2018, 6, 18, 10), facecolor='r', alpha=0.095)
    ax5.axvspan(datetime.datetime(2018, 6, 29, 16), datetime.datetime(2018, 6, 29, 17), facecolor='r', alpha=0.095)
    ax11.axvspan(datetime.datetime(2018, 7, 9, 17), datetime.datetime(2018, 7, 9, 18), facecolor='r', alpha=0.095)

    # ax1.axvspan(datetime.datetime(2018, 7, 5, 15), datetime.datetime(2018, 7, 5, 16), facecolor='r', alpha=0.095)
    # ax1.axvspan(datetime.datetime(2018, 7, 5, 15), datetime.datetime(2018, 7, 5, 16), facecolor='r', alpha=0.095)
    df2 = pd.DataFrame(data={'values': smallavgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 5, 30, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 5, 30, 22)), freq='H'))
    df2.plot(ax=ax2, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df3 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 5, 31, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 5, 31, 22)), freq='H'))
    df3.plot(ax=ax3, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df4 = pd.DataFrame(data={'values': avgg[9:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 6, 18, 9)),
                                           end=pd.to_datetime(datetime.datetime(2018, 6, 18, 22)), freq='H'))
    df4.plot(ax=ax4, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df5 = pd.DataFrame(data={'values': smallavgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 6, 29, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 6, 29, 22)), freq='H'))
    df5.plot(ax=ax5, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df6 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 6, 30, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 6, 30, 22)), freq='H'))
    df6.plot(ax=ax6, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df7 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 2, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 2, 22)), freq='H'))
    df7.plot(ax=ax7, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df8 = pd.DataFrame(data={'values': smallavgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 3, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 3, 22)), freq='H'))
    df8.plot(ax=ax8, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df9 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 4, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 4, 22)), freq='H'))
    df9.plot(ax=ax9, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df10 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 5, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 5, 22)), freq='H'))
    df10.plot(ax=ax10, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df11 = pd.DataFrame(data={'values': smallavgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 9, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 9, 22)), freq='H'))
    df11.plot(ax=ax11, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])
    df12 = pd.DataFrame(data={'values': avgg[10:23]},
                       index=pd.date_range(start=pd.to_datetime(datetime.datetime(2018, 7, 16, 10)),
                                           end=pd.to_datetime(datetime.datetime(2018, 7, 16, 22)), freq='H'))
    df12.plot(ax=ax12, color='#ea5d0b', alpha=0.5, legend=False, dashes=[5, 3])

    ax1.xaxis.grid(False)
    ax2.xaxis.grid(False)
    ax3.xaxis.grid(False)
    ax4.xaxis.grid(False)
    ax5.xaxis.grid(False)
    ax6.xaxis.grid(False)
    ax7.xaxis.grid(False)
    ax8.xaxis.grid(False)
    ax9.xaxis.grid(False)
    ax10.xaxis.grid(False)
    ax11.xaxis.grid(False)
    ax12.xaxis.grid(False)

    bx1.yaxis.grid(False)
    bx2.yaxis.grid(False)
    bx3.yaxis.grid(False)
    bx4.yaxis.grid(False)
    bx5.yaxis.grid(False)
    bx6.yaxis.grid(False)
    bx7.yaxis.grid(False)
    bx8.yaxis.grid(False)
    bx9.yaxis.grid(False)
    bx10.yaxis.grid(False)
    bx11.yaxis.grid(False)
    bx12.yaxis.grid(False)
def hmdxx(x, y):
    return x+(0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+y))))-10))
def find_mean(tt):
    newnew = pd.DataFrame(weather.groupby(['Year', 'Month', 'Day']).aggregate({'Humidex': 'max'}))
    if tt == 34:
        newnew = newnew[newnew['Humidex'] >= tt] #filter by days that have maximum temp above/equal to 30
    else:
        newnew = newnew[newnew['Humidex'] >= 31]  # filter by days that have maximum temp above/equal to 30
        newnew = newnew[newnew['Humidex'] < 34]
    ww = list()
    for x in newnew.itertuples():
        a,b,c = x[0]
        ww.append(pd.to_datetime(datetime.datetime(a,b,c)))
    maindays = [datetime.datetime(2018, 5, 30), datetime.datetime(2018, 5, 31),datetime.datetime(2018, 6, 18),datetime.datetime(2018, 6, 29),datetime.datetime(2018, 6, 30),
    datetime.datetime(2018, 7, 2), datetime.datetime(2018, 7, 3),datetime.datetime(2018, 7, 4),datetime.datetime(2018, 7, 5),datetime.datetime(2018, 7, 9),datetime.datetime(2018, 7, 16)]

    newww = np.array(ww)
    print('Number of days of 30+ degree days: {}\n'.format(len(newww)))
    newww = [x for x in newww if x not in maindays+[datetime.datetime(2018, 7, 23)]]
    #for each day in filtered days, attach a row of energy for that day. Then find the mean (for each hour) of all of those days above 30
    energymatrix = []
    for y in newww:
        eachday = []
        for x in df.itertuples():
            if y.year == x[0].year and y.month == x[0].month and y.day == x[0].day:
                eachday.append(x[1])
        energymatrix.append(eachday)
    energymatrix = np.array(energymatrix)
    fig2mean = energymatrix.mean(axis = 0)
    return fig2mean
def calccost(gapm,cc = 20000):
    # calculate cost of global adjustment fee
    gapm = np.round(gapm)
    b = (cc/1000)/103196.00
    cost = gapm*b
    return cost
def clean_energy(df):
    df.index = pd.to_datetime(df.index)
    try:
        df['Energy (Kwh)'] = [float(x) for x in df['Energy (Kwh)']]
    except:
        df['Energy (Kwh)'] = (df['Energy (Kwh)'].str.split()).apply(lambda x: float(x[0].replace(',', '')))
    return df
def clean_weather(weather):
    weather.index = pd.to_datetime(weather.index)
    weather.fillna(method='ffill', inplace = True)
    weather['Humidex'] = pd.Series([hmdxx(x[5],x[7]) for x in weather.itertuples()], index = weather.index)
    weather['Hour'] = pd.Series([int(x[0].hour) for x in weather.itertuples()], index = weather.index)
    weather['hr_sin'] = np.sin(weather['Hour'] * (2. * np.pi / 24))
    weather['hr_cos'] = np.cos(weather['Hour'] * (2. * np.pi / 24))
    weather['mnth_sin'] = np.sin((weather['Month']- 1) * (2. * np.pi / 12))
    weather['mnth_cos'] = np.cos((weather['Month'] - 1) * (2. * np.pi / 12))
    weather['Temp'] = weather['Temp (°C)']
    weather['Dew Point Temp'] = weather['Dew Point Temp (°C)']
    weather.drop(['Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag', 'Wind Spd (km/h)',
           'Wind Spd Flag', 'Visibility (km)', 'Visibility Flag','Temp Flag', 'Dew Point Temp Flag',
           'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx Flag', 'Wind Chill', 'Rel Hum (%)','Hmdx','Dew Point Temp',
           'Wind Chill Flag', 'Weather','Temp (°C)','Dew Point Temp (°C)'],1,inplace = True)
    return weather
def runLR(qq, data):
    avg = []
    for w in range(qq):
        #X = np.array(data.drop(['Energy (Kwh)', 'Month', 'Year', 'Day', 'Time', 'Hour'], 1))
        X = np.array(data.drop(['Energy (Kwh)', 'Month', 'Year', 'Day','Time','Hour', 'mnth_sin', 'mnth_cos'],1))
        y = np.array(data['Energy (Kwh)'])

        X = preprocessing.scale(X)

        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)
        clf = LinearRegression(n_jobs=-1)
        clf.fit(X_train, y_train)

        accuracy = clf.score(X_test, y_test)
        avg.append(accuracy)
        # print(accuracy)
        values = clf.predict(X)

    return avg, values
rollingpp = '1144.5	1208.8	1096.1	1029.4	821.1	1099.2	914.9	1023.3 786.8	796.3	962.8	937.8'
rollingpp = rollingpp.split()
rollingpp = [float(x) for x in rollingpp]

df = pd.read_csv('energysummer2016.csv', skiprows=2, names = ['Date', 'Energy (Kwh)'], index_col='Date')
df1 = pd.read_csv('energysummer2017.csv', skiprows=2, names = ['Date', 'Energy (Kwh)'], index_col='Date')

df = clean_energy(df)
df1 = clean_energy(df1)
energydf = pd.concat([df,df1])

weather1 = pd.read_csv('torontoweathermay2016.csv', skiprows = 15, index_col='Date/Time')
weather2 = pd.read_csv('torontoweatherjune2016.csv', skiprows = 15, index_col='Date/Time')
weather3 = pd.read_csv('torontoweatherjuly2016.csv', skiprows = 15, index_col='Date/Time')
weather4 = pd.read_csv('torontoweatheraugust2016.csv', skiprows = 15, index_col='Date/Time')
weather5 = pd.read_csv('torontoweatherseptember2016.csv', skiprows = 15, index_col='Date/Time')
weather6 = pd.read_csv('torontoweathermay2017.csv', skiprows = 15, index_col='Date/Time')
weather7 = pd.read_csv('torontoweatherjune2017.csv', skiprows = 15, index_col='Date/Time')
weather8 = pd.read_csv('torontoweatherjuly2017.csv', skiprows = 15, index_col='Date/Time')
weather9 = pd.read_csv('torontoweatheraugust2017.csv', skiprows = 15, index_col='Date/Time')
weather10 = pd.read_csv('torontoweatherseptember2017.csv', skiprows = 15, index_col='Date/Time')

for x in [weather1, weather2, weather3, weather4, weather5, weather6, weather7, weather8, weather9, weather10]:
    x = clean_weather(x)
weatherdf = pd.concat([weather1, weather2, weather3, weather4, weather5, weather6, weather7, weather8, weather9, weather10])

data = pd.merge(weatherdf, energydf, how='inner', left_index = True, right_index = True)

avg1, val1 = runLR(10000, data)

print('LR:',np.mean(avg1))
print(data.columns)
plt.plot(data.index, data['Energy (Kwh)'], color='r', label = 'Actual')
# plt.plot(data['Date/Time'].values, values1, color='b', label = 'Predicted')
plt.plot(data.index, val1, color='g', label = 'Predicted')
plt.legend()
plt.ylabel('Units of Energy')
plt.xlabel('Date')
plt.title('Regression - Property1 Hourly')
plt.show()

# avgg = find_mean(34)
# smallavgg = find_mean(30)
# viz()
# xxx = pd.DataFrame(weather.groupby(['Year', 'Month', 'Day']).aggregate({'Humidex': ['mean', 'max']}))
# # xxx.to_csv('newnew111.csv')
# print('For days with Max Humidex under 34, an average was used that finds the mean values of days where the Max Humidex is between 31 and 34, and where no email was sent')
# print('\nFor days with Max Humidex over 34, a different average was used. This one looks for days where Max Humidex is above 34, but where no email was sent')
#
# Prop1demand= []
# Prop1demand.append(df.loc[datetime.datetime(2018,7,5,15),:]['Energy (Kwh)'])
# Prop1demand.append(df.loc[datetime.datetime(2018,7,4,18),:]['Energy (Kwh)'])
# Prop1demand.append(df.loc[datetime.datetime(2018,7,3,18),:]['Energy (Kwh)'])
# Prop1demand.append(df.loc[datetime.datetime(2018,7,15,17),:]['Energy (Kwh)'])
# Prop1demand.append(df.loc[datetime.datetime(2018,7,16,11),:]['Energy (Kwh)'])
# print('\nTotal MW for the 5 MAIN hours: {:.2f}\n'.format(np.sum(Prop1demand)))
# avgMW = smallavgg[19]+df.loc[datetime.datetime(2018,7,15,17),:]['Energy (Kwh)']+avgg[11]+ avgg[19]+avgg[15]
# print('Total MW for the 5 hours if AVG consumption was used: {:.2f}\n'.format(avgMW))
# print('Prop1 has used 0.23% less energy than average during the 5 peak hours')
# xx = calccost(np.mean(rollingpp)*1000000, np.sum(Prop1demand))
# yy = calccost(np.mean(rollingpp)*1000000, np.sum(avgMW))
# print('\nTherefore Prop1 would pay an average of ${:2f} less per month because of load-shedding efforts'.format(yy-xx))
# plt.show()