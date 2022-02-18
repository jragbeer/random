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
    return f"""<p><b><font color={colour} size={size}>{text}</font></b></p>"""
def make_data(fdf, rig_nm=None, resample='H', col = 'speed'):
    if rig_nm:
        idf = fdf[fdf['rig_name'] == rig_nm.lower()].copy()
    else:
        idf = fdf.copy()
    idf = idf.groupby('timestamp').agg({'speed':np.sum, 'power_usage':np.sum,})
    idf.index = pd.to_datetime(idf.index)
    idf = idf.resample(resample).mean()
    idf.fillna(0, inplace=True)
    for x in [5, 10, 14, 28]:
        idf[f'rolling_{x}'] = idf[col].rolling(x).mean()
    for i in idf.itertuples():
        if i.speed > 5*i.rolling_10:
            idf.at[i.Index, 'speed'] = i.speed/1000
    idf['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in idf.index]
    return idf
def make_btc_profit_source(payout_data_, cb_buy, cb_sell):
    other = payout_data_.set_index('timestamp').resample('H').mean().reset_index()
    other['timestamp'] = other['timestamp'].dt.tz_localize('EST', ambiguous='infer')
    new_cb_buy_data = cb_buy.set_index('Timestamp').resample('H').sum().reset_index()
    new_cb_buy_data.columns = [i.lower() for i in new_cb_buy_data.columns]
    fun = pd.merge(other, new_cb_buy_data[['quantity', 'timestamp', 'total']], on='timestamp', how='left')
    fun['timestamp'] = pd.to_datetime(fun['timestamp'])

    new_cb_sell_data = cb_sell.set_index('Timestamp').resample('H').sum().reset_index()
    new_cb_sell_data.columns = [i.lower()+'_s' for i in new_cb_sell_data.columns]
    new_cb_sell_data.rename(columns={'timestamp_s':'timestamp'}, inplace=True)
    fun = pd.merge(fun, new_cb_sell_data[['quantity_s', 'timestamp', 'total_s']], on='timestamp', how='left')

    fun['net_amount'] = fun['net_amount'].fillna(0)
    fun['new_net_amount_cumsum'] = fun['net_amount'].cumsum()
    fun['quantity'] = fun['quantity'].fillna(0)
    fun['quantity_cumsum'] = fun['quantity'].cumsum()
    fun['quantity_s'] = fun['quantity_s'].fillna(0)
    fun['quantity_s_cumsum'] = fun['quantity_s'].cumsum()
    fun['total'] = fun['total'].fillna(0)
    fun['total_cumsum'] = fun['total'].cumsum()
    fun['total_s'] = fun['total_s'].fillna(0)
    fun['total_s_cumsum'] = fun['total_s'].cumsum()
    fun['total_bought_sold_money'] = fun['total_s_cumsum'] - fun['total_cumsum']

    fun['total_bought_sold_btc'] = fun['quantity_cumsum'] - fun['quantity_s_cumsum']

    fun['total_mined_dollars_converted_now'] = fun['new_net_amount_cumsum'] * cur_BTCCAD
    fun['buy_dollars_cumsum'] = fun['quantity_cumsum'] * cur_BTCCAD
    fun['sell_dollars_cumsum'] = fun['quantity_s_cumsum'] * cur_BTCCAD


    fun['total_btc_now'] = fun['new_net_amount_cumsum'] + fun['total_bought_sold_btc']
    fun['current_btc_in_money'] = fun['total_btc_now'] * cur_BTCCAD

    fun['final'] = fun['current_btc_in_money'] + fun['total_bought_sold_money']
    fun = fun.drop(columns=['created', 'gross_amount', 'nh_fee', 'avg_6'])
    fun['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in fun['timestamp']]

    return ColumnDataSource(fun)
def update_payout_select(attr, old, new):
    if new == '4H':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2()).data)
    elif new == 'Daily':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Daily')).data)
    elif new == 'Weekly':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Weekly')).data)
    elif new == 'Bi-Weekly':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Bi-Weekly')).data)
    elif new == 'Monthly':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Monthly')).data)
    elif new == 'Quarterly':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Quarterly')).data)
    elif new == 'Year':
        source.data = dict(ColumnDataSource(data=get_payout_data_df2('Year')).data)

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'NiceHash Mining'

pd.set_option('display.float_format', lambda x: '%.10f' % x)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

today = datetime.datetime.now()

rig_colours = {"Leader":'orange', "AMDBuster":"firebrick", "Workhorse1080":'forestgreen', "Earlybird":'black', 'Oddballs':'gold'}

df = pd.read_sql('select * from most_recent_rig_device_stats', new_sql_engine, parse_dates='timestamp')
df = df[df['timestamp'] > pd.to_datetime(datetime.datetime(2021,4,24))]
df['rig_name'] = df['rig_name'].str.lower()

mining_costs = pd.read_csv(data_path + "mining_costs.csv")

cur_BTCCAD = yf.Ticker("BTC-CAD").history(period="5d")['Close'][-1]
cur_ETHCAD = yf.Ticker("ETH-CAD").history(period="5d")['Close'][-1]
cur_BTCUSD = yf.Ticker("BTC-USD").history(period="5d")['Close'][-1]
cur_ETHUSD = yf.Ticker("ETH-USD").history(period="5d")['Close'][-1]

coinbase_data = clean_coinbase_data()
coinbase_sell_data = coinbase_data[(coinbase_data['Transaction'] == 'Sell') & (coinbase_data['Asset'] == 'BTC')]
coinbase_buy_data = coinbase_data[(coinbase_data['Transaction'] == 'Buy') & (coinbase_data['Asset'] == 'BTC')]

coinbase_sell_data_eth = coinbase_data[(coinbase_data['Transaction'] == 'Sell') & (coinbase_data['Asset'] == 'ETH')]
coinbase_buy_data_eth = coinbase_data[(coinbase_data['Transaction'] == 'Buy') & (coinbase_data['Asset'] == 'ETH')]

coinbase_sell_data_sum = coinbase_sell_data.sum()[['Quantity','Subtotal', 'Total', "Fees"]]
coinbase_buy_data_sum = coinbase_buy_data.sum()[['Quantity','Subtotal', 'Total', "Fees"]]

coinbase_sell_data_eth_sum = coinbase_sell_data_eth.sum()[['Quantity','Subtotal', 'Total', "Fees"]]
coinbase_buy_data_eth_sum = coinbase_buy_data_eth.sum()[['Quantity','Subtotal', 'Total', "Fees"]]

# payout data
payout_data = get_payout_data_df2()
payout_data['total_mined_dollars_converted_now'] = payout_data['net_amount_cumsum'] * cur_BTCCAD


payout_data_daily = payout_data.set_index("timestamp").resample('D').sum()[['gross_amount', 'net_amount']]
for x in [5,10, 14, 28]:
    payout_data_daily[f'rolling_{x}'] = payout_data_daily['net_amount'].rolling(x).mean()
    payout_data_daily[f'rolling_{x}_price'] = payout_data_daily[f'rolling_{x}']*cur_BTCCAD #55000 USD

# miner statistics data
miner_stats_df = get_miner_stats_df2()
miner_stats_df_hourly = miner_stats_df.set_index('time_datetime').resample('H').mean().reset_index()
miner_stats_df_hourly['speed_accepted'] = miner_stats_df_hourly['speed_accepted'].fillna(0)
miner_stats_df_hourly['avg_24'] = miner_stats_df_hourly['speed_accepted'].rolling(24).mean()
miner_stats_df_hourly['tooltip'] = [t.strftime("%Y-%m-%d-%H") for t in miner_stats_df_hourly['time_datetime']]

payout_chart = figure(plot_width=1200, plot_height=600,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
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
miner_stats_chart.y_range.end = 550
miner_stats_chart.x_range.start = today - datetime.timedelta(days = 30)

source2 = ColumnDataSource(data=miner_stats_df_hourly)
speed_accepted = miner_stats_chart.line(x="time_datetime", y='speed_accepted', source=source2, line_width=4, line_dash='dotted', alpha = 0.37 , color = 'green', legend_label= 'Hashrate')
miner_stats_chart.circle(x="time_datetime", y='speed_accepted', source=source2, size = 4, color = 'green')
avg_24 = miner_stats_chart.line(x="time_datetime", y='avg_24', source=source2, line_width=3, color = 'darkorange', legend_label= '24-hr Rolling Avg')
miner_stats_chart.legend.location = 'bottom_left'
miner_stats_chart.legend.click_policy = 'hide'
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("24-hr Rolling", "@avg_24{(0,0.0)}"),], mode='vline', renderers=[avg_24]))
miner_stats_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Hashrate", "@speed_accepted{(0,0.0)}"),], mode='vline', renderers=[speed_accepted]))

power_data = make_data(df, None, 'H', 'power_usage')
source_power = ColumnDataSource(power_data)
power_chart = figure(x_range=miner_stats_chart.x_range, plot_width=650, plot_height=325,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label=None, y_axis_label="W", toolbar_location="right", title= 'Total Power used by GPUs')
power_chart.y_range.start = 0

power_line = power_chart.line(x="timestamp", y='power_usage', source=source_power,  alpha = 0.3, color = 'goldenrod',  line_width = 3)
power_circle = power_chart.circle(x="timestamp", y='power_usage', source=source_power, size = 3, color = 'goldenrod')

power_chart.add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Power W", "@power_usage{(0.0)}"),], mode='vline', ))

fun_source = make_btc_profit_source(payout_data, coinbase_buy_data, coinbase_sell_data)

total_mined_chart = figure(plot_width=800, plot_height=525,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()], x_axis_label=None, y_axis_label="BTC", toolbar_location="right", title= 'BTC Holdings')
total_mined_chart.yaxis[0].formatter = NumeralTickFormatter(format="0.0000")
total_mined_chart.y_range.start = 0

# mined per month bars
monthly_payout = payout_data.copy().set_index('timestamp').resample("1M").sum().reset_index()
mnth_src = ColumnDataSource(monthly_payout)
monthly_bars = total_mined_chart.vbar(x="timestamp", top='net_amount', bottom=0, source=mnth_src, line_width=4,  alpha = 0.7, color = 'forestgreen', legend_label='Mined by Month')

net_cumsum_line3 = total_mined_chart.line(x="timestamp", y='total_btc_now', source=fun_source, line_width=4,  alpha = 0.7, color = 'black', legend_label='Total BTC Now')
net_cumsum_circle3 = total_mined_chart.circle(x="timestamp", y='total_btc_now', source=fun_source, size = 3, color = 'black', legend_label='Total BTC Now')

net_cumsum_line = total_mined_chart.line(x="timestamp", y='new_net_amount_cumsum', source=fun_source, line_width=4, line_dash='dotted', alpha = 0.3, color = 'firebrick', legend_label='BTC Ever Mined')
total_mined_chart.circle(x="timestamp", y='new_net_amount_cumsum', source=fun_source, size = 3, color = 'firebrick', legend_label='BTC Ever Mined')

net_cumsum_line2 = total_mined_chart.line(x="timestamp", y='quantity_cumsum', source=fun_source, line_width=4,  alpha = 0.7, color = 'blue', legend_label='BTC Purchases')
net_cumsum_circle2 = total_mined_chart.circle(x="timestamp", y='quantity_cumsum', source=fun_source,  size = 3, color = 'blue', legend_label='BTC Purchases')
net_cumsum_circle2.visible = False
net_cumsum_line2.visible = False

net_cumsum_line4 = total_mined_chart.line(x="timestamp", y='quantity_s_cumsum', source=fun_source, line_width=4,  alpha = 0.7, color = 'gold', legend_label='BTC Sales')
net_cumsum_circle4 = total_mined_chart.circle(x="timestamp", y='quantity_s_cumsum', source=fun_source,  size = 3, color = 'gold', legend_label='BTC Sales')
net_cumsum_circle4.visible = False
net_cumsum_line4.visible = False

total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("BTC", "@quantity_s_cumsum{(0,0.00000)}"),], mode='vline', renderers=[net_cumsum_line4]))
total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("BTC", "@quantity_cumsum{(0,0.00000)}"),], mode='vline', renderers=[net_cumsum_line2]))
total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("BTC", "@total_btc_now{(0,0.00000)}"),], mode='vline', renderers=[net_cumsum_line3]))
total_mined_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("BTC", "@new_net_amount_cumsum{(0,0.00000)}"),], mode='vline', renderers=[net_cumsum_line]))
total_mined_chart.legend.location = 'top_left'
total_mined_chart.legend.click_policy = 'hide'


total_rev_chart = figure(plot_width=800, plot_height=525,x_axis_type='datetime',
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()], x_axis_label=None, y_axis_label="$", toolbar_location="right", title= '$ in Crypto')
total_rev_chart.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
total_rev_chart.y_range.start = 0

rev_line3 = total_rev_chart.line(x="timestamp", y='total_mined_dollars_converted_now', source=fun_source, line_width=4,  alpha = 0.7, color = 'black', legend_label='Total Mined Rev')
rev_circle3 = total_rev_chart.circle(x="timestamp", y='total_mined_dollars_converted_now', source=fun_source, size = 3, color = 'black', legend_label='Total Mined Rev')

rev_line0 = total_rev_chart.line(x="timestamp", y='final', source=fun_source, line_width=4,  alpha = 0.7, color = 'firebrick', legend_label='$ in BTC')
rev_circle0 = total_rev_chart.circle(x="timestamp", y='final', source=fun_source, size = 3, color = 'firebrick', legend_label='$ in BTC')

rev_line1 = total_rev_chart.line(x="timestamp", y='buy_dollars_cumsum', source=fun_source, line_width=4,  alpha = 0.7, color = 'blue', legend_label='Total Buy Amt')
rev_circle1 = total_rev_chart.circle(x="timestamp", y='buy_dollars_cumsum', source=fun_source, size = 3, color = 'blue', legend_label='Total Buy Amt')
rev_line1.visible = False
rev_circle1.visible = False

rev_line2 = total_rev_chart.line(x="timestamp", y='sell_dollars_cumsum', source=fun_source, line_width=4,  alpha = 0.7, color = 'gold', legend_label='Total Sell Amt')
rev_circle2 = total_rev_chart.circle(x="timestamp", y='sell_dollars_cumsum', source=fun_source, size = 3, color = 'gold', legend_label='Total Sell Amt')
rev_circle2.visible = False
rev_line2.visible = False

total_rev_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("$", "@total_mined_dollars_converted_now{(0,0.00)}"),], mode='vline', renderers=[rev_line3]))
total_rev_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("$", "@sell_dollars_cumsum{(0,0.00)}"),], mode='vline', renderers=[rev_line2]))
total_rev_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("$", "@buy_dollars_cumsum{(0,0.00)}"),], mode='vline', renderers=[rev_line1]))
total_rev_chart.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("$", "@final{(0,0.00)}"),], mode='vline', renderers=[rev_line0]))

total_rev_chart.legend.location = 'top_left'
total_rev_chart.legend.click_policy = 'hide'

# pretty up the dashboard
for p in [payout_chart, total_mined_chart, miner_stats_chart, total_rev_chart]:
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
div7 = Div(text=wrap_in_paragraphs(f'Current BTC:<br><font size=7>{payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]-coinbase_sell_data_sum["Quantity"] + coinbase_buy_data_sum["Quantity"]:.7f}</font>', 'gold'))
div8 = Div(text=wrap_in_paragraphs(f'Current BTC * Current Price:<br><font size=7>{(payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]-coinbase_sell_data_sum["Quantity"]+coinbase_buy_data_sum["Quantity"])*int(cur_BTCCAD):.2f}</font>', ))

btc_collected_sold_div = Div(text=wrap_in_paragraphs(f"""Total BTC Collected: {payout_data["net_amount_cumsum"].iloc[max(payout_data.index)]:,.7f} / Collected BTC*CAD Price: ${payout_data["total_mined_dollars_converted_now"].iloc[max(payout_data.index)]:,.2f}
<br>Cost of Parts: {mining_costs[mining_costs["Item_type"] != "Electricity"]["Cost"].sum():,.0f} /
Electricity: ${mining_costs[mining_costs["Item_type"] == "Electricity"]["Cost"].sum():,.0f} / Total : ${mining_costs["Cost"].sum():,.0f}
<br>Hold Mining 
ROI: ${payout_data["total_mined_dollars_converted_now"].iloc[max(payout_data.index)]-mining_costs["Cost"].sum():,.2f} ({100*payout_data["total_mined_dollars_converted_now"].iloc[max(payout_data.index)]/mining_costs["Cost"].sum():.0f}%)
<br><font color=black>
<br>Total BTC Sold: {coinbase_sell_data_sum["Quantity"]:.7f} / Total Sold Amount: ${coinbase_sell_data_sum["Total"]:,.2f} 
<br>(avg: {coinbase_sell_data_sum["Total"]/coinbase_sell_data_sum["Quantity"]:,.2f})
<br>Total BTC Bought: {coinbase_buy_data_sum["Quantity"]:.7f} / Total Bought Amount: ${coinbase_buy_data_sum["Total"]:,.2f} 
<br>(avg: {coinbase_buy_data_sum["Total"]/coinbase_buy_data_sum["Quantity"]:,.2f})
<br>Bought-Sold Diff: {coinbase_buy_data_sum["Quantity"]-coinbase_sell_data_sum["Quantity"]:.7f} / Bought-Sold Diff Amount: ${coinbase_buy_data_sum["Total"]-coinbase_sell_data_sum["Total"]:,.2f}</font>""", 'firebrick', ), width=600)

btc_eth_price_div = Div(text=wrap_in_paragraphs(f"""BTC: ${int(cur_BTCUSD):,} / ${int(cur_BTCCAD):,}
<br>ETH: ${int(cur_ETHUSD):,} / ${int(cur_ETHCAD):,}
<br>Coinbase Fees: ${coinbase_sell_data_sum['Fees'] + coinbase_buy_data_sum['Fees']:,.2f}
""", 'black', ), width=200)

eth_collected_sold_div = Div(text=wrap_in_paragraphs(f"""Total ETH Sold: {coinbase_sell_data_eth_sum["Quantity"]:.7f} / Total Sold Amount: ${coinbase_sell_data_eth_sum["Total"]:.2f}
<br>Total ETH Bought: {coinbase_buy_data_eth_sum["Quantity"]:.7f} / Total Bought Amount: ${coinbase_buy_data_eth_sum["Total"]:.2f}
<br>Bought-Sold Diff: {coinbase_buy_data_eth_sum["Quantity"]-coinbase_sell_data_eth_sum["Quantity"]:.7f} / Bought-Sold Diff Amount: ${coinbase_buy_data_eth_sum["Total"]-coinbase_sell_data_eth_sum["Total"]:.2f}
<br>Current ETH wallet: ${(coinbase_buy_data_eth_sum["Quantity"]-coinbase_sell_data_eth_sum["Quantity"])*cur_ETHCAD:,.2f} / ETH Profit to date: ${((coinbase_buy_data_eth_sum["Quantity"]-coinbase_sell_data_eth_sum["Quantity"])*cur_ETHCAD)-(coinbase_buy_data_eth_sum["Total"]-coinbase_sell_data_eth_sum["Total"]):,.2f}""", 'forestgreen', ), width=600)

rolling_payout_div = Div(text=wrap_in_paragraphs(f"""5-day Daily Avg: {payout_data_daily[f'rolling_5'][-2]:,.7f} BTC / ${payout_data_daily[f'rolling_5_price'][-2]:,.2f}
<br>10-day Daily Avg: {payout_data_daily[f'rolling_10'][-2]:,.7f} BTC / ${payout_data_daily[f'rolling_10_price'][-2]:,.2f}
<br>2-week Daily Avg: {payout_data_daily[f'rolling_14'][-2]:,.7f} BTC / ${payout_data_daily[f'rolling_14_price'][-2]:,.2f}
<br>1 Month Daily Avg: {payout_data_daily[f'rolling_28'][-2]:,.7f} BTC / ${payout_data_daily[f'rolling_28_price'][-2]:,.2f}
""", ), width=400)


payout_select = Select(title='Payout Frequency', value='4H', options=['4H', 'Daily', "Weekly", "Bi-Weekly", 'Monthly', "Quarterly", "Yearly"])
payout_select.on_change('value', update_payout_select)

divs1 = row([div7, blank_divs[3], div8, btc_eth_price_div, eth_collected_sold_div])
divs2 = row([rolling_payout_div, blank_divs[1], div1,blank_divs[4], div2, div5,blank_divs[5], div6,])
divs0 = row([btc_collected_sold_div,column([divs1, divs2])])
charts = row([column([payout_select, payout_chart]), column([miner_stats_chart, power_chart])])
tab1 = Panel(child = column([divs0, charts]), title='BTC Report')

# PAGE 2

page_2_objects = {}
for num, rg in enumerate(sorted(list(rig_colours.keys()))):
    if num == 0:
        page_2_objects[rg] = {'source': ColumnDataSource(make_data(df, rg).drop_duplicates()),
                             "chart_1": figure(plot_width=700, plot_height=200,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
               x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= f'{rg} MH/s')}

    else:
        page_2_objects[rg] = {'source': ColumnDataSource(make_data(df, rg).drop_duplicates()),
                             "chart_1": figure(x_range=page_2_objects[sorted(list(rig_colours.keys()))[0]]['chart_1'].x_range, plot_width=700, plot_height=200,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
               x_axis_label=None, y_axis_label="MH/S", toolbar_location="right", title= f'{rg} MH/s')}

    page_2_objects[rg]['chart_1'].y_range.start = 0
    page_2_objects[rg]['chart_1'].y_range.end = 200
    page_2_objects[rg]['chart_1'].x_range.start = today-datetime.timedelta(days=10)
    page_2_objects[rg]['line_1'] = page_2_objects[rg]['chart_1'].line(x="timestamp", y='speed', source=page_2_objects[rg]['source'],  alpha = 0.3, color = rig_colours[rg], line_width = 3)
    page_2_objects[rg]['circle_1'] = page_2_objects[rg]['chart_1'].circle(x="timestamp", y='speed', source=page_2_objects[rg]['source'], size = 3, color = rig_colours[rg])
    page_2_objects[rg]['chart_1'].add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("Speed MH/S", "@speed{(0.0)}"), ], mode='vline', ))

    if num == 0:
        page_2_objects[rg]['chart_2'] = figure(plot_width=700, plot_height=200,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
               x_axis_label=None, y_axis_label="W", toolbar_location="right", title= f'{rg} Power Usage')
    else:
        page_2_objects[rg]["chart_2"] = figure(x_range=page_2_objects[sorted(list(rig_colours.keys()))[0]]['chart_1'].x_range, plot_width=700, plot_height=200,x_axis_type='datetime', tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
               x_axis_label=None, y_axis_label="W", toolbar_location="right", title= f'{rg} Power Usage')
    page_2_objects[rg]['chart_2'].y_range.start = 0
    page_2_objects[rg]['chart_2'].x_range.start = today-datetime.timedelta(days=10)
    page_2_objects[rg]['line_2'] = page_2_objects[rg]['chart_2'].line(x="timestamp", y='power_usage', source=page_2_objects[rg]['source'],  alpha = 0.3, color = rig_colours[rg], line_width = 3)
    page_2_objects[rg]['circle_2'] = page_2_objects[rg]['chart_2'].circle(x="timestamp", y='power_usage', source=page_2_objects[rg]['source'], size = 3, color = rig_colours[rg])
    page_2_objects[rg]['chart_2'].add_tools(HoverTool(tooltips=[("Datetime", "@tooltip"), ("W", "@power_usage{(0.0)}"), ], mode='vline', ))


bigger = {x: {} for x in list(sorted(rig_colours.keys()))}
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

bar_charts = {i:{} for i in sorted(zz.rig.unique())}
for i in bar_charts.keys():
    inner_df = zz[zz['rig'] == i].copy()
    inner_df.set_index("time_period", inplace=True)
    inner_df['y_pos_on'] = [(x, -0.15) for x in inner_df.index]
    inner_df['y_pos_ops'] = [(x, 0.15) for x in inner_df.index]
    srce = ColumnDataSource(inner_df)
    bar_charts[i] = figure(plot_width=300, plot_height=200, toolbar_location=None, title=f"{i} Operational %", x_range=[60, 100], y_range=[i for i in inner_df.index])
    bar_charts[i].hbar(right='on_pct', y='y_pos_on', height=0.3, source=srce, legend_label='ON', color='navy', alpha=0.85)
    bar_charts[i].hbar(right='ops_pct', y='y_pos_ops', height=0.3, source=srce, color='green', legend_label='OPS', alpha=0.85)
    bar_charts[i].ygrid.grid_line_color = None
    bar_charts[i].legend.click_policy = 'hide'
    bar_charts[i].legend.location = 'top_right'
    bar_charts[i].add_tools(HoverTool(tooltips=[("Timeframe", "@time_period"), ("ON PCT", "@on_pct{(0.0)}"), ("Operational PCT", "@ops_pct{(0.0)}")], mode='hline', ))

# Page 3
scce = ColumnDataSource(total_hours_data)
plott = figure(plot_width=300, plot_height=300, toolbar_location=None, title="Total Operational %", x_range = [80,100], y_range = [i for i in total_hours_data.index])
plott.hbar(right='on_pct', y='y_pos_on', height=0.3, source=scce, color='firebrick')
plott.hbar(right='ops_pct', y='y_pos_ops', height=0.3, source=scce, color = 'black')
plott.ygrid.grid_line_color = None
plott.add_tools(HoverTool(tooltips=[("Timeframe", "@time_period"), ("ON PCT", "@on_pct{(0.0)}"), ("Operational PCT", "@ops_pct{(0.0)}")], mode='hline', ))

power_div = Div(text = wrap_in_paragraphs(f"<u><i>Since April 25, 2021</i></u><br><br>Past Month of energy consumption: <br>"
                                            f"All GPUs Avg Energy: {power_data['rolling_28'][-1]:.1f} KWh <br>"
                                          f"Total PCs Avg Energy: {power_data['rolling_28'][-1] + 175*(len(rig_colours.keys())-1):.1f} KWh <br>"
                                          f"Expected Hourly cost: ${(power_data['rolling_28'][-1] + 650)/1000*.12:.2f} <br>"
                                          f"Expected Monthly cost: ${(power_data['rolling_28'][-1] + 650)/1000*.12*24*31:.2f} <br>", 'black'), width = 375)

for p in [page_2_objects[i]['chart_1'] for i in list(sorted(rig_colours.keys()))] + [page_2_objects[i]['chart_2'] for i in list(sorted(rig_colours.keys()))] + [power_chart]:
    p.xaxis.major_label_orientation = np.pi / 4
# pretty up the dashboard
for p in [page_2_objects[i]['chart_1'] for i in list(sorted(rig_colours.keys()))] + [page_2_objects[i]['chart_2'] for i in list(sorted(rig_colours.keys()))] + [plott, power_chart] + [i for i in bar_charts.values()]:
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

tab2 = Panel(child = row([column([plott, power_div]), total_mined_chart, total_rev_chart]), title = "Aggregate Miner Stats")
tab3 = Panel(child = row([column([page_2_objects[i]['chart_1'] for i in list(sorted(rig_colours.keys()))]), column([page_2_objects[i]['chart_2'] for i in list(sorted(rig_colours.keys()))]), column([i for i in bar_charts.values()]), ]), title = 'Rig Stability')

dashboard = Tabs(tabs=[tab1, tab2, tab3])
curdoc().add_root(dashboard)
show(dashboard)
