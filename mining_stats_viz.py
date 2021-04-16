from nicehash import *
import matplotlib.pyplot as plt
import seaborn
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout

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
# print(algos_df.to_string())
# print("*"*8)

print(abc().to_string())

payout_data = get_payout_data()
print(payout_data.to_string())
payout_data.to_sql(f"payout_data_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False)
pprint(private_api.rig_status())

miner_stats_df = miner_statistics()
# miner_stats_df.to_parquet(data_path + "miner_stats_april_15_2021.parquet")
payout_data.to_sql(f"miner_stats_{today.strftime('%Y_%m_%d_%H_%M')}", sql_engine, if_exists='replace', index=False,)
print(miner_stats_df.to_string())
miner_stats_df_hourly = miner_stats_df.set_index('time_datetime').resample('H').mean().reset_index()
miner_stats_df_hourly['avg_24'] = miner_stats_df_hourly['speed_accepted'].rolling(24).mean()

payout_chart = figure(plot_width=1200, plot_height=800,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="BTC", toolbar_location="right", title= 'Payout')
payout_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.000000")
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
payout_chart.line(x="timestamp", y='net_amount', source=source, line_width=4, line_dash='dotted', alpha = 0.3, color = 'red')
payout_chart.circle(x="timestamp", y='net_amount', source=source, size = 4, color = 'red')

payout_chart.line(x="timestamp", y='gross_amount', source=source, line_width=4, line_dash='dotted', alpha = 0.3 )
payout_chart.circle(x="timestamp", y='gross_amount', source=source, size = 4)

payout_chart.line(x="timestamp", y='nh_fee', source=source, line_width=4, line_dash='dotted', alpha = 0.3 , color = 'green')
payout_chart.circle(x="timestamp", y='nh_fee', source=source, size = 4, color = 'green')

miner_stats_chart = figure(plot_width=650, plot_height=400,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="Speed (MH/s)", toolbar_location="right", title= 'Hashrate (MH/s)')
miner_stats_chart.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
miner_stats_chart.y_range.start = 50

source2 = ColumnDataSource(data=miner_stats_df_hourly)
miner_stats_chart.line(x="time_datetime", y='speed_accepted', source=source2, line_width=4, line_dash='dotted', alpha = 0.37 , color = 'green', legend_label= 'Hashrate')
miner_stats_chart.circle(x="time_datetime", y='speed_accepted', source=source2, size = 4, color = 'green')
miner_stats_chart.line(x="time_datetime", y='avg_24', source=source2, line_width=3, color = 'darkorange', legend_label= '24-hr Rolling Avg')
miner_stats_chart.legend.location = 'bottom_left'

other_chart = figure(plot_width=650, plot_height=400,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Datetime", y_axis_label="BTC", toolbar_location="right", title= 'Payout')


# pretty up the dashboard
for p in [payout_chart, other_chart, miner_stats_chart]:

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

dashboard = row([ payout_chart, column([miner_stats_chart, other_chart])])
curdoc().add_root(dashboard)
show(dashboard)
