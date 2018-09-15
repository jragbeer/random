import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
from datetime import timezone
from bokeh.plotting import figure, show, gmap
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, CustomJS, DatetimeTickFormatter, GMapOptions
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter,DataRange1d , Band, SingleIntervalTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Button, CheckboxGroup
from bokeh.layouts import widgetbox, row, column
from bokeh.io import curdoc
import webbrowser
from math import pi
from dateutil import parser
from os.path import dirname, join

doc = curdoc()
#clears the html page and gives the tab a name
doc.clear()
def player_stats(df, name):
    player = df[df['Player'] == str(name)].copy()
    return player
def add_to_Dict(dicta, key, value):
    #add to value if key present or create new key
    if key in dicta:
        return True
    else:
        return False

    # try:
    #     if dicta[key]:
    #         try:
    #             dicta[key] = dicta[key] + value
    #         except:
    #             pass
    #     else:
    #         dicta[key] = value
    # except:
    #     dicta[key] = value
    #
    # return dicta
def cleanplayer(df, player):
    aa = player_stats(df, player)
    cc = pd.DataFrame(aa.groupby(['Player', 'Year']).agg({'TRB':'sum', 'AST':'sum', 'PTS':'sum', 'G':'sum', 'DRB':'sum', 'ORB':'sum', 'PER':'mean'}))

    for x in cc.index:
        if cc['G'][x] > 82:
            cc.at[x, 'G'] = cc.at[x, 'G'] / 2
            cc.at[x, 'PTS'] = cc.at[x, 'PTS'] / 2
            cc.at[x, 'AST'] = cc.at[x, 'AST'] / 2
            cc.at[x, 'TRB'] = cc.at[x, 'TRB'] / 2
            cc.at[x, 'ORB'] = cc.at[x, 'ORB'] / 2
            cc.at[x, 'DRB'] = cc.at[x, 'DRB'] / 2

    cc.G = cc['G'].astype('int')
    cc.PTS = cc['PTS'].astype('int')
    cc.AST = cc['AST'].astype('int')
    cc.TRB = cc['TRB'].astype('int')
    cc.ORB = cc['ORB'].astype('int')
    cc.DRB = cc['DRB'].astype('int')
    cc['ppg'] = cc['PTS'] / cc['G']
    cc['rpg'] = cc['TRB'] / cc['G']
    cc['drpg'] = cc['DRB'] / cc['G']
    cc['orpg'] = cc['ORB'] / cc['G']
    cc['apg'] = cc['AST'] / cc['G']
    return cc
def updateplayer(attr, old, new):
    aa = cleanplayer(df, str(new))
    xp = [x1[1] for x1 in aa.index.values]
    yp = aa['ppg']
    sourceppg.data = ColumnDataSource(data=dict(x=xp, y=yp)).data
    tp = aa['rpg']
    dp = aa['drpg']
    op = aa['orpg']
    ap = aa['apg']
    perp = aa['PER']
    w.y_range.end = tp.max() * 1.4
    i.y_range.start = xp[0]-1
    i.y_range.end = xp[-1]+1
    sourceper.data = ColumnDataSource(data=dict(x=xp, a=perp)).data
    sourcerpg.data = ColumnDataSource(data=dict(x=xp, o=op, d=dp, t=tp)).data
    sourceapg.data = ColumnDataSource(data=dict(x=xp, a=ap)).data
    source.data = ColumnDataSource(aa).data
def updateteam(attr, old, new):
    if str(new) == 'All':
        selectplayer.options = ['All'] + sorted(sorted(list(df['Player'].unique())))
    else:
        selectplayer.options =  ['All']+sorted(newteamsDict[str(new)])
def cleandf(df):
    df.fillna(0, inplace=True)
    df.drop_duplicates(inplace=True)
    df.drop('Unnamed: 0', 1, inplace=True)
    df.Year = df.Year.astype('int')
    df.Age = df.Age.astype('int')
    df.G = df.G.astype('int')
    df.GS = df.GS.astype('int')


    df['ppg'] = df['PTS'] / df['G']
    df['rpg'] = df['TRB'] / df['G']
    df['drpg'] = df['DRB'] / df['G']
    df['orpg'] = df['ORB'] / df['G']
    df['apg'] = df['AST'] / df['G']

    df['Player'] = pd.Series([str(x).replace('*', '') for x in df['Player']], index=df.index)
    return df
def sorting(dict1, tick=1):
    xx=[]
    yy=[]
    aq = sorted(dict1, key = dict1.get, reverse=True)
    for prop in aq:
        xx.append(prop)
        yy.append(dict1[prop])
    if tick == 1:
        yy = [y for y in yy if y > 0]
    xx = xx[:len(yy)]
    return xx, yy

key = 'xx'
lat = 40.391975
lon = -97.685789

df = pd.read_csv('C:/Users/Julien/PycharmProjects/csvsaving/static/Seasons_Stats.csv')
df = cleandf(df)

teams = list(df['Tm'].unique())
teams.remove(0)

teamsDict = {t: set([y[2] for y in df.itertuples() if y[5]==t]) for t in teams}
teamNames = pd.read_csv('C:/Users/Julien/PycharmProjects/csvsaving/static/teams.csv', index_col='Abbrev')
newteamsDict = {teamNames.at[t, 'Name'] :teamsDict[t] for t in teamsDict}

#BOKEH

selectplayer = Select(title='Player:', value='Kevin Durant', options=sorted(list(df['Player'].unique())))
selectplayer.on_change('value', updateplayer)

selectteam = Select(title='Team:', value='All', options=list(['All'] + sorted(list(newteamsDict.keys())))+['All'])
selectteam.on_change('value', updateteam)

source = ColumnDataSource(player_stats(df, str(selectplayer.value)))
button = Button(label="Download Data", button_type="success")
button.callback = CustomJS(args=dict(source=source),
                           code=open(join(dirname(__file__), "download.js")).read())

checkbox_group1 = CheckboxGroup(
        labels=["Average RPG Line", "Average PER Line"], active=[], width = 150)
checkbox_group2 = CheckboxGroup(
        labels=["Average PPG Line", "Average APG Line"], active=[], width = 150)

hoverline = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("PPG", "@y{(0.0)}"), ])
hoverline2 = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("REB", "@t{(0.0)}"),("DREB", "@d{(0.0)}"),("OREB", "@o{(0.0)}")])
hoverline3 = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("APG", "@a{(0.0)}"), ])
hoverbar = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("PER", "@a{(0.0)}"), ])
hoverheatmap = HoverTool(tooltips=[
    ("Area", "@x{0}"),
    ("Shot (%)", "@y{(0.0)}"), ])
p = figure(plot_width=1000, plot_height=450,
           tools=[hoverline, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Points per Game",
           x_axis_type=None,
           y_axis_label="Points (ppg)", toolbar_location="right")
w = figure(plot_width=1000, plot_height=250,
           tools=[hoverline2, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Rebounds per Game",
           x_axis_type=None,
           y_axis_label="Rebounds (rpg)", toolbar_location="right")
z = figure(plot_width=1000, plot_height=250,
           tools=[hoverline3, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Assits per Game",
           x_axis_type=None,
           y_axis_label="Assists (apg)", toolbar_location="right")
i = figure(plot_width=300, plot_height=950,
           tools=[hoverbar, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="PER per season", y_axis_type=None,
           x_axis_label="Player Efficiency Rating", toolbar_location="right")

heatmap = figure(plot_width=350, plot_height=300,
           tools=[hoverheatmap],
           title="Career Shooting Heatmap", x_axis_location=None, y_axis_location=None,toolbar_location="right")
heatmap.rect(-1,0,6,2, color='green', alpha = 0.5, line_color='green')
heatmap.ellipse(1,0,7,1.55, color='firebrick', alpha = 0.5, line_color='white')
heatmap.rect(0,0,2,0.85, color='firebrick', alpha = 0.5, line_color='white')
heatmap.wedge(x=[-1], y=[0], radius=0.98, start_angle=3*pi/2, end_angle=pi/2,
        color="red", alpha=0.6, direction="clock",line_color='white')
heatmap.x_range.end=1
heatmap.x_range.start=-5
heatmap.grid.visible = False

map_options = GMapOptions(lat=lat, lng=lon, map_type="roadmap", zoom=3)
g = gmap(key, map_options, title="Career Stops", width = 350, height = 350)
gsource = ColumnDataSource(data=dict(lat=[ 40.7128,  30.20,  34.0522],lon=[-74.0060, -97.74, -118.2437]))
g.circle(x="lon", y="lat", size=15, fill_color="#568ce2", fill_alpha=0.5, source=gsource)
g.axis.visible = False

a = cleanplayer(df, 'Kevin Durant')
x = [x[1] for x in a.index.values]
y = a['ppg']
sourceppg = ColumnDataSource(data = dict(x=x, y=y))
t = a['rpg']
d = a['drpg']
o = a['orpg']
astt= a['apg']
per = a['PER']
i.y_range=Range1d(x[0]-1, x[-1]+1)
sourceper = ColumnDataSource(data = dict(x=x, a = per))
sourcerpg= ColumnDataSource(data = dict(x=x, o = o, d = d, t = t))
sourceapg = ColumnDataSource(data = dict(x=x, a = astt))
p.line('x', 'y', source=sourceppg, line_width=2.5, line_color='#E24A33',alpha = 0.7)
p.circle('x', 'y', source=sourceppg, size=8, line_color='#E24A33', fill_color = '#568ce2')
z.line('x', 'a', source=sourceapg, line_width=2.5, line_color='#a30693',alpha = 0.7)
z.circle('x', 'a', source=sourceapg, size=8, line_color='#a30693', fill_color = '#568ce2')
w.vbar_stack(stackers=['d','o'], x='x', width=0.5, color=['blue', '#568ce2'], source=sourcerpg,
             legend=['DREB', 'OREB'])

i.hbar(y = 'x', right = 'a', left= 0, height = 0.52, color='#2d0d87', source = sourceper, alpha = 0.7)

ticker = SingleIntervalTicker(interval=1, num_minor_ticks=0)
xaxis = LinearAxis(ticker=ticker)
xaxis2 = LinearAxis(ticker=ticker)
yaxis = LinearAxis(ticker = ticker)

w.add_layout(xaxis2, 'below')
i.add_layout(yaxis, 'left')
w.legend.orientation = 'horizontal'
w.legend.location = "top_left"
w.y_range.end = t.max()*1.4
w.yaxis.major_label_text_font_style = "bold"
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]
w.ygrid.grid_line_alpha = 0.8
w.ygrid.grid_line_dash = [6, 4]
z.ygrid.grid_line_alpha = 0.8
z.ygrid.grid_line_dash = [6, 4]
i.xgrid.grid_line_alpha = 0.8
i.xgrid.grid_line_dash = [6, 4]
checks = row([checkbox_group1,checkbox_group2])
r = column(selectplayer,selectteam, button,checks, width=350)
rr = column([r, heatmap, g])
cc = column([p,z,w])
aavv = row([rr, cc, i])
doc.add_root(aavv)
show(aavv)








