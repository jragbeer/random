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

np.random.seed(4150)
# y values
y = np.array([np.random.randint(10, 50 + 1) for x in range(10)])*-1
X = np.array([x for x in np.arange(len(y))])
ymean = y.mean()
# difference array
diffs = y - ymean
change_points = []
for i in range(len(y)):
    try:
        if np.sign(ymean - y[i]) != np.sign(ymean - y[i+1]):
            change_points.append((i, i+1))
    except:
        pass

def make_glyph_coords(x_in, y_in, change_points, diffs, idx, last_x=None, adjacent = 1):
    """

    This function checks whether it is the first, last or neither. Then calculates the next angle to draw.

    :param x_in: x points of input
    :param y_in: y points of input
    :param change_points: a list of tuples containing where the change points are
    :param diffs: list of differences between y point and mean for each x point
    :param idx: index of change point in list, starts at 0
    :param last_x: last x point to be calculate
    :param adjacent: distance between x points, assuming 1 now
    :return: the ouput of an inner function
    """

    def first_glpyh(x_in, y_in, change_points, diffs, idx, theta):
        x_array = [0, 0, ]
        y_array = [y_in.mean(), y_in[idx],]
        # if glyph is above live and diff is positive
        if y_in[0] > y_in.mean():
            triangle_adjacent_1 = np.around(x_in[change_points[0][1]] + (diffs[change_points[0][1]] / np.tan(theta)), 3)
            triangle_adjacent_2 = np.around(x_in[change_points[0][0]] + (np.abs(diffs[change_points[0][0]]) / np.tan(theta)), 3)
            avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
            for i, k in enumerate(y_in):
                if k > y_in.mean():
                    x_array.append(x_in[i])
                    y_array.append(y_in[i])
                elif k < y_in.mean():
                    break
            x_array.append(avg)
            above_below = 'above'
        # if the glyph will be below line and diff is negative
        elif y_in[0] < y_in.mean():
            triangle_adjacent_1 = np.around(x_in[change_points[0][1]] - (diffs[change_points[0][1]] / np.tan(theta)), 3)
            triangle_adjacent_2 = np.around(x_in[change_points[0][0]] + (np.abs(diffs[change_points[0][0]]) / np.tan(theta)), 3)
            avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
            for i, k in enumerate(y_in):
                if k < y_in.mean():
                    x_array.append(x_in[i])
                    y_array.append(y_in[i])
                elif k > y_in.mean():
                    break
            x_array.append(avg)
            above_below = 'below'
        y_array.append(y_in.mean())
        return x_array, y_array, avg, above_below

    def last_glpyh(x_in, y_in, diffs, idx, last_x):

        x_array = [last_x, x_in[idx], x_in[idx],]
        y_array = [y_in.mean(), y_in.mean(), y_in[idx], ]

        if diffs[-1] > 0:
            for i in range(len(y_in)-1, 0, -1):
                if diffs[i] > 0:
                    x_array.append(x_in[i])
                    y_array.append(y_in[i])
                else:
                    break
            above_below = 'above'
        else:
            for i in range(len(y_in)-1, 0, -1):
                if diffs[i] < 0:
                    x_array.append(x_in[i])
                    y_array.append(y_in[i])
                else:
                    break
            above_below = 'below'
        return x_array, y_array, None, above_below

    def middle_glyph(x_in, y_in, change_points, diffs, idx, theta):
        if y_in[change_points[idx][0]] > y_in.mean():
            triangle_adjacent_1 = np.around(x_in[change_points[idx][0]] + (diffs[change_points[idx][0]] / np.tan(theta)), 3)
            triangle_adjacent_2 = np.around(x_in[change_points[idx][1]] - (np.abs(diffs[change_points[idx][1]]) / np.tan(theta)), 3)
            avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
            above_below = 'above'
        else:
            triangle_adjacent_1 = np.around(x_in[change_points[idx][0]] - (diffs[change_points[idx][0]] / np.tan(theta)), 3)
            triangle_adjacent_2 = np.around(x_in[change_points[idx][1]] - (np.abs(diffs[change_points[idx][1]]) / np.tan(theta)), 3)
            avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
            above_below = 'below'

        if np.abs(change_points[idx - 1][1] - change_points[idx][0]+1) > 1:
            x_array = [last_x] + [x for x in range(change_points[idx - 1][1], change_points[idx][0]+1)] + [avg]
        else:
            x_array = [last_x] + [x for x in range(change_points[idx - 1][1], change_points[idx][0] + 1)] + [avg]
        y_array = [y_in.mean()] + [x for x in y_in[change_points[idx-1][1]:change_points[idx][0]+1]] + [y_in.mean()]
        return x_array, y_array, avg, above_below
    # check if this is the last glyph to be drawn
    if idx == len(change_points):
        idx = -1
    # calculate dimensions of triangle and angle
    height = np.around(np.abs(diffs[change_points[idx][0]]) + np.abs(diffs[change_points[idx][1]]), 8)
    hypotenuse = np.sqrt(1 + height**2) # c = sqrt(a**2 + b**2) where a = 1 and b = high
    theta = np.around(np.arctan(np.abs(hypotenuse / adjacent)), 8)
    # if the first glyph to be drawn
    if idx == 0:
        return first_glpyh(x_in, y_in, change_points, diffs, idx, theta)
    # if the last glyph to be drawn
    elif idx == -1:
        return last_glpyh(x_in, y_in, diffs, idx, last_x)
    # if a glyph in the middle of the endpoints
    else:
        return middle_glyph(x_in, y_in, change_points, diffs, idx, theta)

# the patches to plot
patches = {f"{x+1}":{} for x in range(len(change_points)+1)}
# above or below dictionary, helps to colour the patches
a_b_dict = {f"{x+1}":{'words':None, 'colour':None} for x in range(len(change_points)+1)}
x_point = None
# for each change point (pass the line to switch at)
for x in range(1,len(change_points)+2):
    # calculate x, y, right-most point on x-axis, position of patch
    patches[str(x)]["x"], patches[str(x)]["y"], x_point, a_b_dict[str(x)]["words"] = make_glyph_coords(X, y, change_points, diffs, x-1, x_point)
    # assign colour based on position of patch
    if a_b_dict[str(x)]['words'] == 'below':
        a_b_dict[str(x)]['colour'] = 'red'
    elif a_b_dict[str(x)]['words'] == 'above':
        a_b_dict[str(x)]['colour'] = 'green'
# initial data
data_dict = {"x": X, "y": y, "ymean": [ymean for x in range(len(y))], }
# add x and y arrays for each patch
data_dict.update(**{f"patch_{x}_x": patches[x]["x"] for x in patches.keys()})
data_dict.update(**{f"patch_{x}_y": patches[x]["y"]for x in patches.keys()})

# create single CDS for all of the glyphs
data = ColumnDataSource(data = data_dict)

# plot 2 lines (data, data's average) and then each patch
TOOLS = "pan,wheel_zoom,reset,hover,save"
p = figure(plot_width=1400, plot_height=800, title="Fill Between Example", tools=TOOLS)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"
p.line('x','y', source=data, line_width=3,)
p.line('x','ymean', source=data, line_width=3,)
patch_glyphs = {}
for x in range(1,len(change_points)+2):
    patch_glyphs[str(x)] = p.patch(f'patch_{x}_x', f"patch_{x}_y", source=data, fill_color=a_b_dict[str(x)]['colour'], alpha=0.5)
show(p)
