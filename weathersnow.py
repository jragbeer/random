import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import datetime
import urllib
import bs4 as bs
import glob
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

today= pd.to_datetime(datetime.datetime.now())
print('{}\nTODAY \tDay: {}, Month: {}, Year: {}\n'.format(today, today.day, today.month, today.year))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

fig2 = plt.figure()
ax12 = fig2.add_subplot(121)
ax22 = fig2.add_subplot(122)

def pull_data():
    graphsource = urllib.request.urlopen('https://weather.com/en-CA/weather/hourbyhour/l/CAXX0504:1:CA').read()
    soup = bs.BeautifulSoup(graphsource,'html.parser') #actual and predicted data
    timee=[]
    temp=[]
    feels = []
    humidity=[]
    table = soup.find_all('tr')
    for x in table:
        for y in x.find_all('td'):
            if y.get('headers') == ['time']:
                timee.append(y.text)
            if y.get('headers') == ['temp']:
                temp.append(y.text)
            if y.get('headers') == ['feels']:
                feels.append(y.text)
            if y.get('headers') == ['humidity']:
                humidity.append(y.text)

    timee= [int(x.replace('\n','').split(':')[0]) for x in timee]
    temp = [int(x.split('°')[0]) for x in temp]
    feels = [int(x.split('°')[0]) for x in feels]
    humidity = [x.split('%')[0] for x in humidity]
    for x in range(len(feels)):
        print(timee[x],temp[x],feels[x],humidity[x])

def make_wdata(p=1):
    if p == 1:
        path = r'C:/Users/Julien/PycharmProjects/peaktracker/data/Weather Data/Toronto Weather 2/'
    else:
        path = r'C:/Users/Julien/PycharmProjects/peaktracker/data/Weather Data/Mississauga Weather/'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f,encoding='utf-8', skiprows=24) for f in all_files)
    Wdata = pd.concat(df_from_each_file, ignore_index=True)
    Wdata = Wdata[['Year','Day','Month','Date/Time','Total Snow (cm)']]
    Wdata.fillna(method='ffill', inplace =True)
    Wdata.fillna(method='bfill', inplace =True)
    return Wdata

def newfunc(lol):
    minorLocator = MultipleLocator(5)
    data = lol.copy()
    #applying a mask that will show only days where it snowed
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    data = data[data['Total Snow (cm)']>0.01]
    period0 = [datetime.datetime(2013, 9, 1), datetime.datetime(2014, 5, 30)]
    period1 = [datetime.datetime(2014,9,1), datetime.datetime(2015,5,30)]
    period2 = [datetime.datetime(2015,9,1), datetime.datetime(2016 ,5,30)]
    period3 = [datetime.datetime(2016,9,1), datetime.datetime(2017,5,30)]
    period4 = [datetime.datetime(2017,9,1), datetime.datetime(2018,5,30)]

    print('Total number of days it snowed the dataset: ', len(data))  # number of days it snowed
    a = pd.DataFrame(data = data.groupby('Month')['Year'].count())
    print('\n\nAverage number of days of snowfall per year for each month: \n')
    ax12.bar(range(1,8),[a['Year'].loc[10]/5,a['Year'].loc[11]/5,a['Year'].loc[12]/5,a['Year'].loc[1]/5,a['Year'].loc[2]/5,a['Year'].loc[3]/5,a['Year'].loc[4]/5], color = 'm', alpha = 0.65)
    ax12.set_title('Average Number of Days of Snowfall per Year')
    ax12.set_ylabel('Average Number of Days of Snowfall')
    ax12.set_xlabel('Months')
    ax12.set_xticklabels([' ','October', 'November', 'December', 'January', 'February', 'March', 'April'])
    ax12.tick_params(axis='y', which='minor', bottom='off')
    print(a/5)
    b = data.groupby('Month').sum()
    print('\n\nAverage snowfall per year for each month: \n')
    ax22.bar(range(1,8),[b['Total Snow (cm)'].loc[10]/5,b['Total Snow (cm)'].loc[11]/5,b['Total Snow (cm)'].loc[12]/5,b['Total Snow (cm)'].loc[1]/5,b['Total Snow (cm)'].loc[2]/5,b['Total Snow (cm)'].loc[3]/5,b['Total Snow (cm)'].loc[4]/5],alpha = 0.69,  color = 'c')
    ax22.set_xlabel('Month')
    ax22.set_title('Average Snowfall per Year')
    ax22.set_ylabel('Average Snowfall per Month (cm)')
    ax22.set_xticklabels([' ','October', 'November', 'December','January','February','March','April'])
    ax22.tick_params(axis='y', which='minor', bottom='off')
    print(b/5)

    print('\nSeasonal Stats (per winter): \n')

    data0 = data[data['Date/Time'] < period0[1]]
    data0 = data0[data0['Date/Time'] > period0[0]]
    print('2013-2014 Winter: Days of snowfall: {}, Total CM of snow: {}'.format(len(data0),np.ceil(data0['Total Snow (cm)'].sum())))

    data1 = data[data['Date/Time'] < period1[1]]
    data1 = data1[data1['Date/Time'] > period1[0]]
    print('\n2014-2015 Winter: Days of snowfall: {}, Total CM of snow: {}'.format(len(data1),np.ceil(data1['Total Snow (cm)'].sum())))

    data2 = data[data['Date/Time'] < period2[1]]
    data2 = data2[data2['Date/Time'] > period2[0]]
    print('\n2015-2016 Winter: Days of snowfall: {}, Total CM of snow: {}'.format(len(data2),np.ceil(data2['Total Snow (cm)'].sum())))

    data3 = data[data['Date/Time'] < period3[1]]
    data3 = data3[data3['Date/Time'] > period3[0]]
    print('\n2016-2017 Winter: Days of snowfall: {}, Total CM of snow: {}'.format(len(data3),np.ceil(data3['Total Snow (cm)'].sum())))

    data4 = data[data['Date/Time'] < period4[1]]
    data4 = data4[data4['Date/Time'] > period4[0]]
    print('\n2017-2018 Winter: Days of snowfall: {}, Total CM of snow: {}'.format(len(data4),np.ceil(data4['Total Snow (cm)'].sum())))

pull_data()
data = make_wdata()

newfunc(data)

#the data starts on line 163
data = data[163:]
data2 = data[['Date/Time','Total Snow (cm)']]
print('\nTotal number of days in the dataset: \n',len(data)) #number of entries
print(data['Total Snow (cm)'].describe())

data2.plot(ax=ax1,alpha = 0.9)
ax1.set_ylabel('Total Snowfall (cm)')
ax1.set_xlabel('Day Number of study')

data2.hist(ax=ax2,bins = [x for x in range(17)], color = 'blue', width = 0.6, alpha = 0.8)
ax2.set_xlabel('Centimeters of snow')
ax2.set_ylabel('Number of Days')
plt.show()
# data.to_csv('DownsviewSnowData.csv', index = 0)

