import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
from datetime import timezone
from bokeh.plotting import figure, show, gmap
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, CustomJS, DatetimeTickFormatter, GMapOptions, LinearColorMapper
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter,DataRange1d , Band, SingleIntervalTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Button, CheckboxGroup, Div
from bokeh.layouts import widgetbox, row, column
from bokeh.io import curdoc
from bokeh.palettes import Purples, BuPu
import webbrowser
from math import pi
from dateutil import parser
from os.path import dirname, join
import re
import bokeh
from bokeh.io import show
from bokeh.transform import linear_cmap
from bokeh.palettes import RdYlGn3 as palette
from bokeh.plotting import figure
import math

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

# y values
y = np.array([20.3, 25.43, 30.2, 27.9, 28.1, 28.2, 32, 25.5, 28.2, 25.5])

# easier to plot 8 vs 8000
X = np.array([x for x in np.arange(len(y))])

#mean array, difference array,
ymean = np.array([y.mean() for x in X])
diffs = y - ymean



ydict={'y{}'.format(x): np.linspace(y[x],y[x+1], 1000) for x in range(len(y)-1)}

# 1000 points between each value in y
xx = np.array([x for x in np.linspace(0, len(y)-1, (len(y)-1) * 1000)])

theta = math.atan(np.abs(y[2]-y[0]) / len(y[:2]))
degrees = theta * 180 / math.pi
tri1adj = (ymean[0]-y[0])*math.atan(math.radians(90-degrees))
cc, magicnumber = find_nearest(xx, tri1adj)
xx1=xx[:magicnumber].copy()
newy = np.linspace(y[0], y[2], 1000)
find, _ = find_nearest(newy, ymean[0])
ymean2 = np.array([ymean[0] for x in range(len(newy))])
k=list(newy).index(find)
newy = np.array([x for x in np.linspace(newy[0],newy[k], magicnumber)])

theta2 = math.atan(np.abs(y[7]-y[6]) / 1)
degrees2 = theta2 * 180 / math.pi
tri2adj = np.abs((ymean[0]-y[7]))*math.atan(math.radians(90-degrees2))
tri2hyp = np.sqrt(np.abs(ymean[0]-y[7])**2 + tri2adj**2)
cc2, magicnumber2 = find_nearest(xx, tri2adj)
xx2=xx[magicnumber:8000-magicnumber2].copy()
newy2 = np.concatenate((np.linspace(ymean[0], y[2], 2000-magicnumber), np.linspace(y[2], y[3], 1000), np.linspace(y[3], y[4], 1000),np.linspace(y[4], y[5], 1000),np.linspace(y[5], y[6], 1000),np.linspace(y[6], ymean[0], 1000-magicnumber2)), axis=None)


theta3 = math.atan(np.abs(y[8]-y[7]) / 1)
degrees3 = theta3 * 180 / math.pi
tri3adj = np.abs(ymean[0]-y[7])*math.tan(math.radians(90-degrees3))
cc3, magicnumber3 = find_nearest(xx, 7+tri3adj)
xx3=xx[7000-magicnumber2:magicnumber3].copy()
newy3 = np.concatenate((np.linspace(ymean[0], y[7], len(xx[7000-magicnumber2:7000])), np.linspace(y[7], ymean[0],len(xx[7000:magicnumber3]))), axis = None)

theta4 = math.atan(np.abs(y[9]-y[8]) / 1)
degrees4 = theta4 * 180 / math.pi
tri4adj = np.abs(ymean[0]-y[8])*math.tan(math.radians(90-degrees4))
cc4, magicnumber4 = find_nearest(xx, 8+tri4adj)
xx4 = xx[magicnumber3: magicnumber4].copy()
newy4 = np.concatenate((np.linspace(ymean[0], y[8], len(xx[magicnumber3:8000])), np.linspace(y[8], ymean[0],len(xx[8000:magicnumber4]))), axis = None)


xx5 = xx[magicnumber4:].copy()
newy5 = np.linspace(ymean[0], y[9], len(xx5))
ymean = np.array([ymean[0] for x in range(len(xx))])
print(xx5)
data = ColumnDataSource(data = dict(x=xx, y= y, ymean = ymean, x1=xx1, x2 = xx2,x3=xx3,x4=xx4 ,x5 = xx5, newy5 = newy5, newy2 = newy2,newy3 = newy3, newy4 = newy4,newy = newy,origx = X, ymean2 = ymean2))

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(plot_width=950, plot_height=450,title="Kevin Durant PPG", tools=TOOLS)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"
p.line('origx','y', source = data)
p.line('origx','ymean', source = data)

band1 = Band(base='x1', lower='newy', upper='ymean', source=data,
            level='underlay', fill_alpha=0.54, line_width=1, fill_color='red', line_color = 'red')
p.add_layout(band1)

band2 = Band(base='x2', lower='ymean', upper='newy2', source=data,
            level='underlay', fill_alpha=0.54, line_width=1, fill_color='green', line_color = 'green')
p.add_layout(band2)

band3 = Band(base='x3', lower='newy3', upper='ymean', source=data,
            level='underlay', fill_alpha=0.54, line_width=1, fill_color='red', line_color = 'red')
p.add_layout(band3)

band4 = Band(base='x4', lower='ymean', upper='newy4', source=data,
            level='underlay', fill_alpha=0.54, line_width=1, fill_color='green', line_color = 'green')
p.add_layout(band4)

band5 = Band(base='x5', lower='newy5', upper='ymean', source=data,
            level='underlay', fill_alpha=0.54, line_width=1, fill_color='red', line_color = 'red')
p.add_layout(band5)

show(p)

