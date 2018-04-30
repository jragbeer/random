#Displays any company's closing stock price over the first 4 months of 2018
#Julien Ragbeer
#Python Data Visualization

import quandl
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def graph_data(stock):
    print("\nWorking...")
    fig = plt.figure()
    plot1 = plt.subplot2grid((1, 1), (0, 0))
#fetching data
    quandl.ApiConfig.api_key = "DT9n9tViZmzt2cpgfnsz"
    param = "WIKI/"+stock

    data = quandl.get([""+param+".1",""+param+".2",""+param+".3",""+param+".4"] , returns="numpy", start_date="2018-01-01", end_date="2018-04-30")
#unpacking tuple
    dates = []
    openp=[]
    highp=[]
    lowp=[]
    closep=[]

    for row in data:
        date = (row[0])
        open = (row[1])
        high = (row[2])
        low = (row[3])
        close = (row[4])

        dates.append(date)
        openp.append(open)
        highp.append(high)
        lowp.append(low)
        closep.append(close)

#plotting the data, fill_between for area under curve, line and empty sets for the legend
    plot1.plot_date(dates, closep, '-', label='Price')
    plot1.plot([], [], linewidth=5, label='Up', color='g', alpha=0.25)
    plot1.plot([], [], linewidth=5, label='Down', color='r', alpha=0.25)

    plot1.fill_between(dates, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.25)
    
    plot1.fill_between(dates, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.25)
    for label in plot1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plot1.grid(True, color='k', linewidth=0.1, linestyle='-')
#setting names and legend
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title(stock)
    plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.legend()
    plt.show()
#Asks user to enter a stock to check
user_input = input("Enter a stock symbol: \n\n")
graph_data(user_input.upper())