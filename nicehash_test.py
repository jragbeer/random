from nicehash import *
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
import time

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'NiceHash Mining Rig Performance'

pd.set_option('display.float_format', lambda x: '%.10f' % x)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

today = datetime.datetime.now()

df = pd.read_sql('select * from most_recent_rig_device_stats', sql_engine, parse_dates='timestamp')
df = df[df['timestamp'] > pd.to_datetime(datetime.datetime(2021,4,24))]
print(df.tail().to_string())

def make_data(fdf, rig_nm, resample='H'):
    idf = fdf[fdf['rig_name'] == rig_nm.lower()].copy()
    idf = idf.groupby('timestamp').agg({'speed':np.sum, 'power_usage':np.sum,})
    idf.index = pd.to_datetime(idf.index)
    idf = idf.resample(resample).mean()
    idf.fillna(0, inplace=True)
    for x in [5, 10, 14, 28]:
        idf[f'rolling_{x}'] = idf['speed'].rolling(x).mean()
    for i in idf.itertuples():
        if i.speed > 5*i.rolling_10:
            idf.at[i.Index, 'speed'] = i.speed/1000
    return idf

source_amd = ColumnDataSource(make_data(df, 'AMDBuster'))
amd_speed_chart = figure(plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'AMDBuster MH/s')
amd_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
amd_speed_chart.y_range.start = 0

amd_line = amd_speed_chart.line(x="timestamp", y='speed', source=source_amd,  alpha = 0.3, color = 'firebrick', legend_label= 'Speed', line_width = 3)
amd_circle = amd_speed_chart.circle(x="timestamp", y='speed', source=source_amd, size = 3, color = 'firebrick')

source_leader = ColumnDataSource(make_data(df, 'Leader'))
leader_speed_chart = figure(x_range=amd_speed_chart.x_range,plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'Leader MH/s')
leader_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
leader_speed_chart.y_range.start = 0

leader_line = leader_speed_chart.line(x="timestamp", y='speed', source=source_leader,  alpha = 0.3, color = 'navy', legend_label= 'Speed', line_width = 3)
leader_circle = leader_speed_chart.circle(x="timestamp", y='speed', source=source_leader, size = 3, color = 'navy')

source_wh = ColumnDataSource(make_data(df, 'Workhorse1080'))
wh_speed_chart = figure(x_range=amd_speed_chart.x_range,plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'Workhorse1080 MH/s')
wh_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
wh_speed_chart.y_range.start = 0

wh_line = wh_speed_chart.line(x="timestamp", y='speed', source=source_wh,  alpha = 0.3, color = 'green', legend_label= 'Speed', line_width = 3)
wh_circle = wh_speed_chart.circle(x="timestamp", y='speed', source=source_wh, size = 3, color = 'green')

bigger = {"Leader": {}, "AMDBuster":{}, "Workhorse1080":{}}
for k, v in bigger.items():
    for minss in ['15min', '30min', 'H', '4H']:
        cool=make_data(df, k, resample=minss)
        dt_range = pd.date_range(start = cool.index.min(), end = cool.index.max(), freq=minss)
        ddf = pd.DataFrame([1 for _ in range(len(dt_range))], index=dt_range)
        final = pd.merge(ddf, cool, how='left', left_index=True, right_index=True)
        final.fillna(0, inplace=True)
        duh = []
        ops = []
        for z in final['speed']:
            if z > 25:
               duh.append(0)
            if z > 80:
                ops.append(9)
        bigger[k][minss] = {'length':len(final.index), 'on':len(duh), 'operational':len(ops)}

zz = pd.concat({k:pd.DataFrame(v).T for k,v in bigger.items()})
zz.reset_index(inplace=True)
zz.columns = ['rig', 'time_period', 'length', 'on', 'operational']
new = zz.groupby(['time_period']).sum()
for x in [new, zz]:
    x['on_pct'] = np.round(100*x["on"]/x['length'],1)
    x['ops_pct'] = np.round(100*x["operational"]/x['length'],1)
print(zz)
print(new)
dashboard = column([amd_speed_chart, leader_speed_chart, wh_speed_chart])
curdoc().add_root(dashboard)
show(dashboard)
