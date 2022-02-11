from db_rih_data_eng import *
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import colorcet as cc
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker, RangeSlider, TextInput
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet, Tabs, Panel, BoxAnnotation
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle, MultiChoice
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout


# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'RIH Data Connectivity'

def update_trendline(old, new, attr):
    pass
def update_device(old, new, attr):
    tt = all_tables_to_query[all_tables_to_query['device']==new]['tl'].unique()
    pprint(sorted(tt))
    select_trendline.options = []
    select_trendline.options = sorted(tt)
def update_button():
    tmp = abc[abc['trendline'] == f"{select_device.value}_{select_trendline.value}"].copy()
    print(tmp.tail().to_string())
    source.data = dict(ColumnDataSource(tmp).data)
def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags_
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""

def update_unit(old, new, attr):
    pass
def update_asset(old, new, attr):
    pass
def update_standard_field_name(old, new, attr):
    pass
def update_search_button():
    pass


start_device = "192000"
start_tl = "tl813"
# abc = get_historical_data(start_date='2022-01-22',end_date='2022-02-09', )
# abc.to_parquet(data_path + 'data.parquet')
# print(all_tables_to_query.to_string())
# print(abc[abc['trendline'] == '141011_tl7'].sort_values('ts').to_string())
abc = pd.read_parquet(data_path + 'data.parquet')

loadsheets, merged = join_raw_data_with_loadsheet(abc)

all_tables_to_query = pd.DataFrame({'point':abc['trendline'].unique()})
all_tables_to_query['tl'] = [str(i[7:]) for i in all_tables_to_query['point']]
all_tables_to_query['device'] = [str(i[:6]) for i in all_tables_to_query['point']]

# data_connectivity_work(merged[merged['tl_type'] == 'COV'])
# a = data_connectivity_work(merged[merged['tl_type'] == 'POLL'],loadsheets)

a = pd.read_parquet(data_path + 'loaded_data.parquet')

low_transmission = a[a['avg_mins_between_points'] > 20].copy()
high_transmission = a[a['avg_mins_between_points'] < 5].copy()

print(low_transmission.sort_values('trendline').to_string())
print(high_transmission.sort_values('trendline').to_string())

##
# TAB 1
top = {}
top["by_hour"] = abc.groupby('hour').agg({'rounded_ts':'count', 'trendline': lambda x: len(set(x))}).reset_index()
top["by_hour"]['hour_offset'] = top["by_hour"]['hour'] + 0.2
top["by_hour"]['trendline_avg'] = top["by_hour"]['trendline'].mean()
top["by_hour"]['rounded_ts_avg'] = top["by_hour"]['rounded_ts'].mean()

top["by_date"] = abc.groupby('date').agg({'rounded_ts':'count', 'trendline': lambda x: len(set(x))}).reset_index()
top["by_date"]['date_offset'] = top["by_date"]['date'] + datetime.timedelta(hours = 5)
top["by_date"]['trendline_avg'] = top["by_date"]['trendline'].mean()
top["by_date"]['rounded_ts_avg'] = top["by_date"]['rounded_ts'].mean()

top["by_month"] = abc.groupby(['month']).agg({'rounded_ts':'count', 'trendline': lambda x: len(set(x))}).reset_index()
top["by_month"]['month_offset'] = top["by_month"]['month'] + 0.2
top["by_month"]['trendline_avg'] = top["by_month"]['trendline'].mean()
top["by_month"]['rounded_ts_avg'] = top["by_month"]['rounded_ts'].mean()

by_hour_source = ColumnDataSource(top['by_hour'])
by_hour_chart = figure(plot_width=1000, plot_height=300, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="Count Trendlines", toolbar_location="right", title= f'Trendlines by Hour')
by_hour_chart.y_range.start = 0
by_hour_chart.extra_y_ranges['right_axis'] = Range1d(start=0, end=top['by_hour']["trendline"].max() * 1.2)
by_hour_chart.add_layout(LinearAxis(y_range_name='right_axis', axis_label='Count Timestamps'), 'right')
anomaly_bars1 = by_hour_chart.vbar(x='hour', top="rounded_ts", source = by_hour_source, color='firebrick', legend_label = "Timestamps", alpha = 0.29, width = 0.1)
anomaly_bars1a = by_hour_chart.vbar(x='hour_offset', top="trendline", source = by_hour_source, color='navy', legend_label = "Unique Trendlines", alpha = 0.29, width = 0.1, y_range_name='right_axis')
anomaly_bars1b = by_hour_chart.line(x='hour', y="trendline_avg", source = by_hour_source, color='navy', legend_label = "Unique Trendlines Avg", alpha = 0.39,  y_range_name='right_axis')
anomaly_bars1c = by_hour_chart.line(x='hour', y="rounded_ts_avg", source = by_hour_source, color='firebrick', legend_label = "Timestamps Avg", alpha = 0.39, )
anomaly_bars1c.visible = False
anomaly_bars1b.visible = False

by_date_source = ColumnDataSource(top['by_date'])
by_date_chart = figure(plot_width=1000, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="Count Trendlines", toolbar_location="right", title= f'Trendlines by Day')
by_date_chart.y_range.start = 0
by_date_chart.extra_y_ranges['right_axis'] = Range1d(start=0, end=top['by_date']["trendline"].max() * 1.2)
by_date_chart.add_layout(LinearAxis(y_range_name='right_axis', axis_label='Count Timestamps'), 'right')
w = 12*60*60*1000 # half day in ms
anomaly_bars2 = by_date_chart.vbar(x='date', top="rounded_ts", source = by_date_source, color='firebrick', legend_label = "Timestamps", alpha = 0.29, width = w/4)
anomaly_bars2a = by_date_chart.vbar(x='date', top="trendline", source = by_date_source, color='navy', legend_label = "Unique Trendlines", alpha = 0.29, width = w/4, y_range_name='right_axis',)
anomaly_bars2b = by_date_chart.line(x='date', y="trendline_avg", source = by_date_source, color='navy', legend_label = "Unique Trendlines Avg", alpha = 0.39,  y_range_name='right_axis')
anomaly_bars2c = by_date_chart.line(x='date', y="rounded_ts_avg", source = by_date_source, color='firebrick', legend_label = "Timestamps Avg", alpha = 0.39, )
anomaly_bars2c.visible = False
anomaly_bars2b.visible = False

by_month_source = ColumnDataSource(top['by_month'])
by_month_chart = figure(plot_width=1000, plot_height=300, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="Count Trendlines", toolbar_location="right", title= f'Trendlines by Month')
by_month_chart.y_range.start = 0
by_month_chart.extra_y_ranges['right_axis'] = Range1d(start=0, end=top['by_month']["trendline"].max() * 1.2)
by_month_chart.add_layout(LinearAxis(y_range_name='right_axis', axis_label='Count Timestamps'), 'right')

anomaly_bars3 = by_month_chart.vbar(x='month', top="rounded_ts", source = by_month_source, color='firebrick', legend_label = "Timestamps", alpha = 0.29, width = 0.1)
anomaly_bars3a = by_month_chart.vbar(x='month_offset', top="trendline", source = by_month_source, color='navy', legend_label = "Unique Trendlines", alpha = 0.29, width = 0.1, y_range_name='right_axis')
anomaly_bars3b = by_month_chart.line(x='month', y="trendline_avg", source = by_month_source, color='navy', legend_label = "Unique Trendlines Avg", alpha = 0.39,  y_range_name='right_axis')
anomaly_bars3c = by_month_chart.line(x='month', y="rounded_ts_avg", source = by_month_source, color='firebrick', legend_label = "Timestamps Avg", alpha = 0.39,)
anomaly_bars3c.visible = False
anomaly_bars3b.visible = False

##
# TAB 2


##
# TAB 3

first = abc[abc['trendline'] == f"{start_device}_{start_tl}"].copy()
# print(abc.describe())
# print(abc.sort_values('ts').to_string())
source = ColumnDataSource(first)

main_chart = figure(plot_width=1100, plot_height=500,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="Temp (F)", toolbar_location="right", title= f'Trendlines')
anomaly_bars = main_chart.vbar(x='rounded_ts', top="value", source = source, color='firebrick', legend_label = "Datapoints", alpha = 0.29, width = 0.1)

select_trendline = Select(title='Trendline', value=start_tl, options=sorted(all_tables_to_query[all_tables_to_query['device']==start_device]['tl'].unique()), width=300)
select_trendline.on_change('value', update_trendline)

select_device = Select(title='Device', value=start_device, options=sorted(all_tables_to_query['device'].unique()), width=300)
select_device.on_change('value', update_device)

button = Button(label="Execute", button_type="primary", width=200)
button.on_click(update_button)

div = Div(text=wrap_in_paragraphs(f"""
Device: {start_device}<br>
Trendline: {start_tl}<br>
point: {start_device}_{start_tl}<br>
name: {loadsheets[loadsheets['objectid'] == f"{start_device}_{start_tl}"]['point_name'].values[0]}
"""))

select_asset = Select(title='Asset', value=start_tl, options=sorted(loadsheets['asset'].unique()), width=300)
select_asset.on_change('value', update_asset)

select_standard_field_name = Select(title='Standard Field Name', value=start_device, options=sorted(loadsheets['standard_field_name'].unique()), width=300)
select_standard_field_name.on_change('value', update_standard_field_name)

select_unit = Select(title='Unit', value=start_tl, options=sorted(loadsheets['units'].unique()), width=300)
select_unit.on_change('value', update_unit)

text_input = TextInput(title='Search Name', value="""P1_MP_04_DSP_AV_POLL_TL""",width=500, height=100)


search_button = Button(label="Search", button_type="warning", width=200)
search_button.on_click(update_search_button)

text_results_div = Div(text= wrap_in_paragraphs("Search for a trendline with it's name: "))

##
# FIRST PAGE
readme_div = Div(text=wrap_in_paragraphs("Readme for this data connectivity Dashboard"))


for plot in [by_date_chart, by_hour_chart, by_month_chart, main_chart]:
    # plot.background_fill_color = '#2c2230'
    plot.axis.minor_tick_line_alpha = 0
    # plot.axis.axis_line_color = '#E6E6E6'
    plot.axis.major_tick_in = -1
    plot.yaxis.axis_label_text_font_size = "13pt"
    plot.xaxis.axis_label_text_font_size = "13pt"
    plot.xaxis.major_label_text_font_size = "13pt"
    plot.yaxis.major_label_text_font_size = "13pt"
    plot.yaxis.major_label_text_font_style = 'bold'
    plot.xaxis.major_label_text_font_style = 'bold'
    plot.yaxis.major_label_text_font = "Arial"
    plot.xaxis.major_label_text_font = "Arial"
    plot.title.align = 'center'
    plot.title.text_font_size = '12pt'
    plot.xaxis.axis_line_width = 0
    plot.yaxis.axis_label_text_font_style = "bold"
    plot.xaxis.axis_label_text_font_style = "bold"
    plot.toolbar.active_scroll = "auto"
    plot.ygrid.grid_line_alpha = 1
    plot.xgrid.grid_line_alpha = 0.5
    plot.outline_line_color = "navy"
    plot.outline_line_width = 3
    plot.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
    try:
        plot.yaxis[1].formatter = NumeralTickFormatter(format="0,0")
    except:
        pass
for plot in [by_date_chart, by_hour_chart, by_month_chart]:
    try:
        plot.add_layout(plot.legend[0], 'above')
        plot.legend.border_line_width = 4
        plot.legend.border_line_color = "navy"
        plot.legend.border_line_alpha = 0.5
        plot.legend.click_policy = 'hide'
        plot.legend.orientation = "horizontal"
    except:
        pass
    # plot.toolbar.autohide = True

tab0 = Panel(child=column([readme_div]), title="README")
tab1 = Panel(child=column([by_date_chart, by_hour_chart, by_month_chart]), title="Data Connectivity Overview")
tab2 = Panel(child=row([column([select_asset, select_standard_field_name, select_unit])]), title="Data Connectivity Analysis")
tab3 = Panel(child=column([row([column([select_trendline, select_device]),div, column([text_input, search_button]), text_results_div]), button, main_chart]), title="Individual Trendlines")

tt = Tabs(tabs=[tab0, tab1, tab2, tab3])
dashboard = row([tt])
print(datetime.datetime.now()-today)
curdoc().add_root(dashboard)
show(dashboard)
