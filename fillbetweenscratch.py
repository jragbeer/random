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

np.random.seed(0)

# y values
y = np.array([20.3, 22.93, 30.2, 27.9, 28.1, 28.2, 32, 25.5, 28.2, 25.5])

# easier to plot 8 vs 8000
X = np.array([x for x in np.arange(len(y))])
ymean = [y.mean() for x in range(len(X))]
#mean array, difference array,
diffs = y - np.array([y.mean() for x in X])
kk = []
for x in range(len(y)):
    try:
        if np.sign(ymean[0] - y[x]) != np.sign(ymean[0] - y[x+1]):
            kk.append([x,x+1])
    except:
        pass
print(kk)
theta, degrees, triangle_adjacent = {}, {}, {}
#
# high = np.around(np.abs(diffs[kk[0][0]]) + np.abs(diffs[kk[0][0]]), 3)
# print(high)
# hypotenuse = np.sqrt(1+high**2) # c = sqrt(a**2 + b**2) where a = 1 and b = high
# adjacent = 1
# theta[1] = np.around(np.arctan(np.abs(hypotenuse / adjacent)), 8)
# theta[2] = np.around(np.arcsin(np.abs(high / hypotenuse)), 8)
# triangle_adjacent[1] = np.around(X[2] - (diffs[2] / np.tan(theta[1])), 3)
# triangle_adjacent[2] = np.around(X[1]+(np.abs(diffs[1]) / np.tan(theta[1])), 3)
# avg = (triangle_adjacent[1] + triangle_adjacent[2])/2
# patches = {"1":{'x': [0, 0, X[1], avg],
#              'y': [y.mean(), y[0], y[1], y.mean()]}}
# print(theta)
# print(patches)
# print(triangle_adjacent)
# print('-'*13)

def thing(x_in, y_in, kk, diffs, idx):
    cc = len(kk)
    if idx == cc:
        idx = -1
    print(idx)
    adjacent = 1
    high = np.around(np.abs(diffs[kk[idx][0]]) + np.abs(diffs[kk[idx][0]]), 8)
    hypotenuse = np.sqrt(1 + high**2) # c = sqrt(a**2 + b**2) where a = 1 and b = high
    theta[4] = np.around(np.arctan(np.abs(hypotenuse / adjacent)), 8)
    if idx == 0:
        triangle_adjacent[1] = np.around(X[2] - (diffs[2] / np.tan(theta[4])), 3)
        triangle_adjacent[2] = np.around(X[1] + (np.abs(diffs[1]) / np.tan(theta[4])), 3)
        avg = (triangle_adjacent[1] + triangle_adjacent[2]) / 2
        x_array = [0, 0,]

        if y_in[0] > y_in.mean():
            for i, k in enumerate(y_in):
                if k < y_in.mean():
                    x_array.append(x_in[i-1])
                    break
            x_array.append(avg)
        if y_in[0] < y_in.mean():
            for i, k in enumerate(y_in):
                print(k)
                if k > y_in.mean():
                    x_array.append(x_in[i-1])
                    break
            x_array.append(avg)

        y_array = [y_in.mean(), y_in[idx], y_in[1], y_in.mean()]
        return x_array, y_array
    if idx == -1:
        triangle_adjacent[3] = np.around(X[-1] - (diffs[-2] / np.tan(theta[4])), 8)
        triangle_adjacent[4] = np.around(X[-2] + (np.abs(diffs[-1]) / np.tan(theta[4])), 8)
        avg = (triangle_adjacent[3] + triangle_adjacent[4]) / 2
        x_array = [x_in[idx], x_in[idx], avg]
        y_array = [y_in.mean(),y_in[idx], y_in.mean()]
        return x_array, y_array

patches = {f"{x+1}":{} for x in range(len(kk))}
patches["2"]["x"], patches["2"]["y"] = thing(X, y, kk, diffs, len(kk))
patches["1"]["x"], patches["1"]["y"] = thing(X, y, kk, diffs, 0)

print(patches)




data = ColumnDataSource(data = dict(y= y, ymean = ymean, origx = X, patch_1_x = patches["1"]["x"], patch_1_y = patches["1"]["y"],patch_2_x = patches["2"]["x"],patch_2_y = patches["2"]["y"]))

TOOLS = "pan,wheel_zoom,reset,hover,save"
p = figure(plot_width=1600, plot_height=1000,title="Kevin Durant PPG", tools=TOOLS)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"
p.line('origx','y', source=data, line_width=3,)
p.line('origx','ymean', source=data, line_width=3,)
p.patch('patch_1_x', "patch_1_y", source = data, fill_color="red", alpha = 0.5)
p.patch('patch_2_x', "patch_2_y", source = data, fill_color="red", alpha = 0.5)

show(p)
