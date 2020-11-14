from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, Button, DatePicker, CustomJS, Panel, RangeSlider, Spinner
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FactorRange,BoxAnnotation, Tabs
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.layouts import widgetbox, row, column, gridplot, layout
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from sports_betting_data_eng import *

#jragbeer
#better123

# team 1 is home

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'Soccer Predictions'

def update(years, odds_, win_prob_, league_, bet_, team, dom_eur_,):
    answer1, answer2, line_source_, line_source2_, src_, gsrc_1, gsrc_2 = make_sources(data.copy(), odf.copy(), league_, team, dom_eur_, years, win_prob_, odds_, bet_ , )
    line_src.data = dict(line_source_.data)
    line_src2.data = dict(line_source2_.data)
    src.data = dict(src_.data)

    gsrc1.data = dict(gsrc_1.data)
    gsrc2.data = dict(gsrc_2.data)

    div.text = wrap_in_paragraphs(answer1)
    div2.text = wrap_in_paragraphs(answer2)
def update_league(attr, old, new):
    select_team.options = ['All'] + sorted(data[data['league'] == new]['team1'].unique().tolist())
    select_team.value = 'All'
def update_win_prob(attr, old, new):
    pass
def update_spinner(attr, old, new):
    pass
def update_odds(attr, old, new):
    pass
def update_year(attr, old, new):
    pass
def update_team(attr, old, new):
    pass
def update_dom_eur(attr, old, new):
    pass
def update_button():
    update(year_slider.value, odds_spinner.value, win_prob_slider.value, select_league.value, bet_spinner.value, select_team.value, select_dom_eur.value)
def make_yolo_sure_source(data_, bet,):
    huh = {}
    dumb = []
    for i in data_['date'].unique():
        w = data_[data_['date'] == i]
        huh[i] = w['per_bet'].sum() - (len(w)*bet)
        # dumb.append(w['won_bet'])
    pp = pd.DataFrame({'per_bet':huh.values()}, index=huh.keys())
    pp['date'] = pp.index
    pp['cumsum'] = np.cumsum([bet] + pp['per_bet'].tolist())[1:]
    pp.reset_index(drop=True, inplace=True)
    kk = []
    for t in pp.itertuples():
        try:
            if pp.at[t.Index - 1, 'cumsum'] < bet:
                kk.append(t.cumsum - bet)
            else:
                kk.append(t.cumsum)
        except:
            kk.append(t.cumsum)
    pp['sure'] = kk
    # tt = [bet]
    # for i in pp.itertuples():
    #     if i.per_bet > 0:
    #         if tt[-1] == 0:
    #             tt.append(i.odds * bet)
    #         elif tt[-1] < 0:
    #             tt.append(tt[-1] + (bet * i.odds))
    #         elif tt[-1] > 0:
    #             tt.append(tt[-1] * i.odds)
    #     else:
    #         if tt[-1] == 0:
    #             tt.append(-bet)
    #         elif tt[-1] > 0:
    #             tt.append(0)
    #         elif tt[-1] == -bet:
    #             tt.append(-2 * bet)
    #         else:
    #             tt.append(1000)
    # pp['yolo'] = tt[1:]
    print(pp.to_string())
    return ColumnDataSource({'x': pp['date'], 'y': pp['sure'], 'tooltip': [x.strftime('%Y-%m-%d') for x in pp['date']]})
def make_line_source(df_):
    # dynamic vbar widths
    low = df_['date'].min()
    high = df_['date'].max()
    if (high-low).days <= 80:
        width = [datetime.timedelta(hours=18) for i in df_.index]
    elif 80 < (high-low).days <= 365:
        width = [datetime.timedelta(days=1) for i in df_.index]
    elif 365 < (high-low).days <= 365*2:
        width = [datetime.timedelta(days=2) for i in df_.index]
    elif 365*2 < (high-low).days <= 365*3:
        width = [datetime.timedelta(days=4) for i in df_.index]
    else:
        width = [datetime.timedelta(days=5) for i in df_.index]
    return ColumnDataSource({'x': df_['date'], 'y': df_['prob_win_tie'], 'tooltip': [x.strftime('%Y-%m-%d') for x in df_['date']],
                                    'home_away':df_['team1'] + ' - ' + df_['team2'], 'winner':df_['team1'], 'away':df_['team2'],
                             'score': df_['score1'].astype(int).astype(str) + ' - ' + df_['score2'].astype(int).astype(str), 'width': width})
def make_game_source(df_):
    # df_ = df_.reset_index(drop=True)
    return ColumnDataSource({'x': np.asarray(df_.index), 'y': np.asarray(df_['odds']), 'tooltip': [x.strftime('%Y-%m-%d') for x in df_['date']],
                                    'home_away':df_['team1'] + ' - ' + df_['team2'], 'winner':df_['team1'], 'away':df_['team2'],
                             'score': df_['score1'].astype(int).astype(str) + ' - ' + df_['score2'].astype(int).astype(str), 'width': [0.8 for x in df_.index]})
def make_sources(data_, odf_, ligue_, team_, domestic_, season_, win_prob_,min_odds, bet_ , ):
    odds_bet = min_odds * bet_
    data_ = get_full_cut_df(data_, odf_, ligue_, team_, domestic_, season_, win_prob_,min_odds, bet_ )
    line_source = make_line_source(data_[data_["won_bet"]==False].copy())
    line_source2 = make_line_source(data_[data_["won_bet"]==True].copy())
    abc = make_yolo_sure_source(data_, bet_, )
    data_ = data_.reset_index(drop=True)
    game_source = make_game_source(data_[data_["won_bet"]==False].copy())
    game_source2 = make_game_source(data_[data_["won_bet"]==True].copy())
    wow = f"Total Bets: {len(data_.index)} <br> Winning Bets: {data_['won_bet'].sum()} <br> Win Rate: {100*data_['won_bet'].sum()/len(data_.index):.1f} %"
    pow = f"Money Spent On Bets: ${bet_*len(data_.index):.2f}  <br>  Money Won Off Of Bets: ${odds_bet*data_['won_bet'].sum():.2f}  <br>  Difference: ${odds_bet*data_['won_bet'].sum()-bet_*len(data_.index):.2f} <br> Return: {100*((odds_bet*data_['won_bet'].sum())-(bet_*len(data_.index)))/(bet_*len(data_.index)):.2f} %"
    return wow, pow, line_source, line_source2, abc, game_source, game_source2
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True) #prevent numpy exponential notation on print
today = datetime.datetime.now()

# read in 538 prediction data
idata = clean_df()
idata['league'] = idata['league'].map(league_mapper)
idata.dropna(subset=['league'], inplace=True)
idata = idata.sort_values(['league', 'date', 'team1',])
league = 'premier league'
idata = idata[idata['league'] == league]

data = feature_eng(idata, win_prob)
win_prob = 0.74
# odds data
odf = read_pickles_to_df(league)

button = Button(label="Update", button_type="warning", width=200)
button.on_click(update_button)

select_league = Select(title='League', value=f"Barclays Premier League", options=sorted(data['league'].unique().tolist()), width=200)
select_league = Select(title='League', value=league, options=[league], width=200)
select_league.on_change('value', update_league)

select_dom_eur = Select(title='Competition: Domestic / Europe', value=f"Domestic", options=['Domestic', "Domestic + Europe", "Europe"], width=200)
select_dom_eur.on_change('value', update_dom_eur)

select_team = Select(title='Team', value=f"All", options=['All'] + sorted(data[data['league']==league]['team1'].unique().tolist()), width=200)
select_team.on_change('value', update_team)

win_prob_slider = Slider(start=0.7, end=1, step=0.01, value=win_prob, title="Min. Win Probability", width=200)
win_prob_slider.on_change('value', update_win_prob)

odds_spinner = Spinner(low=1.01, high=1000, step=0.01, value=1.2, title="Min. Odds", width=200)
odds_spinner.on_change('value', update_odds)

bet_spinner = Spinner(title="Bet ($)", low=5, high=100000, step=5, value=5, width=200)
bet_spinner.on_change('value', update_spinner)

year_slider = RangeSlider(start=2016, end=2020, value=(2016,2020), step=1, title="Season", width=200)
year_slider.on_change('value', update_year)
yolo = 'YOLO'

divtext, div2text, line_src, line_src2, src, gsrc1, gsrc2 = make_sources(data,odf, select_league.value, select_team.value, select_dom_eur.value, year_slider.value, win_prob_slider.value, odds_spinner.value,bet_spinner.value, )

chart = figure(plot_width=800, plot_height=600, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()], x_axis_type = 'datetime',
           x_axis_label="Year", y_axis_label="Dollars ($)", toolbar_location="right", title=f"Performance")
chart.line('x', 'y', source=src,  alpha=0.75, name='lines', color='orangered',  line_width = 3.75)
chart.circle('x', 'y', source=src,  alpha=0.75, name='circles', color='orangered',  size = 3.75)

bar = figure(plot_width=800, plot_height=600, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],x_axis_type='datetime',
           x_axis_label="Year", y_axis_label="Win Percentage (%)", toolbar_location="right", title=f"Data", y_range = (0.6, 1.01))
bar.vbar('x', top='y', source=line_src, width='width', alpha=0.75, name='red_bars', line_color = 'firebrick', fill_color = 'firebrick')
bar.vbar('x', top='y', source=line_src2, width='width', alpha=0.75, name='green_bars', line_color = 'forestgreen', fill_color = 'forestgreen')

games = figure(plot_width=800, plot_height=600, tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label="Games", y_axis_label="Payout Ratio", toolbar_location="right", title=f"Payout by Game", y_range = (1, 1.7))
games.vbar('x', top='y', source=gsrc1, width='width', alpha=0.75, name='red_game_bars', line_color = 'firebrick', fill_color = 'firebrick')
games.vbar('x', top='y', source=gsrc2, width='width', alpha=0.75, name='green_game_bars', line_color = 'forestgreen', fill_color = 'forestgreen')

games.add_tools(HoverTool(mode='vline', tooltips=[("Date", "@tooltip"),("Odds", "@y{(0.00)}"),("Home-Away", "@home_away"),('Score', "@score"), ("Winner", "@winner"),], names = ['red_game_bars', 'green_game_bars']))
bar.add_tools(HoverTool(mode='vline', tooltips=[("Date", "@tooltip"),("Win/Tie Prediction", "@y{(0.00)}"),
("Home-Away", "@home_away"),('Score', "@score"), ("Winner", "@winner"),], names = ['red_bars', 'green_bars']))
chart.add_tools(HoverTool(mode='vline', tooltips=[("Date", "@tooltip"),("Balance", "@y{(0.00)}"),], names = ['lines']))

for plot in [bar, chart]:
    plot.outline_line_width = 3
    plot.outline_line_alpha = 0.3
    plot.axis.minor_tick_line_alpha = 0
    plot.axis.major_tick_in = -1
    plot.yaxis.major_label_text_font_style = 'bold'
    plot.xaxis.major_label_text_font_style = 'bold'
    plot.yaxis.major_label_text_font = "Arial"
    plot.xaxis.major_label_text_font = "Arial"
    plot.title.align = 'center'
    plot.title.text_font_size = '12pt'
    plot.xaxis.axis_line_width = 0
    plot.yaxis.axis_line_width = 0
    plot.yaxis.axis_label_text_font_style = "bold"
    plot.xaxis.axis_label_text_font_style = "bold"
    plot.toolbar.active_scroll = "auto"
    plot.toolbar.autohide = True

blank_div = Div(text = ' ')
div_separater = Div(text = '__________________________________________')
div = Div(text = wrap_in_paragraphs(divtext, size = 5), )
div2 = Div(text = wrap_in_paragraphs(div2text, size = 5))

tab1 = Panel(child=row([bar]), title="Games by Date")
tab2 = Panel(child=row([chart]), title="Balance by Date")
tab3 = Panel(child=row([games]), title="Games")
tt = Tabs(tabs=[tab1, tab2, tab3])

widgets = column([select_league, select_team, div_separater, select_dom_eur, year_slider, win_prob_slider, odds_spinner, bet_spinner, button, blank_div, div, div2], width = 300)
dashboard = row([widgets, tt])
curdoc().add_root(dashboard)
show(dashboard)
