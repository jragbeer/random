from nicehash import *
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet, Tabs, Panel
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
import time
import yfinance as yf

def wrap_in_paragraphs(text, colour="DarkSlateBlue", size=4):
    """
    This function wraps text in paragraph, bold and font tags - according to the colour and size given.
    :param text: text to wrap in tags
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return """<p><b><font color={} size={}>{}</font></b></p>""".format(colour, size, text)

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'NiceHash Mining'

pd.set_option('display.float_format', lambda x: '%.10f' % x)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

today = datetime.datetime.now()

cur_BTCCAD = yf.Ticker("BTC-CAD").history(period="5d")['Close'][-1]
cur_ETHCAD = yf.Ticker("ETH-CAD").history(period="5d")['Close'][-1]
cur_BTCUSD = yf.Ticker("BTC-USD").history(period="5d")['Close'][-1]
cur_ETHUSD = yf.Ticker("ETH-USD").history(period="5d")['Close'][-1]

sql_table_info = get_names_of_latest_tables(sql_engine)

coinbase_data = clean_coinbase_data()
coinbase_sell_data = coinbase_data[(coinbase_data['Transaction'] == 'Sell') & (coinbase_data['Asset'] == 'BTC')]
coinbase_buy_data = coinbase_data[(coinbase_data['Transaction'] == 'Buy') & (coinbase_data['Asset'] == 'BTC')]

kk = coinbase_sell_data.sum()[['Quantity','Subtotal', 'Total', "Fees"]]
qqq = coinbase_buy_data.sum()[['Quantity','Subtotal', 'Total', "Fees"]]
# payout data
payout_data = get_payout_data_df(sql_table_info)
payout_data['avg_6'] = payout_data['net_amount'].rolling(6).mean()
payout_data['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in payout_data['timestamp']]
payout_data['net_amount_cumsum'] = payout_data['net_amount'].cumsum()  # total bitcoin recieved
payout_data['total_mined_dollars_converted_now'] = payout_data['net_amount_cumsum'] * cur_BTCCAD

payout_data_daily = payout_data.set_index("timestamp").resample('D').sum()[['gross_amount', 'net_amount']]
for x in [5,10, 14, 28]:
    payout_data_daily[f'rolling_{x}'] = payout_data_daily['net_amount'].rolling(x).mean()
    payout_data_daily[f'rolling_{x}_price'] = payout_data_daily[f'rolling_{x}']*67000 #55000 USD

# miner statistics data
miner_stats_df = get_miner_stats_df(sql_table_info)
miner_stats_df_hourly = miner_stats_df.set_index('time_datetime').resample('H').mean().reset_index()
miner_stats_df_hourly['speed_accepted'] = miner_stats_df_hourly['speed_accepted'].fillna(0)
miner_stats_df_hourly['avg_24'] = miner_stats_df_hourly['speed_accepted'].rolling(24).mean()
miner_stats_df_hourly['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in miner_stats_df_hourly['time_datetime']]

payout_chart = figure(plot_width=1200, plot_height=650,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="BTC", toolbar_location="right", title= 'Payout')
payout_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.00000")
payout_chart.y_range.start = 0

source = ColumnDataSource(data=payout_data)
net_line = payout_chart.vbar(x="timestamp", top='net_amount',bottom=0, source=source,  alpha = 0.3, color = 'blue', legend_label= 'Net Amount')
net_circle = payout_chart.circle(x="timestamp", y='net_amount', source=source, size = 0.5, color = 'blue')

gross_line = payout_chart.line(x="timestamp", y='gross_amount', source=source, line_width=4, line_dash='dotted', alpha = 0.3, legend_label= 'Gross Amount', color = 'grey' )
gross_circle = payout_chart.circle(x="timestamp", y='gross_amount', source=source, size = 4, color = 'grey')
gross_circle.visible = False
gross_line.visible = False

nh_fee = payout_chart.circle(x="timestamp", y='nh_fee', source=source, size = 4, color = 'green', legend_label= 'NH Fee')
avg_6 = payout_chart.line(x="timestamp", y='avg_6', source=source, line_width=3, color = 'mediumvioletred', legend_label= '24-hr Rolling Avg')

payout_chart.legend.location = 'top_left'
payout_chart.legend.click_policy = 'hide'
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Fee", "@nh_fee{(0.000000)}")], mode='vline', renderers=[nh_fee]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Net", "@net_amount{(0.000000)}")], mode='vline', renderers=[net_line]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Gross", "@gross_amount{(0.000000)}")], mode='vline', renderers=[gross_line]))
payout_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Avg 6", "@avg_6{(0.000000)}")], mode='vline', renderers=[avg_6]))

miner_stats_chart = figure(plot_width=650, plot_height=325,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="Speed (MH/s)", toolbar_location="right", title= 'Hashrate (MH/s)')
miner_stats_chart.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
miner_stats_chart.y_range.start = 100

source2 = ColumnDataSource(data=miner_stats_df_hourly)
speed_accepted = miner_stats_chart.line(x="time_datetime", y='speed_accepted', source=source2, line_width=4, line_dash='dotted', alpha = 0.37 , color = 'green', legend_label= 'Hashrate')
miner_stats_chart.circle(x="time_datetime", y='speed_accepted', source=source2, size = 4, color = 'green')
avg_24 = miner_stats_chart.line(x="time_datetime", y='avg_24', source=source2, line_width=3, color = 'darkorange', legend_label= '24-hr Rolling Avg')
miner_stats_chart.legend.location = 'bottom_left'
miner_stats_chart.legend.click_policy = 'hide'
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("24-hr Rolling", "@avg_24{(0,0.0)}"),], mode='vline', renderers=[avg_24]))
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Hashrate", "@speed_accepted{(0,0.0)}"),], mode='vline', renderers=[speed_accepted]))

total_mined_chart = figure(plot_width=650, plot_height=325,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()], x_axis_label=None, y_axis_label="BTC", toolbar_location="right", title= 'Payout')
total_mined_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0000")
total_mined_chart.y_range.start = 0

net_cumsum_line = total_mined_chart.line(x="timestamp", y='net_amount_cumsum', source=source, line_width=4, line_dash='dotted', alpha = 0.3, color = 'firebrick')
total_mined_chart.circle(x="timestamp", y='net_amount_cumsum', source=source, size = 3, color = 'firebrick')
total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Collected BTC", "@net_amount_cumsum{(0,0.00000)}"),("Collected BTC * BTC Price", "@total_mined_dollars_converted_now{(0,0)}"),], mode='vline', renderers=[net_cumsum_line]))

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

blank_divs = {x:Div(text='', width = 1) for x in range(10)}

div1 = Div(text=wrap_in_paragraphs(f'Last BTC Payout:<br><font size=7>{payout_data["net_amount"].iloc[max(payout_data.index)]:.6f}</font>', 'blue'), width = 250)
div2 = Div(text=wrap_in_paragraphs(f'24hr Avg Amt/Payout:<br><font size=7>{payout_data["avg_6"].iloc[max(payout_data.index)]:.6f}</font>', 'mediumvioletred'), width = 250)
div5 = Div(text=wrap_in_paragraphs(f'Most Recent Hashrate:<br><font size=7>{miner_stats_df_hourly["speed_accepted"].iloc[max(miner_stats_df_hourly.index)]:.1f}</font> MH/s', 'green'), width = 250)
div6 = Div(text=wrap_in_paragraphs(f'24hr Rolling Hashrate:<br><font size=7>{miner_stats_df_hourly["avg_24"].iloc[max(miner_stats_df_hourly.index)]:.1f}</font> MH/s', 'darkorange'), width = 250)
div7 = Div(text=wrap_in_paragraphs(f'Current BTC:<br><font size=7>{payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]-kk["Quantity"] + qqq["Quantity"]:.7f}</font>', 'gold'))
div8 = Div(text=wrap_in_paragraphs(f'Current BTC * Current Price:<br><font size=7>{(payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]-kk["Quantity"]+qqq["Quantity"])*int(cur_BTCCAD):.2f}</font>', ))

btc_collected_sold_div = Div(text=wrap_in_paragraphs(f"""Total BTC Collected: {payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]:,.7f} / Collected BTC*CAD Price: ${payout_data["total_mined_dollars_converted_now"].iloc[max(payout_data.index)]:,.2f}
<br>Total BTC Sold: ${kk["Quantity"]:.7f} / Total Sold Amount: ${kk["Total"]:.2f}
<br>Total BTC Bought: ${qqq["Quantity"]:.7f} / Total Bought Amount: ${qqq["Total"]:.2f}""", 'firebrick', ), width=600)
btc_eth_price_div = Div(text=wrap_in_paragraphs(f"""BTC: ${int(cur_BTCUSD):,} / ${int(cur_BTCCAD):,}
<br>ETH: ${int(cur_ETHUSD):,} / ${int(cur_ETHCAD):,}
<br>Coinbase Fees: ${kk['Fees'] + qqq['Fees']}
""", 'black', ), width=200)
rolling_payout_div = Div(text=wrap_in_paragraphs(f"""5-day Daily Avg: {payout_data_daily[f'rolling_5'][-1]:,.7f} BTC / ${payout_data_daily[f'rolling_5_price'][-1]:,.2f}
<br>10-day Daily Avg: {payout_data_daily[f'rolling_10'][-1]:,.7f} BTC / ${payout_data_daily[f'rolling_10_price'][-1]:,.2f}
<br>2-week Daily Avg: {payout_data_daily[f'rolling_14'][-1]:,.7f} BTC / ${payout_data_daily[f'rolling_14_price'][-1]:,.2f}
<br>1 Month Daily Avg: {payout_data_daily[f'rolling_28'][-1]:,.7f} BTC / ${payout_data_daily[f'rolling_28_price'][-1]:,.2f}
""", ), width=400)

widgets = column([])
divs1 = row([btc_collected_sold_div, div7, blank_divs[3], div8, btc_eth_price_div])
divs2 = row([div1, blank_divs[1], div2,blank_divs[4], rolling_payout_div, div5,blank_divs[5], div6,])
charts = row([payout_chart, column([miner_stats_chart, total_mined_chart])])
tab1 = Panel(child = column([divs1, divs2, charts]), title='BTC Report')



# PAGE 2

df = pd.read_sql('select * from most_recent_rig_device_stats', sql_engine, parse_dates='timestamp')
df = df[df['timestamp'] > pd.to_datetime(datetime.datetime(2021,4,24))]
print(df.tail().to_string())

def make_data(fdf, rig_nm, resample='H'):
    if rig_nm:
        idf = fdf[fdf['rig_name'] == rig_nm.lower()].copy()
    else:
        idf = fdf.copy()
    idf = idf.groupby('timestamp').agg({'speed':np.sum, 'power_usage':np.sum,})
    idf.index = pd.to_datetime(idf.index)
    idf = idf.resample(resample).mean()
    idf.fillna(0, inplace=True)
    for x in [5, 10, 14, 28]:
        idf[f'rolling_{x}'] = idf['speed'].rolling(x).mean()
    for i in idf.itertuples():
        if i.speed > 5*i.rolling_10:
            idf.at[i.Index, 'speed'] = i.speed/1000
    idf['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in idf.index]
    return idf

source_amd = ColumnDataSource(make_data(df, 'AMDBuster'))
amd_speed_chart = figure(plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'AMDBuster MH/s')
amd_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
amd_speed_chart.y_range.start = 0

amd_line = amd_speed_chart.line(x="timestamp", y='speed', source=source_amd,  alpha = 0.3, color = 'firebrick', line_width = 3)
amd_circle = amd_speed_chart.circle(x="timestamp", y='speed', source=source_amd, size = 3, color = 'firebrick')

amd_speed_chart.add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Speed MH/S", "@speed{(0.0)}"),], mode='vline', ))

source_leader = ColumnDataSource(make_data(df, 'Leader'))
leader_speed_chart = figure(x_range=amd_speed_chart.x_range,plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'Leader MH/s')
leader_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
leader_speed_chart.y_range.start = 0

leader_line = leader_speed_chart.line(x="timestamp", y='speed', source=source_leader,  alpha = 0.3, color = 'navy', line_width = 3)
leader_circle = leader_speed_chart.circle(x="timestamp", y='speed', source=source_leader, size = 3, color = 'navy')

leader_speed_chart.add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Speed MH/S", "@speed{(0.0)}"),], mode='vline', ))

source_wh = ColumnDataSource(make_data(df, 'Workhorse1080'))
wh_speed_chart = figure(x_range=amd_speed_chart.x_range,plot_width=800, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= 'Workhorse1080 MH/s')
wh_speed_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
wh_speed_chart.y_range.start = 0

wh_line = wh_speed_chart.line(x="timestamp", y='speed', source=source_wh,  alpha = 0.3, color = 'green',  line_width = 3)
wh_circle = wh_speed_chart.circle(x="timestamp", y='speed', source=source_wh, size = 3, color = 'green')

wh_speed_chart.add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Speed MH/S", "@speed{(0.0)}"),], mode='vline', ))


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
total_hours_data = zz.groupby(['time_period']).sum()
for x in [total_hours_data, zz]:
    x['on_pct'] = np.round(100*x["on"]/x['length'],1)
    x['ops_pct'] = np.round(100*x["operational"]/x['length'],1)
    x.sort_values('length', inplace=True)
total_hours_data['y_pos_on'] = [(x,-0.15) for x in total_hours_data.index]
total_hours_data['y_pos_ops'] = [(x,0.15) for x in total_hours_data.index]

scce = ColumnDataSource(total_hours_data)
plott = figure(plot_width=300, plot_height=300, toolbar_location=None, title="Total Operational %", x_range = [80,100], y_range = [i for i in total_hours_data.index])
plott.hbar(right='on_pct', y='y_pos_on', height=0.3, source=scce, color='navy')
plott.hbar(right='ops_pct', y='y_pos_ops', height=0.3, source=scce, color = 'green')
plott.ygrid.grid_line_color = None
plott.add_tools(HoverTool(tooltips=[("Timeframe", "@time_period"), ("ON PCT", "@on_pct{(0.0)}"), ("Operational PCT", "@ops_pct{(0.0)}")], mode='hline', ))

bar_charts = {i:{} for i in sorted(zz.rig.unique())}
for i in bar_charts.keys():
    inner_df = zz[zz['rig'] == i].copy()
    inner_df.set_index("time_period", inplace=True)
    inner_df['y_pos_on'] = [(x, -0.15) for x in inner_df.index]
    inner_df['y_pos_ops'] = [(x, 0.15) for x in inner_df.index]
    srce = ColumnDataSource(inner_df)
    bar_charts[i] = figure(plot_width=300, plot_height=300, toolbar_location=None, title=f"{i} Operational %", x_range=[80, 100], y_range=[i for i in inner_df.index])
    bar_charts[i].hbar(right='on_pct', y='y_pos_on', height=0.3, source=srce, legend_label='ON', color='navy', alpha=0.85)
    bar_charts[i].hbar(right='ops_pct', y='y_pos_ops', height=0.3, source=srce, color='green', legend_label='OPS', alpha=0.85)
    bar_charts[i].ygrid.grid_line_color = None
    bar_charts[i].legend.click_policy = 'hide'
    bar_charts[i].legend.location = 'top_right'
    bar_charts[i].add_tools(HoverTool(tooltips=[("Timeframe", "@time_period"), ("ON PCT", "@on_pct{(0.0)}"), ("Operational PCT", "@ops_pct{(0.0)}")], mode='hline', ))


source_power = ColumnDataSource(make_data(df, None, 'H'))
power_chart = figure(x_range=amd_speed_chart.x_range,plot_width=600, plot_height=300,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="W", toolbar_location="right", title= 'Total Power used by GPUs')
power_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0")
power_chart.y_range.start = 0

power_line = power_chart.line(x="timestamp", y='power_usage', source=source_power,  alpha = 0.3, color = 'green',  line_width = 3)
power_circle = power_chart.circle(x="timestamp", y='power_usage', source=source_power, size = 3, color = 'green')

power_chart.add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Power W", "@power_usage{(0.0)}"),], mode='vline', ))


for p in [amd_speed_chart, leader_speed_chart, wh_speed_chart, plott, power_chart]:
    p.xaxis.major_label_orientation = np.pi / 4
# pretty up the dashboard
for p in [amd_speed_chart, leader_speed_chart, wh_speed_chart, plott, power_chart] + [i for i in bar_charts.values()]:
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
    p.yaxis.axis_label_text_font_style = "bold"
    p.xaxis.axis_label_text_font_style = "bold"
    p.toolbar.active_scroll = "auto"

tab2 = Panel(child = row([column([amd_speed_chart, leader_speed_chart, wh_speed_chart]), column([i for i in bar_charts.values()]), column([power_chart, plott])]), title = 'Miner Stability')

dashboard = Tabs(tabs=[tab1, tab2])
curdoc().add_root(dashboard)
show(dashboard)
