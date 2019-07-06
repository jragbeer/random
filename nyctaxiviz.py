import geopandas as gpd
import pysal as ps
import numpy as np
import pandas as pd
import datetime
import bs4 as bs
import urllib.request
from bokeh.plotting import figure, show, save
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, LogColorMapper, GeoJSONDataSource
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, ColorBar
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs
from bokeh.layouts import widgetbox, row, column, gridplot, layout
from bokeh.io import curdoc
import calendar
import pickle
import time
import copy
import colorcet as cc



def getXYCoords(geometry, coord_type):
    """ Returns either x or y coordinates from  geometry coordinate sequence. Used with LineString and Polygon geometries."""
    if coord_type == 'x':
        return geometry.coords.xy[0]
    elif coord_type == 'y':
        return geometry.coords.xy[1]

def getPolyCoords(geometry, coord_type):
    """ Returns Coordinates of Polygon using the Exterior of the Polygon."""
    ext = geometry.exterior
    return getXYCoords(ext, coord_type)

def getLineCoords(geometry, coord_type):
    """ Returns Coordinates of Linestring object."""
    return getXYCoords(geometry, coord_type)

def getPointCoords(geometry, coord_type):
    """ Returns Coordinates of Point object."""
    if coord_type == 'x':
        return geometry.x
    elif coord_type == 'y':
        return geometry.y

def multiGeomHandler(multi_geometry, coord_type, geom_type):
    """
    Function for handling multi-geometries. Can be MultiPoint, MultiLineString or MultiPolygon.
    Returns a list of coordinates where all parts of Multi-geometries are merged into a single list.
    Individual geometries are separated with np.nan which is how Bokeh wants them.
    # Bokeh documentation regarding the Multi-geometry issues can be found here (it is an open issue)
    # https://github.com/bokeh/bokeh/issues/2321
    """

    for i, part in enumerate(multi_geometry):
        # On the first part of the Multi-geometry initialize the coord_array (np.array)
        if i == 0:
            if geom_type == "MultiPoint":
                coord_arrays = np.append(getPointCoords(part, coord_type), np.nan)
            elif geom_type == "MultiLineString":
                coord_arrays = np.append(getLineCoords(part, coord_type), np.nan)
            elif geom_type == "MultiPolygon":
                coord_arrays = np.append(getPolyCoords(part, coord_type), np.nan)
        else:
            if geom_type == "MultiPoint":
                coord_arrays = np.concatenate([coord_arrays, np.append(getPointCoords(part, coord_type), np.nan)])
            elif geom_type == "MultiLineString":
                coord_arrays = np.concatenate([coord_arrays, np.append(getLineCoords(part, coord_type), np.nan)])
            elif geom_type == "MultiPolygon":
                coord_arrays = np.concatenate([coord_arrays, np.append(getPolyCoords(part, coord_type), np.nan)])

    # Return the coordinates
    return coord_arrays

def getCoords(row, geom_col, coord_type):
    """
    Returns coordinates ('x' or 'y') of a geometry (Point, LineString or Polygon) as a list (if geometry is LineString or Polygon).
    Can handle also MultiGeometries.
    """
    # Get geometry
    geom = row[geom_col]

    # Check the geometry type
    gtype = geom.geom_type

    # "Normal" geometries
    # -------------------

    if gtype == "Point":
        return getPointCoords(geom, coord_type)
    elif gtype == "LineString":
        return list( getLineCoords(geom, coord_type) )
    elif gtype == "Polygon":
        return list( getPolyCoords(geom, coord_type) )

    # Multi geometries
    # ----------------

    else:
        return list( multiGeomHandler(geom, coord_type, gtype) )

def update_pickup_dropoff(attr, old, new):
    update_chart(str(new), select_car_type.value, select_year.value)

def update_car_type(attr, old, new):
    update_chart(select_pickup_dropoff.value, str(new), select_year.value)


def update_year(attr, old, new):
    update_chart(select_pickup_dropoff.value, select_car_type.value, str(new))

def update_chart(pickup_dropoff, cartype, year):
    DATA = copy.deepcopy(DF)
    dat = pd.merge(DATA, pu_do_data[pickup_dropoff][cartype.lower()][str(year).lower()], right_index=True, left_on='LocationID')
    dfsource.data = ColumnDataSource(data=dat).data

doc = curdoc()
#clears the html page and gives the tab a name
doc.clear()
doc.title = 'NYC Taxi Dashboard'

# File path
points_fp = r"C:\Users\Julien\PycharmProjects\nyctaxi\geofiles\taxi_zones.shp"
pu_do_data = {"Pick-Up": {}, "Drop-Off": {}}
palette = cc.fire
for colr in ['yellow', 'green', "fhv", "all", ]:
    pu_do_data['Pick-Up'][str(colr)] = {}
    pu_do_data['Drop-Off'][str(colr)] = {}
    for yr in [2016, 2017, 2018, 'all']:
        # pickle_in = open("pulocationid_{}_full.pickle".format(colr),"rb")
        pickle_in = open("pulocationid_{}_{}_full_test.pickle".format(colr, yr),"rb")
        pu_data = pickle.load(pickle_in)
        # pickle_in = open("dolocationid_{}_full.pickle".format(colr),"rb")
        pickle_in = open("dolocationid_{}_{}_full_test.pickle".format(colr, yr),"rb")
        do_data = pickle.load(pickle_in)
        pu_data.columns = ['value']
        do_data.columns = ['value']
        pu_do_data['Pick-Up'][str(colr)][str(yr)] = pu_data
        pu_do_data['Drop-Off'][str(colr)][str(yr)] = do_data

# Read the data
data = gpd.read_file(points_fp)
data['x'] = data.apply(getCoords, geom_col="geometry", coord_type="x", axis=1)
data['y'] = data.apply(getCoords, geom_col="geometry", coord_type="y", axis=1)
data['y'] = [np.array(x) for x in data['y']]
data['x'] = [np.array(x) for x in data['x']]

# Select only necessary columns for our plotting to keep the amount of data minumum
# df = data[['x', 'y', 'pt_r_tt_ud', 'pt_r_tt', 'car_r_t', 'from_id', 'label_pt']]
data = data[[x for x in data.columns if x not in ['geometry']]]
data.fillna(0, inplace=True)

DF = copy.deepcopy(data)
data = pd.merge(data, pu_do_data['Pick-Up']["all"]["all"], right_index = True, left_on='LocationID')
dfsource = ColumnDataSource(data=data)

# Specify the tools that we want to use
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

# Flip the colors in color palette
palette.reverse()
color_mapper = LogColorMapper(palette=palette, )

p = figure(title="NYC Map", tools=TOOLS,
           plot_width=1350, plot_height=900, active_scroll="wheel_zoom")

# Do not add grid line
p.grid.grid_line_color = None

# Add polygon grid and a legend for it
grid = p.patches('x', 'y', source=dfsource, name="grid",
         fill_color={'field': 'value', 'transform': color_mapper},
         fill_alpha=1.0, line_color="black", line_width=0.23)

ghover = HoverTool(renderers=[grid])
ghover.tooltips=[("Location ID", "@LocationID"),
                ("Borough", "@borough"),
                ("Zone", "@zone"),
                ("Value", "@value{0,0}"),
               ]

p.add_tools(ghover)
color_bar = ColorBar(color_mapper=color_mapper, location=(0, 0), orientation='horizontal', )
p.axis.visible = False
p.add_layout(color_bar, 'below')

select_pickup_dropoff = Select(title='Pick-Up/Drop-Off', value='Pick-Up', options=['Pick-Up', 'Drop-Off'])
select_pickup_dropoff.on_change('value', update_pickup_dropoff)

select_car_type = Select(title='Taxi Type', value='All', options=['Yellow', 'Green', 'FHV', 'All'])
select_car_type.on_change('value', update_car_type)

select_year = Select(title='Year', value='All', options=['2016', '2017', '2018', 'All'])
select_year.on_change('value', update_year)

uu = widgetbox([select_pickup_dropoff, select_car_type, select_year], width=240)
dashboard = row(uu, p, )
show(dashboard)

doc.add_root(dashboard)
