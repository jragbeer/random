import datetime
import pandas as pd
import numpy as np
import time
from dateutil import parser
from os.path import dirname, join
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import pickle
import calendar
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup
from bokeh.layouts import widgetbox, row, column, gridplot, layout
from bokeh.io import curdoc
import glob
import os

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
def make_data(nameOfTable):
    c.execute('SELECT INTERVAL_DTTM,SUM_VALUE FROM {}'.format('"'+nameOfTable+'"'))
    data= c.fetchall()
    df = pd.DataFrame([x for x in data], columns = ['INTERVAL_DTTM','SUM_VALUE'])
    df.set_index('INTERVAL_DTTM',inplace =True)
    df.index = [parser.parse(y.split()[0] + ' ' + y.split()[1].split('.')[0] + ':' + y.split()[1].split('.')[1] + ':' + y.split()[1].split('.')[2] + ' ' + y.split()[2]) for y in df.index]
    df.index = pd.to_datetime(df.index)
    df = df.resample('H').sum()
    df['DIFFS'] = pd.Series([df['SUM_VALUE'][x] - df['SUM_VALUE'][x - 1] for x in range(len(df))], index=df.index)
    newdf = pd.merge(df, weather, left_index=True, right_index=True)
    newdf['tooltip'] = [x.strftime("%Y-%m-%d %H:%M:%S") for x in newdf.index]
    newdf.index = pd.to_datetime([x for x in newdf.index])
    return newdf
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

    # sorts dictionary (dict1) by key and returns the sorted key, value arrays
    # tick is a binary variable that only chooses values that are positive

    # unfinished method (xx doesn't always return right keys
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
    #boundaries for threshold
    e_ = 0.05
    e = 1-e_
    ee = 1+e_

    p = {pd.to_datetime(x[0]):[x[-1], x[-9]] for x in newdf.itertuples() if x[-1]*e <= x[-1] <= x[-1]*ee}
    qq = {pd.to_datetime(x[0]):x[-9] for x in newdf.itertuples() if x[-1]*e <= x[-1] <= x[-1]*ee}
    print(p)
    k = [x[1] for x in p.values()]
    o = list(p.keys())
    r, z = sorting(qq) #descending order
    z = z[:int(len(z)*0.9)] #values of sums
    r = r[:int(len(r)*0.9)] #datetimes

    plt.scatter([pd.to_datetime(dt)][-2:], newdf.loc[dt].SUM_VALUE, s = 30, alpha = 0.6)
    plt.plot([pd.to_datetime(x.date()) for x in o][-2:], [np.mean(k) for x in k][-2:], color = color1, alpha = 0.8)
    plt.plot([pd.to_datetime(x.date()) for x in r][-2:], [np.mean(z) for x in z][-2:], color = color2, alpha = 0.3)
def slow_ingest(datee, timestep=3):

    # datee = date looking to split on - before this is the 'data', after this we're ingesting at a rate of every *timestep* seconds
    # "%Y-%m-%d %H:%M:%S" format

    # timestep = number of seconds to wait to perform 'ingestion'

    # updates the dataframe (newdf) in place. It adds to the existing df 1 row and then performs a AR function, finding the expected value
    # of the next value in the list. Does this every *timestep* seconds.

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
        kk = parser.parse(datee) + datetime.timedelta(hours=count) #look ahead one hour from split point

        ww = x[1].to_frame().T #get the data from
        t = t.append(ww) # attach next row to train data

        ###
        # before this is the ingestion, after is the prediction part
        ###

        kko = parser.parse(datee) + datetime.timedelta(hours=count + 1)  # used to check error of AR compared to actual

        preds, obs = runAR2(t.SUM_VALUE, 10) #run AR with a test and validation set (last ten values)
        preds2, obs2 = runAR2(t.DIFFS, 10) # run AR on the differences between values instead of only the values, split into test/validation

        standard = np.sqrt(mean_squared_error(obs, preds)) #RMSE for the values
        diffs = np.sqrt(mean_squared_error(obs, np.cumsum([t.SUM_VALUE[-11]+preds2[0]] + preds2[1:])))#RMSE for the differences
        # print('STANDARD: ',standard)
        # print('DIFFS: ',diffs)

        standlist.append(standard) #list of running error values
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
        print('PREDICTION: {:.2f}, ACTUAL: {:.2f}'.format(newpred, newdf1.loc[str(kko)].SUM_VALUE))
        qt = np.abs(newdf1.loc[str(kko)].SUM_VALUE - newpred)
        errorpercent = qt * 100 / newdf.loc[str(kko)].SUM_VALUE

        # print(newpred, t.loc[str(kk)].SUM_VALUE[0])
        # qt = np.abs(t.loc[str(kk)].SUM_VALUE[0] - newpred)
        # errorpercent = qt * 100 / t.loc[str(kk)].SUM_VALUE[0]
        print('ERROR: {:.1f}, ERROR PERCENT: {:.1f}'.format(qt, errorpercent))
        #if errorpercent is more that 10 % off, send an alert
        if errorpercent > 10:
            print('*' * 15)
            print("SEND AN EMAIL ALERT")
            print('*' * 15)
        time.sleep(timestep) #sleep for specified time to similate ingestion

        if count == 50:
            break
def doARstuff(orig_df, newdf1, kko, timestep=3):
    t = newdf1
    newpred = runAR(t.SUM_VALUE)[0]
    predictionmessage = 'NEXT STEP PREDICTION: {:.2f}, NEXT STEP ACTUAL: {:.2f}'.format(newpred, orig_df.loc[str(kko)].SUM_VALUE)
    print(predictionmessage)
    qt = np.abs(orig_df.loc[str(kko)].SUM_VALUE - newpred)
    errorpercent = qt * 100 / orig_df.loc[str(kko)].SUM_VALUE
    errormessage = 'ERROR: {:.1f} units, ERROR PERCENT: {:.1f}%'.format(qt, errorpercent)
    print(errormessage)
    #if errorpercent is more that 10 % off, send an alert
    if errorpercent > 10:
        print('*' * 15)
        print("EMAIL ALERT SENT")
        print('*' * 15)
        text = 'The percent error is 10% or higher \n' + errormessage + '\n' + predictionmessage
        html = '<b>The percent error is <i>10%</i> or higher</b><br><br><b>' + errormessage + '</b><br><br><b>' + predictionmessage + '</b>'
        sendemail(text, html)
    return newpred
def ingest(newdf1, dateee,timeee, timestep=3):
    # datee = date looking to split on - before this is the 'data', after this we're ingesting at a rate of every *timestep* seconds
    # "%Y-%m-%d %H:%M:%S" format

    # timestep = number of seconds to wait to perform 'ingestion'

    # updates the dataframe (newdf) in place. It adds to the existing df 1 row and then performs a AR function, finding the expected value
    # of the next value in the list. Does this every *timestep* seconds.
    datee = '{} {}:00:00'.format(dateee, timeee)
    standlist = []
    diffslist = []
    standerror = []
    diffserror = []
    kk = parser.parse(datee) + datetime.timedelta(hours=1)
    t = newdf1.loc[:datee]  # train data
    rr = newdf1.loc[kk:]  # dataframe containing next values to load in
    count = -1
    print(t)
    for x in rr.iterrows():
        count = count + 1
        kk = parser.parse(datee) + datetime.timedelta(hours=count)  # look ahead one hour from split point
        kko = parser.parse(datee) + datetime.timedelta(hours=count+1)
        ww = x[1].to_frame().T  # get the data from
        t = t.append(ww)  # attach next row to train data
        pred = doARstuff(newdf1,t,kko)

        expvalue= make_expected(newdf1, str(kk) ,6)
        baselinevalue = find_baseline(newdf1.loc[kk].Humidex, kk.year)
        print('BASELINE VALUE: {:.2f}'.format(baselinevalue))
        print('EXPECTED VALUE: {:.2f}'.format(expvalue))
        print('*'*5)
        print('REAL VALUE: {:.2f}'.format(newdf1.loc[kk].SUM_VALUE))
        print('TEMP: {:.1f}'.format(newdf1.loc[kk].Humidex))
        print('DATE: ', str(kk)) #print day trying to *predict*
        print('-'*15)
        print('-' * 15)
        print('\n')

        time.sleep(timestep)
def make_expected(origdf, date, tim):

    #makes charts that show for the past *tim* amount of days that are weekdays (or weekends),
    #the averages for temperature and energy useage.

    #origdf = df you're looking at
    #date = date that you're looking back from
    #tim = number of days to look back

    #returns = mean of the list of temperatures matching your query

    df = origdf.copy()
    temps = []
    energy = []
    dates = []
    def doStuffweekday(df, timp):

        curdate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days = timp)
        a = df.loc[curdate]
        #checks if the day number is under 6 (6 = sat, 7 = sunday).
        if (datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days = timp)).isoweekday() < 6:
            energy.append(a.values[8]) # add 'SUM_VALUE' column value to the list
            temps.append(a.values[-3]) # add 'Humidex' column value to the list
            dates.append(curdate) # add the current date being looked at to the list
        else:
            pass
    def doStuffweekend(df, timp):
        curdate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days = timp)
        a = df.loc[curdate]
        if (datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days = timp)).isoweekday() > 5:
            energy.append(a.values[8])
            temps.append(a.values[-3])
            dates.append(curdate)
        else:
            pass

    x = 1 # starting one day in the past, find means
    if datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").isoweekday() < 6:
        while True:
            doStuffweekday(df, x)
            if len(energy) == tim:
                break
            else:
                x+=1
    else:
        while True:
            doStuffweekend(df, x)
            if len(energy) == tim:
                break
            else:
                x+=1
    return np.mean(energy)
def find_baseline(n, year):
    if year == 2016:
        baselineyear = 2016
    elif year == 2017:
        baselineyear = 2016
    elif year == 2018:
        baselineyear = 2017

    u = set(baselinedict[np.ceil(n)][baselineyear] + baselinedict[np.floor(n)][baselineyear])
    kpp = pd.Series([df.loc[x].SUM_VALUE for x in u], index=[x for x in u])
    return kpp.mean()
def sendemail(text, html):
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    curtime = datetime.datetime.now()  # current time and date

    # list of who to send the email to
    TO = ['jragbeer@oxfordproperties.com']
    SUBJECT = 'Error in script'  # subject line of the email

    TEXT = text
    HTML = html

    # Gmail Sign In
    gmail_sender = 'julienwork789@gmail.com'  # senders email
    gmail_passwd = '12fork34'  # senders password

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    part1 = MIMEText(TEXT, 'plain')  # add the 2 parts of the email (one plain text, one html)
    part2 = MIMEText(HTML, 'html')
    msg.attach(part1)  # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part2)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to the GMAIL server
    server.login(gmail_sender, gmail_passwd)  # login to the GMAIL server

    try:
        server.sendmail(gmail_sender, TO, msg.as_string())  # send email
        print(curtime, 'email sent')  # confirm email is sent, and the time
    except Exception as e:
        print(str(e))  # print error if not sent
        print(curtime, 'error sending mail')  # confirm that email wasn't sent

    server.quit()
def download():
    pass
def updateenergytype(attr, old, new):
    global meter
    if str(new) == 'DLCW':
        selectmeter.options = sorted(dlcw)
        meter = dlcw[0]
        selectmeter.value = dlcw[0]
    elif str(new) == 'Electricity':
        selectmeter.options = sorted(electricity)
        meter = electricity[0]
        selectmeter.value = electricity[0]
    elif str(new) == 'Gas':
        selectmeter.options = sorted(gas)
        meter = gas[0]
        selectmeter.value = gas[0]
def updatemeter(attr, old, new):
    idf = make_data(str(new))
    source.data = ColumnDataSource(data={'x': idf.index[-169:], 'y': idf.SUM_VALUE[-169:], 'tooltip': idf.tooltip[-169:]}).data
def updatehour(attr, old, new):
    global hour
    hour = str(new)
def datechanger(attr, old, new):
    global date
    date = str(new)
def updateslider(attr, old, new):
    global ingesttime
    ingesttime = str(new)
def update(attr, old, new):
    layout.children[1] = ingest(df, '2018-04-7 11:00:00')

timee = datetime.datetime.now()
print(timee,'\n')
path = r'xx'
pickle_in1 = open(path+"baselinesdict.pickle","rb")
baselinedict = pickle.load(pickle_in1)

conn = sqlite3.connect(path + 'xx')
c = conn.cursor()
namesReal = ['Concourse Cooling King', 'Concourse Cooling Wellington', 'King Gas', 'King Tower Electricity', 'MCC-KPHA Penthouse', 'MCC-KPHXA Emergency', 'MCC-RCA', 'MCC-RCB', 'MCC-WPHA Penthouse', 'MCC-WPHXA Emergency', 'Mechanical Riser King', 'Mechanical Riser Wellington', 'Power and Light Riser King', 'Power and Light Riser Wellington', 'Retail Bus1', 'Retail Bus2', 'Retail DLCW', 'Retail Electricity', 'Toronto Hydro Main', 'Total DLCW', 'Tower Cooling King', 'Tower Cooling Wellington', 'Towers DLCW', 'Wellington Gas', 'Wellington Tower Electricity']
otherNames = ['ConcourseCooling(MCk_CSM.t)', 'ConcourseCooling(MCw_CSM.t)', 'KingGas(MCk_GU0.t)', 'KingTowerElectricity(MCk_EVM.mx)', 'MCCKPHAPenthouse(MCk_ESB.mc)', 'MCCKPHXAEmergency(MCk_ESB.mc)', 'MCCRCA(MCr_ESB.mc)', 'MCCRCB(MCr_ESB.mc)', 'MCCWPHAPenthouse(MCw_ESB.mc)', 'MCCWPHXAEmergency(MCw_ESB.mc)', 'MechanicalRiser(MCk_ESB.m)', 'MechanicalRiser(MCw_ESB.m)', 'PowerandLightRiser(MCk_ESM.mx)', 'PowerandLightRiser(MCw_ESM.mx)', 'RetailBus1(MCr_ESM.mx)', 'RetailBus2(MCr_ESM.mx)', 'RetailDLCW(MC_DU0.t)', 'RetailElectricity(MCr_EVM.mx)', 'TorontoHydroMain(MC_EU0.mx)', 'TotalDLCW(MC_DV0.t)', 'TowerCooling(MCk_CSM.t)', 'TowerCooling(MCw_CSM.t)', 'TowersDLCW(MC_DU0.t)', 'WellingtonGas(MCw_GU0.t)', 'WellingtonTowerElectricity(MCw_EVM.mx)']

namesDict = {namesReal[x]:otherNames[x] for x in range(len(otherNames))}

weather = weather1()
num = 3
print(namesReal[num],'\n')
df = make_data(namesReal[num])

# bokeh viz

dlcw = ['Concourse Cooling King', 'Concourse Cooling Wellington', 'Retail DLCW', 'Total DLCW', 'Tower Cooling King', 'Tower Cooling Wellington', 'Towers DLCW']
electricity = ['King Tower Electricity', 'MCC-KPHA Penthouse', 'MCC-KPHXA Emergency', 'MCC-RCA', 'MCC-RCB', 'MCC-WPHA Penthouse', 'MCC-WPHXA Emergency', 'Mechanical Riser King', 'Mechanical Riser Wellington', 'Power and Light Riser King', 'Power and Light Riser Wellington', 'Retail Bus1', 'Retail Bus2', 'Retail Electricity', 'Toronto Hydro Main', 'Wellington Tower Electricity']
gas = ['King Gas', 'Wellington Gas']
energytypes = ['DLCW', 'Electricity', 'Gas']
firsthour = 11
hour = 11
firstmeter= electricity[0]
meter = electricity[0]
ingesttime = 5
date = '2018-04-7'

source = ColumnDataSource(data={'x': df.loc[parser.parse(date+' '+str(hour)+':00:00') - datetime.timedelta(hours = 169):date+' '+str(hour)+':00:00'].index, 'y': df['SUM_VALUE'].loc[parser.parse(date+' '+str(hour)+':00:00') - datetime.timedelta(hours = 169):date+' '+str(hour)+':00:00'], 'tooltip': df['tooltip'].loc[parser.parse(date+' '+str(hour)+':00:00') - datetime.timedelta(hours = 169):date+' '+str(hour)+':00:00']})
expvaluesource = ColumnDataSource(data = {})
predvaluesource = ColumnDataSource(data = {})
baselinesource = ColumnDataSource(data = {})

# print(df.loc[parser.parse(date+' '+str(hour)+':00:00') - datetime.timedelta(hours = 169):date+' '+str(hour)+':00:00'].index)
# print(parser.parse(date+' '+str(hour)+':00:00'))


hoverline = HoverTool(tooltips = """ <div> 
             <span style="font-size: 12px; color: #2c2230; font-weight: bold; ">Date/Time: </span>
             <span style="font-size: 12px; color: #966; font-weight: bold; ">@tooltip</span><br>
            <span style="font-size: 12px; color: #2c2230; font-weight: bold; ">Energy Demand:</span>
            <span style="font-size: 12px; color: #966; font-weight: bold; ">@y</span>
            </div>""")

# hoverline = HoverTool(tooltips=[
#     ("Date", "@tooltip"),
#     ("Energy Demand", "@y{(0.0)} units"), ])

p = figure(x_axis_type='datetime', plot_width=1610, plot_height=650,
           tools=[hoverline, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title='Energy Demand', y_axis_label='Energy Demand (units)', x_axis_label='Date/Time')

p.line('x', 'y', source=source, line_width=4, color='gold', legend='Actual', alpha=0.65)
p.circle('x', 'y', source=source, size=4, color='gold', alpha=0.65)

p.background_fill_color = '#2c2230'
p.yaxis.formatter = NumeralTickFormatter(format='0,0')
p.axis.minor_tick_line_alpha = 0
p.axis.axis_line_color = '#E6E6E6'
p.axis.major_tick_in = -1
p.axis.axis_label_text_font_style = 'bold'
p.xaxis.axis_label_text_font_size = '10pt'
p.yaxis.axis_label_text_font_size = '11pt'
p.axis.major_label_text_font_size = '9pt'
p.axis.major_label_text_font_style = 'bold'
p.title.align = 'center'
p.title.text_font_size = '11pt'
p.toolbar.active_scroll = "auto"
p.ygrid.grid_line_alpha = 0.3
p.xgrid.grid_line_alpha = 0.3
p.legend.location = 'bottom_left'
p.legend.click_policy = "hide"

baselinecheckbox = CheckboxGroup(
        labels=["Baseline"], active=[])
expvaluecheckbox = CheckboxGroup(
        labels=["Expected Value"], active=[])
predcheckbox = CheckboxGroup(
        labels=["Next Step Prediction"], active=[])

button = Button(label="Download Data", button_type="success")
button.on_click(download)

buttonRun = Button(label="Run Ingestion", button_type="danger")
buttonRun.on_click(download)

slider = Slider(start=5, end=300, value=5, step=1, title="Ingestion Speed (s)")
slider.on_change('value', updateslider)

select = Select(title='Energy Type:', value=energytypes[1], options=sorted(list(energytypes)))
select.on_change('value', updateenergytype)

selectmeter = Select(title='Meter:', value=electricity[0], options=sorted(electricity))
selectmeter.on_change('value', updatemeter)

selecthour = Select(title='Hour:', value=str(firsthour), options=[str(e) for e in range(24)])
selecthour.on_change('value', updatehour)

datepicker = inputs.DatePicker(title = 'Starting Date',max_date='2018-8-31', min_date='2016-1-6', value = date)
datepicker.on_change('value', datechanger)
div = Div(text = """<p><b>Baseline:</b> Select this if you want to look back at last year and find the average energy comsumption for +/- 1 Degree of the current value (i.e. Avg energy consumption of 27-29 if current is 28)</p><br>
<p><b>Expected Value:</b> Select this if you want to look back at the last 6 types of days (weekday/weekend) and find average of Top 5 for that hour of the day (i.e. 11am) </p><br>
<p><b>Next Step Prediction:</b> Select this if you want to use a regression algorithm to see what a future value will most likely look like </p><br>
<p> <b>Any Questions/Comments?</b><br> Please send a message to the Oxford Data Science / Analytics Team </p>
                        """)
div2 = Div(text="<img src='xx'>",width=280, height=100)
r = widgetbox(select, selectmeter, selecthour, datepicker,baselinecheckbox, expvaluecheckbox, predcheckbox,slider,button,buttonRun,div,div2, width = 280)

pp = row([r, p])
curdoc().add_root(pp)
show(pp)

# ingest(df, date, hour, ingesttime)


