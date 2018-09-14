import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
from datetime import timezone
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, CustomJS, DatetimeTickFormatter
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter, Band, SingleIntervalTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Button, CheckboxGroup
from bokeh.layouts import widgetbox, row, column
from bokeh.io import curdoc
import webbrowser
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

checkbox_group = CheckboxGroup(
        labels=["Average PPG Line", "Average APG Line", "Average RPG Line", "Average PER Line"], active=[])

hoverline = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("PPG", "$y{(0.0)}"), ])
hoverline2 = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("RPG", "$y{(0.0)}"), ])
hoverline3 = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("APG", "@a{(0.0)}"), ])
hoverbar = HoverTool(tooltips=[
    ("Year", "@x{0}"),
    ("PER", "@a{(0.0)}"), ])
p = figure(plot_width=1000, plot_height=400,
           tools=[hoverline, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Points per Game",
           x_axis_type=None,
           y_axis_label="Points (ppg)", toolbar_location="right")
w = figure(plot_width=1000, plot_height=200,
           tools=[hoverline2, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Rebounds per Game",
           x_axis_type=None,
           y_axis_label="Rebounds (rpg)", toolbar_location="right")
z = figure(plot_width=1000, plot_height=200,
           tools=[hoverline3, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="Average Assits per Game",
           x_axis_type=None,
           y_axis_label="Assists (apg)", toolbar_location="right")
i = figure(plot_width=300, plot_height=800,
           tools=[hoverbar, BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           title="PER per season", y_axis_type=None,
           x_axis_label="Player Efficiency Rating", toolbar_location="right")

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
p.circle('x', 'y', source=sourceppg, size=8, line_color='#E24A33', fill_color = '#E24A33')
z.line('x', 'a', source=sourceapg, line_width=2.5, line_color='#568ce2',alpha = 0.7)
z.circle('x', 'a', source=sourceapg, size=8, line_color='#568ce2', fill_color = '#568ce2')
w.line('x', 't', source=sourcerpg, line_width=2.5, line_color='orange', legend='TRPG', alpha = 0.7)
w.line('x', 'd', source=sourcerpg, line_width=2.5, line_color='blue', legend='DRPG', alpha = 0.7)
w.line('x', 'o', source=sourcerpg, line_width=2.5, line_color='yellow', legend='ORPG', alpha = 0.7)
w.circle('x', 't', source=sourcerpg, size=6, line_color='orange',fill_color = 'orange', legend='TRPG')
w.circle('x', 'd', source=sourcerpg, size=6, line_color='blue', legend='DRPG',fill_color = 'blue')
w.circle('x', 'o', source=sourcerpg, size=6, line_color='yellow', legend='ORPG',fill_color = 'yellow')

i.hbar(y = 'x', right = 'a', left= 0, height = 0.75, color='#2d0d87', source = sourceper, alpha = 0.7)

ticker = SingleIntervalTicker(interval=1, num_minor_ticks=0)
xaxis = LinearAxis(ticker=ticker)
xaxis2 = LinearAxis(ticker=ticker)
yaxis = LinearAxis(ticker = ticker)
p.add_layout(xaxis, 'below')
w.add_layout(xaxis2, 'below')
i.add_layout(yaxis, 'left')
w.legend.orientation = 'horizontal'
w.legend.location = "top_left"
w.y_range.end = t.max()*1.4

r = widgetbox(selectplayer,selectteam, button,checkbox_group,width=300)
cc = column([p,z,w])
aavv = row([r, cc, i])
doc.add_root(aavv)
# show(aavv)









