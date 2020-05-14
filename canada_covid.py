import numpy as np
from collections import Counter
import pandas as pd
import pickle
import re
from itertools import chain
import webbrowser
import sys
import os
import copy
import yfinance as yf
from pprint import pprint
from dateutil import parser
import sqlite3
import datetime
import pymongo
import datetime
import bokeh
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet
from bokeh.models.widgets import StringFormatter, TableColumn, NumberFormatter, Button, HTMLTemplateFormatter
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
from bokeh.palettes import Category20_20
from bokeh import events
from sqlalchemy import create_engine
import pymysql
import traceback
from pytz import timezone
from tqdm import tqdm
import holidays
import inspect
from pandas.tseries.offsets import BDay
import colorcet as cc
import time
import requests

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'COVID-19 in Canada'


def update_metric(attr, old, new):
    if new.replace(" ", "_") in data.columns:
        p = data[new.replace(" ", "_")]
    else:
        p = data['Adjusted_Deaths']
    mean_line.text=wrap_in_paragraphs(f"Average Deaths per year: {int(np.nanmean(p))}", 'firebrick', 5)
    source.data = {'x': data['Season'], 'info':data['Strain'], 'deaths': p, 'pop': data['Pop']}

def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True) #prevent numpy exponential notation on print

path = os.getcwd().replace("\\", "/") + "/data/"
today = datetime.date.today()
day_num = int(today.strftime('%j'))
# number of days from October 1 to December 31 (first part of flu season)
season_length = 92
# canada population for half-point of 2020 according to worldometer.
canada_population = 37742154

# current coronavirus deaths, canada
total_corona_deaths = pd.read_html(requests.get("https://www.worldometers.info/coronavirus/", headers=header).text)[0]
total_corona_deaths.columns = [x.replace(',', "").replace(' ', "").lower() for x in total_corona_deaths.columns]
total_corona_deaths.set_index('countryother', inplace=True)
total_canadian_deaths = total_corona_deaths.loc['Canada']['totaldeaths']

# data from research paper
df = pd.read_csv(path + 'covid_data.csv', engine='python', usecols=[x for x in range(0, 7) if x not in [4]], skipfooter=3)
df.columns = ['Season', "Strain", "Deaths", "Deaths_Range", "Hospital_Admissions", "Admissions_Range"]
df.fillna(0, inplace=True)
for each in ["Deaths",  "Hospital_Admissions", ]:
    df[each] = [int(str(x).replace(",", "")) for x in df[each]]
for each in ["Deaths_Range", "Admissions_Range"]:
    low = []
    high = []
    for i in df[each]:
        try:
            a = re.findall(r"\d{1,2},?\d+", i)
        except:
            a = ["0","0"]
        b = [int(x.replace(',', "")) for x in a]
        low.append(b[0])
        high.append(b[1])
    df[f"{each}_Low"] = low
    df[f"{each}_High"] = high
df.drop(columns=["Deaths_Range", "Admissions_Range"], inplace=True)
df = df[df['Deaths'] > 1000]
df['Season_Ending'] = [x[:2] + x[-2:] for x in df['Season']]
df['Season_Ending'].replace("1900", "2000", inplace=True)
df['Curr_Deaths'] = [np.around(each*(day_num/(season_length+day_num))) for each in df['Deaths']]

# population data from wikipedia
wiki_population_tables = pd.read_html("https://en.wikipedia.org/wiki/Population_of_Canada")
population = wiki_population_tables[8] # current time period's population chart
population.columns = ['Year', "Pop", "Change"]
population = population.iloc[:-1, :]
population = population[['Year', "Pop"]]

# join data sets
data = df.merge(population, left_on='Season_Ending', right_on='Year')
data['Pop']= data['Pop'].astype(int)
data['Pop_multiplier'] = 1+(canada_population-data['Pop'])/data['Pop']
data['Adjusted_Deaths'] = data['Deaths'] * data['Pop_multiplier']

data.columns = [x.replace("_Range", "") for x in data.columns]
data['Adjusted_Deaths_Low'] = data['Deaths_Low'] * data['Pop_multiplier']
data['Adjusted_Deaths_High'] = data['Deaths_High'] * data['Pop_multiplier']
metrics = ["Deaths", "Deaths Low", "Deaths High", "Adjusted Deaths", "Adjusted Deaths High","Adjusted Deaths Low",]
select_metric = Select(title='Metric:', value=metrics[0], options=sorted(metrics))
select_metric.on_change('value', update_metric)

p = figure(plot_width=800, plot_height=600, x_range = np.asarray(data['Season']).tolist() + ['2019/20'],
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Season", y_axis_label="Deaths", toolbar_location="right", title= 'COVID-19 vs. Past Influenzas in Canada')
# HOVERTOOLS
p.add_tools(HoverTool(tooltips=[
    ("Strain", "@info"),("Deaths", "@deaths{(0,0)}"),("Population", "@pop{(0,0)}"),]))
# MEAN LINE SPAN
p.add_layout(Span(location=np.nanmean(data['Deaths']), dimension='width', line_color='firebrick', line_width=3, line_alpha= 0.43))

source = ColumnDataSource(data={'x': data['Season'], 'info':data['Strain'], 'deaths': data['Deaths'], 'pop': data['Pop']})
p.line(x="x", y='deaths', source=source, line_width=4, line_dash='dotted', alpha = 0.3 )
p.circle(x="x", y='deaths', source=source, size = 12)

source2020 = ColumnDataSource(data={'x': ['2019/20'], 'deaths': [total_canadian_deaths], "info": ['A/Wuhan/2019'],
                                    'pop': [canada_population]})
p.circle(x='x', y='deaths', source=source2020, color='forestgreen', size = 20)

text="""- The mean line does not include data from 2019/20.<br>
- Adjusted in the selector means population normalized.<br><br>
Sources:<br><br>
Historical Death Data: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3842334/">Research Paper on NIH</a><br><br>
Population: <a href="https://en.wikipedia.org/wiki/Population_of_Canada">Wikipedia</a><br><br>
Current Canadian deaths: Live from <a href="https://www.worldometers.info/coronavirus/">Worldometer</a>.<br>
"""
div = Div(text=wrap_in_paragraphs(text, "Dimgrey", 3))
mean_line = Div(text = wrap_in_paragraphs(f"Average Deaths per year: {int(np.nanmean(data['Deaths']))}", 'firebrick', 5))

# pretty up the dashboard
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
p.xaxis.major_label_orientation = np.pi/4
p.y_range.start = 0
p.axis.minor_tick_line_alpha = 0
p.axis.major_tick_in = -1
p.yaxis.axis_label_text_font_size = "13pt"
p.xaxis.axis_label_text_font_size = "13pt"
p.xaxis.major_label_text_font_size = "13pt"
p.yaxis.major_label_text_font_size = "13pt"
p.yaxis.major_label_text_font_style = 'bold'
p.xaxis.major_label_text_font_style = 'bold'
p.yaxis.major_label_text_font = "Arial"
p.xaxis.major_label_text_font = "Arial"
p.title.align = 'center'
p.title.text_font_size = '12pt'
p.xaxis.axis_line_width = 0
p.yaxis.axis_label_text_font_style = "bold"
p.xaxis.axis_label_text_font_style = "bold"
p.toolbar.active_scroll = "auto"
p.toolbar.autohide = True

dashboard = row(column([select_metric, mean_line, div], width = 200), p)
curdoc().add_root(dashboard)
show(dashboard)
