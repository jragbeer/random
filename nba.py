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

doc = curdoc()
doc.title = 'NBA Stats'
#clears the html page and gives the tab a name
doc.clear()
def makediv(df, teams):
    text = '''<br><font color="#113672" size = "3"><b>Player: </b></font><br><br>
    <font color="#e82751" size = "5"><b>{}</b></font><br><br>
    <font color="#113672" size = "3"><b>Teams played on: </b></font><br><br>
    <font color="#e82751" size = "4"><b>{}</b></font><br><br>
    <font color="#113672" size = "3"><b>Games Played: </b></font>
    <font color="#e82751" size = "5"><b>{:d}</b></font><br><br>
    <font color="#113672" size = "3"><b>Years Active: </b></font>
    <font color="#e82751" size = "5"><b>{:d}</b></font><font color="#e82751" size = "3"><b>  ({:d}-{:d})</b></font><br><br>
    <font color="#113672" size = "3"><b>Career Average PPG: </b></font>
    <font color="#e82751" size = "5"><b>{:.1f}</b></font><br><br>
    <font color="#113672" size = "3"><b>Career Average APG: </b></font>
    <font color="#e82751" size = "5"><b>{:.1f}</b></font><br><br>
    <font color="#113672" size = "3"><b>Career Average RPG: </b></font>
    <font color="#e82751" size = "5"><b>{:.1f}</b></font>'''.format(
        selectplayer.value, ', '.join(teams), int(df['G'].sum()), int(len(df['G'])),df.index.levels[1].values[0],df.index.levels[1].values[-1], df['ptsavg'].mean(), df['astavg'].mean(), df['rebavg'].mean())
    return text
def player_stats(df, name):
    player = df[df['Player'] == str(name)].copy()
    return player
def cleanplayer(df, player):
    aa = player_stats(df, player)
    cc = pd.DataFrame(aa.groupby(['Player', 'Year']).agg({'TRB':'sum', 'AST':'sum', 'PTS':'sum', 'G':'sum', 'DRB':'sum', 'ORB':'sum','FTA':'sum','FT':'sum','FGA':'sum','FG':'sum','3PA':'sum','3P':'sum', 'PER':'mean'}))

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
    cc['rebavg'] = cc['TRB'].sum() / cc['G'].sum()
    cc['ptsavg'] = cc['PTS'].sum() / cc['G'].sum()
    cc['astavg'] = cc['AST'].sum() / cc['G'].sum()
    cc['orbavg'] = cc['ORB'].sum() / cc['G'].sum()
    cc['drbavg'] = cc['DRB'].sum() / cc['G'].sum()


    return cc
def updateplayer(attr, old, new):
    teamlistp = [list(y) for x in player_stats(df, str(new))['Tm'].unique() for y in teamNames.itertuples() if
                x == y[0] and x != 'TOT']
    try:
        teamlistp.remove('Multiple Teams in a season')
    except:
        pass
    aa = cleanplayer(df, str(new))
    xp = [x1[1] for x1 in aa.index.values]
    yp = aa['ppg']

    tp = aa['rpg']
    dp = aa['drpg']
    op = aa['orpg']
    ap = aa['apg']
    perp = aa['PER']
    astavgp = aa['astavg']
    rebavgp = aa['rebavg']
    ptsavgp = aa['ptsavg']
    orbavgp = aa['orbavg']
    drbavgp = aa['drbavg']
    sourceppg.data = ColumnDataSource(data=dict(x=xp, y=yp, avg = ptsavgp)).data

    w.y_range.end = tp.max() * 1.4
    i.y_range.start = xp[0]-1
    i.y_range.end = xp[-1]+1
    gsource.data = ColumnDataSource(
        data=dict(lat=[x[3] for x in teamlistp], lon=[x[4] for x in teamlistp], city=[x[2] for x in teamlistp])).data
    sourceper.data = ColumnDataSource(data=dict(x=xp, a=perp)).data
    sourcerpg.data = ColumnDataSource(data=dict(x=xp, o=op, d=dp, t=tp, avgt=rebavgp, avgo = orbavgp, avgd = drbavgp)).data
    sourceapg.data = ColumnDataSource(data=dict(x=xp, a=ap, avg = astavgp)).data
    source.data = ColumnDataSource(aa).data
    div.text = makediv(aa, [x[1] for x in teamlistp])
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
def update_plot4(new):

    if checkbox_group4.active ==[0]:
        avglinep.visible = True

    else:
        avglinep.visible = False
def update_plot3(new):
    if checkbox_group3.active ==[0]:
        avglinez.visible = True

    else:
        avglinez.visible = False
def update_plot1(new):
    if checkbox_group1.active ==[0]:
        avglinewo.visible = True
        avglinewd.visible = True
        avglinewt.visible = True
    else:
        avglinewo.visible = False
        avglinewd.visible = False
        avglinewt.visible = False

key = 'xx'
lat = 40.391975
lon = -97.685789

direc = 'xx'

df = pd.read_csv(direc + 'Seasons_Stats.csv')
df = cleandf(df)

teams = list(df['Tm'].unique())
teams.remove(0)

teamsDict = {t: set([y[2] for y in df.itertuples() if y[5]==t]) for t in teams}
teamNames = pd.read_csv(direc + 'teams.csv', index_col='Abbrev')

newteamsDict = {teamNames.at[t, 'Name'] :teamsDict[t] for t in teamsDict}

teamabbrevdict = {teamNames.index[x]:str(teamNames.values[x][0].strip()) for x in range(len(teamNames))}
teamlist = [list(y) for x in player_stats(df, 'Kevin Durant')['Tm'].unique() for y in teamNames.itertuples() if x == y[0] and x != 'TOT']

#BOKEH


selectplayer = Select(title='Player:', value='Kevin Durant', options=sorted(list(df['Player'].unique())))
selectplayer.on_change('value', updateplayer)

selectteam = Select(title='Team:', value='All', options=list(['All'] + sorted(list(newteamsDict.keys())))+['All'])
selectteam.on_change('value', updateteam)

source = ColumnDataSource(player_stats(df, str(selectplayer.value)))
button = Button(label="Download Data", button_type="success")
button.callback = CustomJS(args=dict(source=source),code=open(join(dirname(__file__), "download.js")).read())


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
hovermap = HoverTool(tooltips=[
    ("City", "@city"),])
p = figure(plot_width=950, plot_height=450,
           tools=[hoverline, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Points per Game",x_axis_type=None,y_axis_label="Points (ppg)", toolbar_location="right")
w = figure(plot_width=950, plot_height=250,
           tools=[hoverline2, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Rebounds per Game",x_axis_type=None, y_axis_label="Rebounds (rpg)", toolbar_location="right")
z = figure(plot_width=950, plot_height=250,
           tools=[hoverline3, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Assits per Game", x_axis_type=None, y_axis_label="Assists (apg)", toolbar_location="right")
i = figure(plot_width=300, plot_height=950,
           tools=[hoverbar, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="PER per season", y_axis_type=None, x_axis_label="Player Efficiency Rating", toolbar_location="right")

heatmap = figure(plot_width=350, plot_height=300,
           tools=[hoverheatmap],title="Career Shooting Heatmap", x_axis_location=None, y_axis_location=None,toolbar_location="right")
hmapsq = heatmap.rect(-1,0,6,2, color='green', line_color='green')
hmapellipse = heatmap.ellipse(1,0,7,1.55, color='firebrick', line_color='white')
hmaprect = heatmap.rect(0,0,2,0.85, color='firebrick', line_color='white')
hmapwedge = heatmap.wedge(x=[-1], y=[0], radius=0.98, start_angle=3*pi/2, end_angle=pi/2,
        color="red",  direction="clock",line_color='white')
heatmap.x_range.end=1
heatmap.x_range.start=-5
heatmap.grid.visible = False
heatmap.outline_line_color = None

# map_options = GMapOptions(lat=lat, lng=lon, map_type="roadmap", zoom=3)
# g = gmap(key, map_options, title="Career Stops", width = 350, height = 350)
g = figure(plot_width=350, plot_height=350,
           tools=[hovermap],
           title="Map", x_axis_location=None, y_axis_location=None,toolbar_location="right")
gsource = ColumnDataSource(data=dict(lat=[x[3] for x in teamlist],lon=[x[4] for x in teamlist], city = [x[2] for x in teamlist]))
g.circle(x="lon", y="lat", size=12, fill_color="#c157f2", fill_alpha=0.8, source=gsource)
g.axis.visible = False
g.add_tools(hovermap)

a = cleanplayer(df, 'Kevin Durant')
x = [x[1] for x in a.index.values]
y = a['ppg']
t = a['rpg']
d = a['drpg']
o = a['orpg']
astt = a['apg']
per = a['PER']
peravg = [a['PER'].sum()/len(x) for y in range(len(x))]
rebavg = a['rebavg']
ptsavg = a['ptsavg']
astavg = a['astavg']
orbavg = a['orbavg']
drbavg = a['drbavg']

htmap3 = a['3P'].sum()/a['3PA'].sum()
htmapft = a['FT'].sum()/a['FTA'].sum()
htmapfg = a['FG'].sum()/a['FGA'].sum()
# heatmapsource = ColumnDataSource(data = dict(three = htmap3, ft = htmapft, fg = htmapfg))

if htmap3 < 20:
    print("pink")
elif 20<=htmap3 < 40:
    print("orange")
elif htmap3 >= 40:
    print('blue')


color_mapper = LinearColorMapper(palette=Purples[9][::-1][3:], low=min(per), high=max(per))
i.y_range=Range1d(x[0]-1, x[-1]+1)
sourceppg = ColumnDataSource(data = dict(x=x, y=y, avg = ptsavg))
sourceper = ColumnDataSource(data = dict(x=x, a = per, avg = peravg))
sourcerpg= ColumnDataSource(data = dict(x=x, o = o, d = d, t = t, avgt=rebavg, avgo = orbavg, avgd = drbavg))
sourceapg = ColumnDataSource(data = dict(x=x, a = astt, avg = astavg))
p.line('x', 'y', source=sourceppg, line_width=2.5, line_color='#E24A33',alpha = 0.7)
p.circle('x', 'y', source=sourceppg, size=8, line_color='#E24A33', fill_color = '#568ce2')
z.line('x', 'a', source=sourceapg, line_width=2.5, line_color='#a30693',alpha = 0.7)
z.circle('x', 'a', source=sourceapg, size=8, line_color='#a30693', fill_color = '#568ce2')
w.vbar_stack(stackers=['d','o'], x='x', width=0.5, color=['blue', '#568ce2'], source=sourcerpg,
             legend=['DREB', 'OREB'])

i.hbar(y = 'x', right = 'a', left= 0, height = 0.52, color={'field': 'a', 'transform': color_mapper}, source = sourceper)

avglinep = p.line('x', 'avg', source=sourceppg, line_width=3.5, line_color='#E24A33', alpha = 0.2)
avglinewt = w.line('x', 'avgt', source=sourcerpg, line_width=3.5, line_color='purple', alpha = 0.2)
avglinewo = w.line('x', 'avgo', source=sourcerpg, line_width=3.5, line_color='#568ce2', alpha = 0.2)
avglinewd = w.line('x', 'avgd', source=sourcerpg, line_width=3.5, line_color='blue', alpha = 0.2)
avglinez = z.line('x', 'avg', source=sourceapg, line_width=3.5, line_color='#a30693', alpha = 0.2)

avglinewd.visible = False
avglinewo.visible = False
avglinez.visible = False
avglinewt.visible = False
avglinep.visible = False

checkbox_group1 = CheckboxGroup(labels=["Average RPG Lines"], active=[], width = 150)
checkbox_group3 = CheckboxGroup(labels=["Average APG Line"], active=[], width = 150)
checkbox_group4 = CheckboxGroup(labels=["Average PPG Line"], active=[], width = 150)
checkbox_group1.on_click(update_plot1)
checkbox_group3.on_click(update_plot3)
checkbox_group4.on_click(update_plot4)

img = figure(plot_width=300, plot_height=200, x_range=(0, 370), y_range=(0, 834), x_axis_type=None,y_axis_type=None,tools = [])
img.image_url(url=['csvsaving/static/kevin.png'],x=0, y=0, w=369, h=834,anchor="bottom_left")
img.grid.visible = False
img.outline_line_color = None

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

div = Div(width = 300, height = 500, text = makediv(a, [x[1] for x in teamlist]))

r = column(selectplayer,selectteam, button,checkbox_group4,checkbox_group3,checkbox_group1,img, div, width=300)
rr = column([heatmap, g])
cc = column([p,z,w])
aavv = row([r, cc, i, rr])
doc.add_root(aavv)
show(aavv)








