import geopandas as gpd
import shapely
import pandas as pd
import numpy as np
import datetime
import calendar
import os
from bokeh.plotting import figure, show
import bokeh
from collections import Counter
from pprint import pprint
import pymysql
from bokeh.io import curdoc
from pytz import timezone
import json
from pprint import pprint
import datetime
import time
from datetime import timezone
from bokeh.plotting import figure, show, gmap
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL,FixedTicker, CustomJS, DatetimeTickFormatter, GMapOptions, LinearColorMapper, LabelSet
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter,DataRange1d , Band, SingleIntervalTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Button, CheckboxGroup, Div,  CheckboxButtonGroup
from bokeh.layouts import widgetbox, row, column, gridplot, layout
from bokeh.io import curdoc
from bokeh.palettes import Purples, BuPu, OrRd, viridis
from dateutil import parser
from bokeh.models.glyphs import ImageURL
from bokeh.models.renderers import GlyphRenderer
from bokeh.core.properties import Instance, String
from bokeh.transform import transform, linear_cmap
from bokeh.io import curdoc
from pytz import timezone
import pickle
from urllib.request import Request, urlopen
import bs4 as bs
import time
from bokeh.models import Legend, LegendItem

# Patches / patch support issue (no tooltip for patch).
# https://github.com/bokeh/bokeh/issues/9154

doc = curdoc()
doc.clear()
doc.title = 'IESO Zonal Map'

colours = {'Toronto':"#5D96B3",'Bruce':"cyan",
'Southwest':"black", 'Niagara':"purple",
"East":"#951D16",'Northeast':"red",
'West':"#BB6831",'Essa':"navy",
'Ottawa':"#CAAE8A", 'Northwest':"darkorange"}

data = gpd.read_file(os.getcwd().replace("\\", "/") + "/IESO_Zonal_Map.geojson")
data.index = data['Name']
hover = HoverTool(tooltips=[("Name", "@region"), ("Population", "@pop"), ("Dwellings", "@dwellings")] )
# middle of map is lat=50, long=-85
key = 'AIzaSyDDAzir5vZuZ0Z-dkCLOp3rIq5l74KLJWo'
lat = 50
lon = -85
map_options = GMapOptions(lat=lat, lng=lon, map_type="roadmap", zoom=5)
map_figure = gmap(key, map_options, title="IESO Zonal Map", width=600, height=600, y_axis_label='Latitude', x_axis_label='Longitude',)
map_figure.add_tools(hover)

xs = []
ys = []
for x in list(data['geometry'].exterior.values):
    long, lati = x.coords.xy
    ys.append([i for i in lati])
    xs.append([i for i in long])

source = ColumnDataSource(data = {'xs':xs, 'ys':ys, 'region': list(data['Name']), "pop":[1 for x in list(data['Name'])], "dwellings":[1 for x in list(data['Name'])], 'colour':[colours[x] for x in data['Name']]})
map_figure.patches(xs='xs', ys='ys', source=source, alpha=0.6, fill_color = 'colour')
map_figure.legend.location = 'top_right'
map_figure.yaxis.axis_label_text_font_size = "10pt"
map_figure.xaxis.axis_label_text_font_size = "10pt"
map_figure.xaxis.major_label_text_font_size = "8pt"
map_figure.yaxis.major_label_text_font_size = "8pt"
map_figure.yaxis.major_label_text_font_style = 'bold'
map_figure.xaxis.major_label_text_font_style = 'bold'
map_figure.yaxis.major_label_text_font = "Arial"
map_figure.xaxis.major_label_text_font = "Arial"
map_figure.title.align = 'center'
map_figure.title.text_font_size = '12pt'
map_figure.yaxis.minor_tick_line_color = None
map_figure.xaxis.minor_tick_line_color = None
map_figure.yaxis.axis_label_text_font_style = "bold"
map_figure.xaxis.axis_label_text_font_style = "bold"

doc.add_root(map_figure)
show(map_figure)

