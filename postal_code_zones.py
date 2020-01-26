import geopandas as gpd
import pysal as ps
from shapely.geometry import Point
import numpy as np
import pandas as pd
import datetime
import bs4 as bs
import urllib.request
from bokeh.plotting import figure, show, save
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, LogColorMapper, GeoJSONDataSource, FactorRange, FixedTicker, FuncTickFormatter
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, ColorBar, LinearColorMapper, BasicTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs
from bokeh.layouts import widgetbox, row, column, gridplot, layout
from bokeh.io import curdoc
import calendar
import pickle
import time
import copy
import colorcet as cc
import calendar
from pprint import pprint
import os
import json

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

#shapefile from https://www12.statcan.gc.ca/census-recensement/alternative_alternatif.cfm?archived=1&l=eng&dispext=zip&teng=gfsa000a11a_e.zip&k=%20%20%20%2026170&loc=http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gfsa000a11a_e.zip

shape_file = "C:/Users/Julien/PycharmProjects/peaktracker/gfsa/gfsa000a11a_e.shp"
# Read the data
data = gpd.read_file(shape_file)
data['x'] = data.apply(getCoords, geom_col="geometry", coord_type="x", axis=1)
data['y'] = data.apply(getCoords, geom_col="geometry", coord_type="y", axis=1)
data['y'] = [np.array(x) for x in data['y']]
data['x'] = [np.array(x) for x in data['x']]
pprint(data)
info = {x.CFSAUID: {'long':np.nanmean(x.x), 'lat': np.nanmean(x.y)} for x in data.itertuples()}

file = open(os.getcwd().replace("\\", "/") + "/IESO_Zonal_Map.geojson", 'r', encoding='utf-8')
zonal_geojson = json.loads(file.read())
zonal_data = {}
for x in range(len(zonal_geojson['features'])):
    r = zonal_geojson['features'][x]['geometry']['coordinates'][0]
    t = zonal_geojson['features'][x]['properties']['Name']
    d = zonal_geojson['features'][x]['properties']["description"]
    x_range = [i[0] for i in r]
    y_range = [i[1] for i in r]
    zonal_data[t] = {'Description': d, 'Long/Lat':r, 'ranges': {'long': [min(x_range), max(x_range)], 'lat': [min(y_range), max(y_range)], 'center': {'long':np.nanmean(x_range), 'lat': np.nanmean(y_range)}}}
print('\n-\n')
pprint(zonal_data)
print('\n-\n')

zone_boundaries = gpd.read_file(os.getcwd().replace("\\", "/") + "/IESO_Zonal_Map.geojson")

zone_boundaries['center'] = [i.centroid for i in zone_boundaries.geometry]
print(zone_boundaries.to_string())
print('\n-\n')
#

zone_fsa_mapping = {}

for i in zone_boundaries.itertuples(): # each zone
    for z in info.keys(): # each FSA
        if Point(info[z]['long'], info[z]['lat']).within(i.geometry):
            try:
                zone_fsa_mapping[i.Name].append(z)
            except:
                zone_fsa_mapping[i.Name] = [z]

pprint(zone_fsa_mapping)
