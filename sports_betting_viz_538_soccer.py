from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, Button, DatePicker, CustomJS, TabPanel, RangeSlider, Spinner
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource,  Range1d, ColorBar, LinearColorMapper, BasicTicker, Tabs, DateRangeSlider
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.layouts import  row, column, gridplot, layout
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from sports_betting_data_eng import *
import sqlite3

#jragbeer
#better123

# team 1 is home

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'Soccer Betting'
def pay_out_text():
    return wrap_in_paragraphs("This chart displays the payout multiple for each game in the series.", 'black', 2)
def win_prob_text():
    return wrap_in_paragraphs("This chart displays the win/tie probability for each game in the series.", 'black', 2)
def dollar_return_text():
    return wrap_in_paragraphs("This chart displays the dollar return for each game in the series.", 'black', 2)
def update(years, odds_, win_prob_, league_, bet_, team, dom_eur_, pay_out_win_prob_ind):
    league_ = league_.lower()
    answer1, answer2, line_source_, line_source2_, src_, gsrc_1, gsrc_2 = make_sources(data.copy(), odf.copy(), league_, team, dom_eur_, years, win_prob_, odds_, bet_ , pay_out_win_prob_ind)
    line_src.data = dict(line_source_.data)
    line_src2.data = dict(line_source2_.data)
    src.data = dict(src_.data)
    gsrc1.data = dict(gsrc_1.data)
    gsrc2.data = dict(gsrc_2.data)
    games.y_range.start = 1
    div.text = wrap_in_paragraphs(answer1, 'dimGrey')
    div2.text = wrap_in_paragraphs(answer2, 'dimGrey')
def update_league(attr, old, new):
    if new != 'All':
        sc = sorted(data[data['league'] == league_mapper[new]]['team1'].unique().tolist())
        select_team.options = ['All'] + sc
        select_team.value = 'All'
    else:
        sc = sorted(data['team1'].unique().tolist())
        select_team.options = ['All'] + sc
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
    if select_league.value != 'All':
        update(date_range_slider.value, odds_spinner.value, win_prob_slider.value, league_mapper[select_league.value].lower(), bet_spinner.value, select_team.value, select_dom_eur.value, select_payout_win_prob.value)
    else:
        update(date_range_slider.value, odds_spinner.value, win_prob_slider.value, select_league.value, bet_spinner.value, select_team.value, select_dom_eur.value, select_payout_win_prob.value)
def create_text_1(data_):
    try:
        return f"Total Bets: <font size = 5, color='orangered'>{len(data_.index):,}</font> <br> Winning Bets: <font size = 5, color='orangered'>{int(data_['won_bet'].sum()):,}</font> <br> Win Rate: <font size = 5, color='orangered'>{100*data_['won_bet'].sum()/len(data_.index):.1f} %</font>"
    except:
        return "Bad Query: No data available. Please select new parameters."
def create_text_2(data_, bet_):
    try:
        return f"Money Spent On Bets:<br>  <font size = 5, color='orangered'>${bet_ * len(data_.index):,.2f}</font>  <br>  Money Won Off Of Bets:<br>  <font size = 5, color='orangered'>${(data_['actual_per_game_return']+bet_).sum():,.2f}</font>  <br>  Difference: <font size = 5, color='orangered'>${(data_['actual_per_game_return']+bet_).sum() - bet_ * len(data_.index):,.2f}</font> <br> Return: <font size = 5, color='orangered'>{100 * (((data_['actual_per_game_return']+bet_).sum()) - (bet_ * len(data_.index))) / (bet_ * len(data_.index)):.2f} %</font>"
    except:
        return ''
def make_balance_by_date_source(data_, bet,):
    huh = {}
    for i in data_['date'].unique():
        w = data_[data_['date'] == i]
        # print(w)
        # huh[i] = w['actual_per_game_return'].sum() - (len(w)*bet)

        huh[i] = w['actual_per_game_return'].sum()
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
    # print(pp.to_string())
    return ColumnDataSource({'x': pp['date'], 'y': pp['sure'], 'tooltip': [x.strftime('%Y-%m-%d') for x in pp['date']]})
def make_games_by_date_source(df_):
    # dynamic vbar widths
    low = df_['date'].min()
    high = df_['date'].max()
    if (high-low).days <= 80:
        width = [datetime.timedelta(hours=18/2) for i in df_.index]
    elif 80 < (high-low).days <= 365:
        width = [datetime.timedelta(days=1/2) for i in df_.index]
    elif 365 < (high-low).days <= 365*2:
        width = [datetime.timedelta(days=2/2) for i in df_.index]
    elif 365*2 < (high-low).days <= 365*3:
        width = [datetime.timedelta(days=4/2) for i in df_.index]
    else:
        width = [datetime.timedelta(days=5/2) for i in df_.index]
    df_['home_away'] = df_['team1'] + ' - ' + df_['team2']
    df_['score']= df_['score1'].astype(int).astype(str) + ' - ' + df_['score2'].astype(int).astype(str)
    qq = pd.DataFrame(df_.groupby('date').agg({'won_bet': lambda x: list(x), 'per_bet':'count',
                                               'home_away': lambda x: list(x),'score': lambda x: list(x),
                                               'prob_win_tie': lambda x: list(x),'game_winner': lambda x: list(x),}))
    new = []
    for i in qq['per_bet']:
        array = list(range(i+1))
        inner_list=[]
        for num in range(len(array)):
            try:
                inner_list.append((array[num], array[num+1]))
            except:
                pass
        new.append(inner_list)
    qq['bottom_tops'] = new
    green = []
    red = []
    for i in qq.itertuples():
        for ind, val in enumerate(i.won_bet):
            tmp = {'date': i.Index, 'bottom': i.bottom_tops[ind][0], 'top': i.bottom_tops[ind][1],'winner':i.game_winner[ind], 'odds':i.prob_win_tie[ind],'score': i.score[ind], 'home_away': i.home_away[ind]}
            if val == True:
                green.append(tmp)
            else:
                red.append(tmp)
    rr =  ColumnDataSource({'x': [x['date'] for x in red], 'bottom': [x['bottom'] for x in red],'top': [x['top'] for x in red], 'odds': [x['odds'] for x in red],
                            'tooltip': [x['date'].strftime('%Y-%m-%d') for x in red],'width': [width[0] for x in range(len(red))],'winner':[x['winner'] for x in red],
                            'home_away':[x['home_away'] for x in red], 'score': [x['score'] for x in red]})
    gg =  ColumnDataSource({'x': [x['date'] for x in green], 'bottom': [x['bottom'] for x in green],'top': [x['top'] for x in green],'odds': [x['odds'] for x in green],
                           'tooltip': [x['date'].strftime('%Y-%m-%d') for x in green],'width': [width[0] for x in range(len(green))],'winner':[x['winner'] for x in green],
                           'home_away':[x['home_away'] for x in green], 'score': [x['score'] for x in green]})
    return rr, gg
def make_game_source(df_, indicator):
    if indicator == 'Win Probability':
        ind = df_['prob_win_tie']
    elif indicator == 'Payout':
        ind = df_['odds']
    elif indicator == 'Dollar Return':
        ind = df_['actual_per_game_return']
    return ColumnDataSource({'x': np.asarray(df_.index), 'y': np.asarray(ind), 'tooltip': [x.strftime('%Y-%m-%d') for x in df_['date']],'bottom':[0 for x in df_['date']],
                                    'home_away':df_['team1'] + ' - ' + df_['team2'], 'winner':df_['team1'], 'away':df_['team2'],'winnings':np.asarray(df_['actual_per_game_return']),
                             'score': df_['score1'].astype(int).astype(str) + ' - ' + df_['score2'].astype(int).astype(str), 'width': [0.8 for x in df_.index]})
def make_sources(data_, odf_, ligue_, team_, domestic_, season_, win_prob_,min_odds, bet_ , pay_out_win_prob_ind):
    data_ = get_full_cut_df(data_, odf_, ligue_, team_, domestic_, season_, win_prob_,min_odds, bet_ )
    line_source, line_source2 = make_games_by_date_source(data_.copy())
    abc = make_balance_by_date_source(data_, bet_, )
    data_ = data_.reset_index(drop=True)
    game_source = make_game_source(data_[data_["won_bet"]==False].copy(),pay_out_win_prob_ind)
    game_source2 = make_game_source(data_[data_["won_bet"]==True].copy(),pay_out_win_prob_ind)
    text1 = create_text_1(data_,)
    text2 = create_text_2(data_, bet_)
    return text1, text2, line_source, line_source2, abc, game_source, game_source2
def get_full_cut_df(data_,odf_, ligue, team_, domestic, season, win_prob_, min_odds, bet):
    data_ = feature_eng(data_, win_prob_)
    fdf = data_[data_['prob_win_tie'] >= win_prob_].copy()
    fdf = fdf[(fdf['date'] >= convert_unix_timestamp_to_pandas_date(season[0])) & (fdf['date'] <= convert_unix_timestamp_to_pandas_date(season[1]))].copy()
    if ligue != 'all':
        list_of_all_teams = list(data[data['league'] == ligue]['team1'].unique())
    else:
        list_of_all_teams = data['team1'].unique().tolist()
    if domestic == 'Domestic':
        if ligue != 'all':
            fdf = fdf[fdf['league'] == ligue]
        else:
            fdf = fdf
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            fdf = fdf[fdf['team1'].isin(list_of_all_teams) | (fdf['team2'].isin(list_of_all_teams))]
    elif domestic == 'Domestic + Europe':
        if ligue != "all":
            fdf = fdf[(fdf['league'] == ligue) | (fdf['league'] == "champions league") | (fdf['league'] == "europa league")]
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            if ligue != "all":
                list_of_all_teams = list(data[data['league'] == ligue]['team1'].unique())
            else:
                list_of_all_teams = list(data['team1'].unique())
            fdf = fdf[(fdf['team1'].isin(list_of_all_teams)) | (fdf['team2'].isin(list_of_all_teams))]
    else:
        fdf = fdf[(fdf['league'] == "champions league") | (fdf['league'] == "europa league")]
        if team_ != 'All':
            fdf = fdf[(fdf['team1'] == team_) | (fdf['team2'] == team_)]
        else:
            fdf = fdf[fdf['team1'].isin(list_of_all_teams) | (fdf['team2'].isin(list_of_all_teams))]
    fdf.dropna(inplace=True)
    full_data = add_odds_data_to_df(fdf, odf_, bet, min_odds).sort_values('date')
    # print(full_data.to_string())
    return full_data
def per_team(df_, team = 'Manchester City', season = (2016, 2020), ):
    try:
        df_ = df_[(df_['season'] >= season[0]) & (df_['season'] <= season[1])].copy()
        df = df_[(df_['team1'] == team) | (df_['team2'] == team)].copy()
        df = df[df['date'] <= today]
        df['prob_win_tie'] = [i.prob1 if i.team1 == team else i.prob2 for i in df.itertuples()] + df['probtie']
        df['win_tie'] = [i.score1 >= i.score2 if i.team1 == team else i.score2 >= i.score1 for i in df.itertuples()]
        df['won_bet'] = [i.win_tie if i.prob_win_tie > 0.7 else np.nan for i in df.itertuples()]
        # print(df.to_string())
        df.dropna(inplace=True)
        # print(df.to_string())
        # print()
        output = {'wins':len([x for x in df['won_bet'].dropna() if x ]), 'num_bets':len([x for x in df['won_bet'].dropna()])}
        output['pct'] = output['wins'] / output['num_bets']
        return {team:output}
    except:
        print(team, season)
        print(error_handling())
        return {}
def add_odds_data_to_df(df, rdf, bet, min_odds_):
    output = pd.merge(df, rdf, left_on=['league', 'date', 'team1', 'team2'], right_on=['league', 'date', 'team1', 'team2'], how='inner')
    output = output.dropna().reset_index(drop=True)
    qq = []
    odd_list = []
    won = []
    for i in output.itertuples():
        if i.won_bet:
            won.append(True)
            if i.prob1_win_tie == i.prob_win_tie:
                qq.append((bet * float(i.avg_1X)))
                odd_list.append(float(i.avg_1X))
            else:
                qq.append((bet * float(i.avg_X2)))
                odd_list.append(float(i.avg_X2))
        else:
            qq.append(-1 * bet)
            won.append(False)
            if i.prob1_win_tie == i.prob_win_tie:
                odd_list.append(float(i.avg_1X))
            else:
                odd_list.append(float(i.avg_X2))
    data = pd.DataFrame({'per_bet': qq, 'odds': odd_list, 'won_bet': won,}, index=output.index)
    data = data[data['odds']>=min_odds_]
    data['cumsum'] = data['per_bet'].cumsum()
    kk = []
    for t in data.itertuples():
        try:
            if data.at[t.Index - 1, 'cumsum'] < 10:
                kk.append(t.cumsum - bet)
            else:
                kk.append(t.cumsum)
        except:
            kk.append(t.cumsum)
    data['sure'] = kk
    tt = [bet]
    for i in data.itertuples():
        if i.won_bet:
            if tt[-1] == 0:
                tt.append(i.odds * bet)
            elif tt[-1] < 0:
                tt.append(tt[-1] + (bet * i.odds))
            elif tt[-1] > 0:
                tt.append(tt[-1] * i.odds)
        else:
            if tt[-1] == 0:
                tt.append(-bet)
            elif tt[-1] > 0:
                tt.append(0)
            elif tt[-1] == -bet:
                tt.append(-2 * bet)
            else:
                tt.append(1000)
    data['yolo'] = tt[1:]
    data = data.drop(columns=['won_bet'])
    final = data.merge(output, left_index=True, right_index=True)
    # np.where --- if (first arg) then (second arg) else (third arg)
    final['actual_per_game_return'] = np.where(final['per_bet'] < 0, final['per_bet'], final['per_bet'] - bet)
    final['cumsum'] = final['actual_per_game_return'].cumsum()
    final = final.drop(columns=['xg1', "xg2", "nsxg1", "nsxg2", "adj_score1", "adj_score2",])
    return final
def update_payout_win_prob(attr, old, new):
    if select_league.value != 'All':
        data_ = get_full_cut_df(data.copy(), odf.copy(), league_mapper[select_league.value].lower(), select_team.value, select_dom_eur.value, date_range_slider.value, win_prob_slider.value,odds_spinner.value, bet_spinner.value )
    else:
        data_ = get_full_cut_df(data.copy(), odf.copy(), select_league.value.lower(), select_team.value, select_dom_eur.value, date_range_slider.value, win_prob_slider.value,
                                odds_spinner.value, bet_spinner.value)
    data_ = data_.reset_index(drop=True)
    game_source = make_game_source(data_[data_["won_bet"]==False].copy(), new)
    game_source2 = make_game_source(data_[data_["won_bet"]==True].copy(), new)
    gsrc1.data = dict(game_source.data)
    gsrc2.data = dict(game_source2.data)
    if new == "Payout":
        games.y_range.start = 1
        games.title.text = "Payout Multiple by Game"
        games_explanation_div.text = pay_out_text()
        games.yaxis.axis_label = "Payout Multiple"
    elif new == 'Win Probability':
        games.y_range.start = 0.6
        games.y_range.end = 1
        games.title.text = "Win Probability by Game"
        games_explanation_div.text = win_prob_text()
        games.yaxis.axis_label = "Win Probability"
    elif new == 'Dollar Return':
        games.y_range.start = -bet_spinner.value
        games.y_range.end = bet_spinner.value
        games.title.text = "Dollar Return by Game"
        games.yaxis.axis_label = "Return ($)"
        games_explanation_div.text = dollar_return_text()

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True) #prevent numpy exponential notation on print
today = datetime.datetime.now()


local_engine = sqlite3.connect(data_path + "soccer_betting/sports_betting.db")

# read in 538 prediction data
idata = get_clean_538_prediction_data()
idata.dropna(subset=['league'], inplace=True)
idata = idata.sort_values(['league', 'date', 'team1',])

win_prob = 0.74
data = feature_eng(idata, win_prob)



# odds data
odf = pd.concat([pd.read_sql('select * from historical_odds', local_engine, parse_dates=['date']),pd.read_sql('select * from current_season_odds', local_engine, parse_dates=['date'])])
odf.replace("-", np.nan, inplace=True)
odf.dropna(inplace=True)


button = Button(label="Update", button_type="warning", width=200)
button.on_click(update_button)

# select_league = Select(title='League', value=f"Barclays Premier League", options=sorted(data['league'].unique().tolist()), width=200)
select_league = Select(title='League', value="Barclays Premier League", options=['All'] + list(league_mapper.keys()), width=200)
select_league.on_change('value', update_league)

select_dom_eur = Select(title='Competition: Domestic / Europe', value=f"Domestic", options=['Domestic', "Domestic + Europe", "Europe"], width=200)
select_dom_eur.on_change('value', update_dom_eur)

select_team = Select(title='Team', value=f"All", options=['All'] + sorted(data[data['league']==league_mapper[select_league.value].lower()]['team1'].unique().tolist()), width=200)
select_team.on_change('value', update_team)

select_payout_win_prob = Select(title='Team', value=f"Payout", options=['Payout',"Win Probability", "Dollar Return" ] , width=200)
select_payout_win_prob.on_change('value', update_payout_win_prob)

win_prob_slider = Slider(start=0.7, end=1, step=0.01, value=win_prob, title="Min. Win/Tie Probability", width=200)
win_prob_slider.on_change('value', update_win_prob)

odds_spinner = Spinner(low=1.01, high=1000, step=0.01, value=1.2, title="Min. Odds", width=200)
odds_spinner.on_change('value', update_odds)

bet_spinner = Spinner(title="Bet ($)", low=5, high=100000, step=5, value=5, width=200)
bet_spinner.on_change('value', update_spinner)

date_range_slider = DateRangeSlider(value=(odf['date'].max().date() - datetime.timedelta(days=365), odf['date'].max().date()),
                                    start=odf['date'].min().date(), end=odf['date'].max().date())
date_range_slider.on_change('value', update_year)
yolo = 'YOLO'

divtext, div2text, line_src, line_src2, src, gsrc1, gsrc2 = make_sources(data,odf, league_mapper[select_league.value].lower(), select_team.value, select_dom_eur.value, date_range_slider.value, win_prob_slider.value, odds_spinner.value,bet_spinner.value, select_payout_win_prob.value )

chart = figure(width=900, height=750, tools=BOKEH_TOOLS, x_axis_type = 'datetime',
           x_axis_label="Datetime", y_axis_label="Dollars ($)", toolbar_location="right", title=f"Performance")
chart.line('x', 'y', source=src,  alpha=0.75, name='lines', color='orangered',  line_width = 5)
chart.circle('x', 'y', source=src,  alpha=0.75, name='circles', color='orangered',  size = 6)

zero_line = Span(location=0, dimension='width', line_color='black', line_width=2, line_alpha=0.78)
chart.add_layout(zero_line)

bar = figure(width=900, height=750, tools=BOKEH_TOOLS, x_axis_type='datetime',
           x_axis_label="Datetime", y_axis_label="Number of Games", toolbar_location="right", title=f"Games by Date", )
bar.vbar('x', top='top', bottom = 'bottom',source=line_src, width='width', alpha=0.75, name='red_bars', line_color = 'firebrick', fill_color = 'firebrick')
bar.vbar('x', top='top', bottom = 'bottom',source=line_src2, width='width', alpha=0.75, name='green_bars', line_color = 'forestgreen', fill_color = 'forestgreen')

games = figure(width=900, height=750, tools=BOKEH_TOOLS,
           x_axis_label="Games", y_axis_label="Payout Multiple", toolbar_location="right", title=f"Payout Multiple by Game", )
games.vbar('x', top='y', bottom = 'bottom', source=gsrc1, width='width', alpha=0.75, name='red_game_bars', line_color = 'firebrick', fill_color = 'firebrick')
games.vbar('x', top='y', bottom = 'bottom', source=gsrc2, width='width', alpha=0.75, name='green_game_bars', line_color = 'forestgreen', fill_color = 'forestgreen')
# games.y_range.start = 1

# hover tools
games.add_tools(HoverTool( mode='vline', tooltips=[("Date", "@tooltip"),("Odds", "@y{(0.00)}"),("Home-Away", "@home_away"),('Score', "@score"), ("Winner", "@winner"),("Return", "@winnings{$(0.00)}"),],
                           # name = ['red_game_bars', 'green_game_bars'],
                           ))
bar.add_tools(HoverTool(tooltips=[("Date", "@tooltip"),("Win/Tie Prediction", "@odds"),
("Home-Away", "@home_away"),('Score', "@score"), ("Winner", "@winner"),],
                        # name = ['red_bars', 'green_bars'],
                        ))
chart.add_tools(HoverTool(mode='vline',tooltips=[("Date", "@tooltip"),("Balance", "@y{(0.00)}"),],
                          # name = ['lines'],
                          ))

for plot in [bar, chart, games]:
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
    plot.xaxis.major_label_text_font_size = "10pt"
    plot.yaxis.major_label_text_font_size = "10pt"

blank_div = Div(text = ' ')
div_separater = Div(text = '__________________________________________')
div_separater2 = Div(text = '__________________________________________')
div = Div(text = wrap_in_paragraphs(divtext,'dimGrey', 3))
div2 = Div(text = wrap_in_paragraphs(div2text, 'dimGrey', 3))
games_explanation_div = Div(text =pay_out_text(), width = 500)

tab3 = TabPanel(child=row([bar]), title="Games by Date")
tab2 = TabPanel(child=row([chart]), title="Balance by Date")
tab1 = TabPanel(child=column([row(select_payout_win_prob, games_explanation_div), games]), title="Games")
tt = Tabs(tabs=[tab1, tab2, tab3])

widgets = column([select_league, select_team, div_separater, select_dom_eur, date_range_slider, win_prob_slider, odds_spinner, bet_spinner, button, div_separater2, div, div2], width = 300)
dashboard = row([widgets, tt])
curdoc().add_root(dashboard)
show(dashboard)
