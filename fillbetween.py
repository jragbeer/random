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
print(X)
#mean array, difference array,
ymean = np.array([y.mean() for x in y])
diffs = y - ymean
kk = []
for x in range(len(y)):
    try:
        if np.sign(ymean[0] - y[x]) != np.sign(ymean[0] - y[x+1]):
            kk.append([x,x+1])
    except:
        pass
print(kk)
kk[0] = [0, kk[0][-1]]
print(kk)

# 1000 points between each value in y
xx = {0: np.array([x for x in np.linspace(0, len(y)-1, (len(y)-1) * 1000)])}

theta = {}
degrees = {}
triangle_adjacent = {}
cc = {}
magicnumber = {0:0}
newy = {}

def thing(xx, duo, idx):
    theta[idx] = math.atan(np.abs(y[duo[1]] - y[duo[0]]) / 2)
    degrees[idx] = theta[idx] * 180 / math.pi
    triangle_adjacent[idx] = (ymean[0] - y[duo[0]]) * math.atan(math.radians(90 - degrees[idx]))
    _,  magicnumber[idx] = find_nearest(xx[0], triangle_adjacent[idx])
    xx[idx] = xx[0][:magicnumber[idx]].copy()
    newy[idx] = np.linspace(y[duo[0]], y[duo[1]], 1000)
    find, _ = find_nearest(newy[idx], ymean[0])
    k = list(newy[idx]).index(find)
    if idx == 1:
        newy[idx] = np.array([x for x in np.linspace(newy[idx][0], newy[idx][k], magicnumber[idx])])
    elif idx == len(kk):
        pass
    else:
        pass
    return xx[[idx]], newy[idx]

def ok(xx, duo, idx, magicnumber, newy):
    theta[idx] = math.atan(np.abs(y[duo[1]] - y[duo[0]]) / len(y[duo[0]:y[duo[1]]]))
    degrees[idx] = theta[idx] * 180 / math.pi
    # find length of adjacent for triangle
    triangle_adjacent[idx] = (ymean[0] - y[duo[0]]) * math.atan(math.radians(90 - degrees[idx]))
    # find nearest number for the length with
    _,  magicnumber[idx] = find_nearest(xx[0], triangle_adjacent[idx])
    # new point on X line
    # original line, sliced. From last magic number to this magic number
    xx[idx] = xx[0][magicnumber[idx-1]:magicnumber[idx]].copy()
    newy[idx] = np.linspace(y[duo[0]], y[duo[1]], 1000)
    find, _ = find_nearest(newy[idx], ymean[0])
    k = list(newy[idx]).index(find)
    if idx == 1:
        newy[idx] = np.array([x for x in np.linspace(newy[idx][0], newy[idx][k], magicnumber[idx])])
    elif idx == len(kk):
        pass
    else:
        pass
    return xx[[idx]], newy[idx]

theta[1] = math.atan(np.abs(y[2]-y[0]) / len(y[:2]))
degrees[1] = theta[1] * 180 / math.pi
triangle_adjacent[1] = (y.mean()-y[0])*math.atan(math.radians(90-degrees[1]))
cc[1], magicnumber[1] = find_nearest(xx[0], triangle_adjacent[1])
xx[1]=xx[0][:magicnumber[1]].copy()
newy[1] = np.linspace(y[0], y[2], 1000)
find, _ = find_nearest(newy[1], y.mean())
k=list(newy[1]).index(find)
newy[1] = np.array([x for x in np.linspace(newy[1][0],newy[1][k], magicnumber[1])])
print(magicnumber)


theta[2] = math.atan(np.abs(y[7]-y[6]) / 1)
degrees[2] = theta[2] * 180 / math.pi
triangle_adjacent[2] = np.abs((ymean[0]-y[7]))*math.atan(math.radians(90-degrees[2]))
cc[2], magicnumber[2] = find_nearest(xx[0], triangle_adjacent[2])
xx[2]=xx[0][magicnumber[1]:7000-magicnumber[2]].copy()
newy[2] = np.concatenate((np.linspace(ymean[0], y[2], 2000-magicnumber[1]), np.linspace(y[2], y[3], 1000), np.linspace(y[3], y[4], 1000),np.linspace(y[4], y[5], 1000),np.linspace(y[5], y[6], 1000),np.linspace(y[6], ymean[0], 1000-magicnumber[2])), axis=None)


theta[3] = math.atan(np.abs(y[8]-y[7]) / 1)
degrees[3] = theta[3] * 180 / math.pi
triangle_adjacent[3] = np.abs(y.mean()-y[7])*math.tan(math.radians(90-degrees[3]))
cc[3], magicnumber[3] = find_nearest(xx[0], 7+triangle_adjacent[3])
xx[3]=xx[0][7000-magicnumber[2]:magicnumber[3]].copy()
newy[3] = np.concatenate((np.linspace(ymean[0], y[7], len(xx[0][7000-magicnumber[2]:7000])), np.linspace(y[7], y.mean(),len(xx[0][7000:magicnumber[3]]))), axis = None)

theta[4] = math.atan(np.abs(y[9]-y[8]) / 1)
degrees[4] = theta[4] * 180 / math.pi
triangle_adjacent[4] = np.abs(ymean[0]-y[8])*math.tan(math.radians(90-degrees[4]))
cc[4], magicnumber[4] = find_nearest(xx[0], 8+triangle_adjacent[4])
xx[4] = xx[0][magicnumber[3]: magicnumber[4]].copy()
newy[4] = np.concatenate((np.linspace(ymean[0], y[8], len(xx[0][magicnumber[3]:8000])), np.linspace(y[8], ymean[0],len(xx[0][8000:magicnumber[4]]))), axis = None)


xx[5] = xx[0][magicnumber[4]:].copy()
newy[5] = np.linspace(y.mean(), y[9], len(xx[5]))
ymean = np.array([y.mean() for x in range(len(xx))])
print(ymean)
data = ColumnDataSource(data = dict(x=xx[0], y=y, ymean=ymean, x1=xx[1], x2=xx[2], x3=xx[3], x4=xx[4], x5=xx[5], newy5=newy[5], newy2=newy[2], newy3=newy[3], newy4=newy[4], newy1=newy[1],origx = X,))

TOOLS = "pan,wheel_zoom,reset,hover,save"
p = figure(plot_width=1600, plot_height=1000,title="Kevin Durant PPG", tools=TOOLS)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

print(X)
bands = {}
for i in range(1,6):
    if i % 2 != 0:
        print(i)
        bands[i] = Band(base = f"x{i}", source = data, upper='ymean', lower = f"newy{i}",
                        level='underlay', fill_alpha=0.44, line_width=1, fill_color='red', line_color = 'red')
    else:
        bands[i] = Band(base = f"x{i}", source = data, lower='ymean', upper = f"newy{i}",
                        level='underlay', fill_alpha=0.44, line_width=1, fill_color='green', line_color = 'green')
    p.add_layout(bands[i])
p.line('origx','y', source=data, line_width=3,)
p.line('origx','ymean', source=data, line_width=3,)
show(p)




