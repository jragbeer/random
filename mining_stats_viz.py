from nicehash import *
import matplotlib.pyplot as plt
import seaborn
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
doc.title = 'NiceHash Mining'

pd.set_option('display.float_format', lambda x: '%.10f' % x)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

today = datetime.datetime.now()

algos = public_api.get_algorithms()
algos_df = pd.DataFrame(algos['miningAlgorithms'])
algos_df.to_sql(f"mining_algorithms_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False)

pprint(private_api.rig_status())
dumb = get_active_workers_stats()
print(dumb.to_string())
dumb.to_sql(f"active_workers_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False)

payout_data = get_payout_data()
payout_data['avg_6'] = payout_data['net_amount'].rolling(6).mean()
payout_data['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in payout_data['timestamp']]
payout_data.to_sql(f"payout_data_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False)



miner_stats_df = miner_statistics()
miner_stats_df.to_sql(f"miner_stats_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False,)

miner_stats_df_hourly = miner_stats_df.set_index('time_datetime').resample('H').mean().reset_index()
miner_stats_df_hourly['avg_24'] = miner_stats_df_hourly['speed_accepted'].rolling(24).mean()
miner_stats_df_hourly['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in miner_stats_df_hourly['time_datetime']]

payout_chart = figure(plot_width=1200, plot_height=800,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="BTC", toolbar_location="right", title= 'Payout')
payout_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.00000")
payout_chart.y_range.start = 0
# # HOVERTOOLS
# payout_chart.add_tools(HoverTool(tooltips=[
#     ("Strain", "@info"),("Deaths", "@deaths{(0,0)}"),("Population", "@pop{(0,0)}"),]))
# # MEAN LINE SPAN
# span = Span(location=np.nanmean(data['Deaths']), dimension='width', line_color='firebrick', line_width=3, line_alpha= 0.43)
# payout_chart.add_layout(span)
# my_label = Label(x=5, y=np.nanmean(data['Deaths']) + 10, text='MEAN LINE', text_color='firebrick',
#                  text_alpha=0.43, text_font_style='bold')
# payout_chart.add_layout(my_label)

source = ColumnDataSource(data=payout_data)
net_line = payout_chart.line(x="timestamp", y='net_amount', source=source, line_width=4, line_dash='dotted', alpha = 0.3, color = 'blue', legend_label= 'Net Amount')
net_circle = payout_chart.circle(x="timestamp", y='net_amount', source=source, size = 4, color = 'blue')

gross_line = payout_chart.line(x="timestamp", y='gross_amount', source=source, line_width=4, line_dash='dotted', alpha = 0.3, legend_label= 'Gross Amount', color = 'grey' )
gross_circle = payout_chart.circle(x="timestamp", y='gross_amount', source=source, size = 4, color = 'grey')
gross_circle.visible = False
gross_line.visible = False

nh_fee = payout_chart.circle(x="timestamp", y='nh_fee', source=source, size = 4, color = 'green', legend_label= 'NH Fee')
avg_6 = payout_chart.line(x="timestamp", y='avg_6', source=source, line_width=3, color = 'darkorange', legend_label= '24-hr Rolling Avg')

payout_chart.legend.location = 'top_left'
payout_chart.legend.click_policy = 'hide'
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Fee", "@nh_fee{(0.000000)}")], mode='vline', renderers=[nh_fee]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Net", "@net_amount{(0.000000)}")], mode='vline', renderers=[net_line]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Gross", "@gross_amount{(0.000000)}")], mode='vline', renderers=[gross_line]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Avg 6", "@avg_6{(0.000000)}")], mode='vline', renderers=[avg_6]))

miner_stats_chart = figure(plot_width=650, plot_height=400,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="Speed (MH/s)", toolbar_location="right", title= 'Hashrate (MH/s)')
miner_stats_chart.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
miner_stats_chart.y_range.start = 50

source2 = ColumnDataSource(data=miner_stats_df_hourly)
speed_accepted = miner_stats_chart.line(x="time_datetime", y='speed_accepted', source=source2, line_width=4, line_dash='dotted', alpha = 0.37 , color = 'green', legend_label= 'Hashrate')
miner_stats_chart.circle(x="time_datetime", y='speed_accepted', source=source2, size = 4, color = 'green')
avg_24 = miner_stats_chart.line(x="time_datetime", y='avg_24', source=source2, line_width=3, color = 'darkorange', legend_label= '24-hr Rolling Avg')
miner_stats_chart.legend.location = 'bottom_left'
miner_stats_chart.legend.click_policy = 'hide'
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("24-hr Rolling", "@avg_24{(0,0.0)}"),], mode='vline', renderers=[avg_24]))
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Hashrate", "@speed_accepted{(0,0.0)}"),], mode='vline', renderers=[speed_accepted]))


total_mined_chart = figure(plot_width=650, plot_height=400,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="BTC", toolbar_location="right", title= 'Payout')
total_mined_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0000")
total_mined_chart.y_range.start = 0

net_cumsum_line = total_mined_chart.line(x="timestamp", y='net_amount_cumsum', source=source, line_width=4, line_dash='dotted', alpha = 0.3, color = 'goldenrod')
total_mined_chart.circle(x="timestamp", y='net_amount_cumsum', source=source, size = 3, color = 'goldenrod')
total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Collected BTC", "@net_amount_cumsum{(0,0.00000)}"),], mode='vline', renderers=[net_cumsum_line]))

# pretty up the dashboard
for p in [payout_chart, total_mined_chart, miner_stats_chart]:
    p.xaxis.major_label_orientation = np.pi/4
    p.axis.minor_tick_line_alpha = 0
    p.axis.major_tick_in = -1
    p.yaxis.axis_label_text_font_size = "13pt"
    p.xaxis.axis_label_text_font_size = "13pt"
    p.xaxis.major_label_text_font_size = "13pt"
    p.yaxis.major_label_text_font_size = "13pt"
    p.yaxis.major_label_text_font_style = 'bold'
    p.xaxis.major_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font = "Arial"
    p.xaxis.major_label_text_font = "Arial"
    p.title.align = 'center'
    p.title.text_font_size = '12pt'
    p.xaxis.axis_line_width = 0
    p.yaxis.axis_label_text_font_style = "bold"
    p.xaxis.axis_label_text_font_style = "bold"
    p.toolbar.active_scroll = "auto"

dashboard = row([ payout_chart, column([miner_stats_chart, total_mined_chart])])
curdoc().add_root(dashboard)
show(dashboard)
