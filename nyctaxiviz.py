import geopandas as gpd
import pysal as ps
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
    update_chart(str(new), select_car_type.value, select_year.value, select_hour.value, select_month.value,
                     select_day.value, select_holiday.value)

def update_car_type(attr, old, new):
    update_chart(select_pickup_dropoff.value, str(new).lower(),  select_year.value, select_hour.value, select_month.value, select_day.value, select_holiday.value)

def update_day_of_week(attr, old, new):
    update_chart(select_pickup_dropoff.value, select_car_type.value, select_year.value, select_hour.value, select_month.value, str(new), select_holiday.value)

def update_hour(attr, old, new):
    update_chart(select_pickup_dropoff.value, select_car_type.value, select_year.value, str(new),  select_month.value, select_day.value, select_holiday.value)

def update_year(attr, old, new):
    update_chart(select_pickup_dropoff.value, select_car_type.value, str(new), select_hour.value, select_month.value, select_day.value, select_holiday.value)

def update_holiday(attr, old, new):

    update_chart(select_pickup_dropoff.value, select_car_type.value, select_year.value, select_hour.value, select_month.value, select_day.value, str(new))

def update_month(attr, old, new):
    update_chart(select_pickup_dropoff.value, select_car_type.value, select_year.value, select_hour.value, str(new), select_day.value, select_holiday.value)

def update_chart(pickup_dropoff, cartype, year, hour, month, day, holiday):
    global DF
    DATA = copy.deepcopy(DF)

    holi = ['No', 'Yes']
    if str(holiday) in holi:
        holi_value = holi.index(str(holiday))
    else:
        holi_value = 'all'

    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if str(day).lower() in weekdays:
        day_value = weekdays.index(str(day).lower())+1
    else:
        day_value = 'all'
    months2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if str(month) in months2:
        month_value = months2.index(str(month))+1
    else:
        month_value = 'all'

    if hour == "6pm-7pm":
        hour_value = 18
    elif hour == "7pm-8pm":
        hour_value = 19
    elif hour == "8pm-9pm":
        hour_value = 20
    else:
        hour_value = 'all'

    thing = so_far[pickup_dropoff][cartype.lower()][str(year).lower()][str(hour_value)][str(month_value)][str(day_value)][str(holi_value)]

    div.text = make_div(thing)
    dat = pd.merge(DATA, thing, right_index=True, left_on='LocationID')
    borough_data_ = pd.DataFrame(dat.groupby(['borough'])['value'].sum())
    borough_source.data = ColumnDataSource(
        data={'names': borough_data_.index, 'x': np.array([x for x in range(len(borough_data_.index))]) + 0.5, 'right': borough_data_.values,
              'colour': ['firebrick'] * len(borough_data_.index)}).data

    top5_locations = dat.sort_values(by='value', ascending=False).iloc[:5, :].sort_values(by='value')

    locations_source.data = ColumnDataSource(
        data={'zone': np.asarray(top5_locations['zone']), 'x': np.array([x for x in range(len(top5_locations.index))]) + 0.5, 'borough': np.asarray(top5_locations["borough"]),
              'right': np.asarray(top5_locations["value"]), 'colour': ['orange'] * len(top5_locations.index)}).data
    dfsource.data = ColumnDataSource(data=dat).data
    z.y_range.factors = top5_locations['zone'].to_list()

def wrap_in_paragraphs(text, colour="DarkSlateBlue", size=4):
    """
    This function wraps text in paragraph, bold and font tags - according to the colour and size given.
    :param text: text to wrap in tags
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return """<p><b><font color={} size={}>{}</font></b></p>""".format(colour, size, text)

def make_div(info):
    text = wrap_in_paragraphs('NYC For-Hire Vehicle / Taxi  Analysis', size=5) + \
    wrap_in_paragraphs('Total Trips: {:,}'.format(np.asarray(info).sum()), 'Firebrick')
    return text

doc = curdoc()
#clears the html page and gives the tab a name
doc.clear()
doc.title = 'NYC Taxi Dashboard'

# for colr in ['yellow', 'green', "fhv", "all", ]:
#     pu_do_data['Pick-Up'][str(colr)] = {}
#     pu_do_data['Drop-Off'][str(colr)] = {}
#     for yr in [2016, 2017, 2018, 'all']:
#         # pickle_in = open("pulocationid_{}_full.pickle".format(colr),"rb")
#         pickle_in = open("pulocationid_{}_{}_full_test.pickle".format(colr, yr),"rb")
#         pu_data = pickle.load(pickle_in)
#         # pickle_in = open("dolocationid_{}_full.pickle".format(colr),"rb")
#         pickle_in = open("dolocationid_{}_{}_full_test.pickle".format(colr, yr),"rb")
#         do_data = pickle.load(pickle_in)
#         pu_data.columns = ['value']
#         do_data.columns = ['value']
#         pu_do_data['Pick-Up'][str(colr)][str(yr)] = pu_data
#         pu_do_data['Drop-Off'][str(colr)][str(yr)] = do_data

# File path
points_fp = r"C:\Users\J_Ragbeer\PycharmProjects\nyctaxi\geofiles\taxi_zones.shp"
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

pickle_in = open("answers.pickle","rb")
so_far = pickle.load(pickle_in)
DF = copy.deepcopy(data)
starting = so_far['Drop-Off']["all"]["all"]["all"]["all"]["all"]["all"]
data = pd.merge(data, starting, right_index = True, left_on='LocationID')

top5_ = data.sort_values(by='value', ascending=False).iloc[:5, :].sort_values(by='value')

dfsource = ColumnDataSource(data=data)

current_time = datetime.datetime.now()
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

borough_data = pd.DataFrame(data.groupby(['borough'])['value'].sum())

# Flip the colors in color palette
# infinite colour palette
palette = cc.fire[16:253]
palette.reverse()
color_mapper = LinearColorMapper(palette=palette, )
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(), location=(0, 0), orientation='horizontal', border_line_color=None,)

p = figure(title="NYC Map", tools=TOOLS,
           plot_width=1225, plot_height=900, active_scroll="wheel_zoom")

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
                ("No. of Trips", "@value{0,0}"),
               ]

p.add_tools(ghover)
p.axis.visible = False
p.add_layout(color_bar, 'below')

# W Chart
w = figure(title="Borough Counts", tools=TOOLS, y_axis_label=None, y_range=FactorRange(factors=[]),
           plot_width=400, plot_height=450, active_scroll="wheel_zoom")
w.ygrid.grid_line_color = None
borough_source = ColumnDataSource(data={'names': borough_data.index, 'x': np.array([x for x in range(len(borough_data.index))])+0.5, 'right': borough_data.values, 'colour': ['firebrick']*len(borough_data.index)})

wchart = w.hbar(y='x', right='right', left=0, height=0.8, source=borough_source, fill_color='colour', name='wchart')
whover = HoverTool(renderers=[wchart])
whover.tooltips=[("Borough", "@names"),
                ("No. of Trips", "@right{0,0}")]
w.add_tools(whover)
w.xaxis.formatter = NumeralTickFormatter(format="0.0a")
w.y_range.factors = borough_data.index

# Z Chart
z = figure(title="Top 5 Locations", tools=TOOLS, y_axis_label=None, y_range=FactorRange(factors=[]),
           plot_width=400, plot_height=450, active_scroll="wheel_zoom")
z.ygrid.grid_line_color = None
locations_source = ColumnDataSource(data={'zone': np.asarray(top5_['zone']), 'x': np.array([x for x in range(len(top5_.index))])+0.5,'borough': np.asarray(top5_["borough"]), 'right': np.asarray(top5_["value"]), 'colour': ['orange']*len(top5_.index)})

zchart = z.hbar(y='x', right='right', left=0, height=0.6, source=locations_source, fill_color='colour', name='zchart')
zhover = HoverTool(renderers=[zchart])
zhover.tooltips=[("Borough", "@borough"),
                 ("Zone", "@zone"),
                ("No. of Trips", "@right{0,0}")]
z.add_tools(zhover)
z.xaxis.formatter = NumeralTickFormatter(format="0.0a")
z.y_range.factors = np.asarray(top5_['zone'])

select_pickup_dropoff = Select(title='Pick-Up/Drop-Off', value='Drop-Off', options=['Pick-Up', 'Drop-Off'])
select_pickup_dropoff.on_change('value', update_pickup_dropoff)

select_car_type = Select(title='Taxi Type', value='All', options=['Yellow', 'Green', 'FHV', 'All'])
select_car_type.on_change('value', update_car_type)

select_year = Select(title='Year', value='All', options=[str(x) for x in range(2016, 2019)] + ['All'])
select_year.on_change('value', update_year)

select_hour = Select(title='Hour', value='All', options=["6pm-7pm", "7pm-8pm", "8pm-9pm"] + ['All'])
select_hour.on_change('value', update_hour)

select_month = Select(title='Month', value='All', options=months + ['All'])
select_month.on_change('value', update_month)

select_day = Select(title='Day of Week', value='All', options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'])
select_day.on_change('value', update_day_of_week)

select_holiday = Select(title='Holiday', value='All', options=['No', 'Yes', 'All'])
select_holiday.on_change('value', update_holiday)

div = Div(width=240, text=make_div(starting))

bottom_div_text = wrap_in_paragraphs("Data is from June 2016 to end of 2018.") + wrap_in_paragraphs("This dashboard is maintained by:", "DimGray") + \
                  wrap_in_paragraphs("Julien Ragbeer, IT", "Black") + \
                  wrap_in_paragraphs("Any comments / questions / concerns, please send an email to the maintainer.", "DimGray", size=3) + \
                  wrap_in_paragraphs("""Data is up-to-date as of <br><font color="DarkSlateBlue">January 1, 2019</font>""", "Black", 3) + \
                  wrap_in_paragraphs("Best viewed with Google Chrome", "DimGray", size=3)

bottom_div = Div(text=bottom_div_text, width=235)

uu = widgetbox([select_pickup_dropoff, select_car_type, select_year, select_hour, select_month, select_day, select_holiday], width=240)
first_part = column(uu, div, bottom_div)
second_part = column(w,z)
dashboard = row(first_part, p, second_part,)
show(dashboard)

doc.add_root(dashboard)
