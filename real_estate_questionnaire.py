from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker, RangeSlider
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, TextInput, CustomJS
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models import BoxAnnotation
import time
import datetime
import os
import pytz
from collections import Counter
import traceback
from scipy import stats
import numpy as np
import pandas as pd
import sqlalchemy
import pickle
from pprint import pprint

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'Real Estate Questionnaire'

# pandas settings for terminal output
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

today = datetime.datetime.now()
path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
data_path = path + 'data/'

def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags_
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""
def update_button():
    pass
    # update(select_meter.value,  select_algo.value, resample_slider.value, window_slider.value)
def update_property(attr, old, new):
    pass
def update_time(attr, old, new):
    pass
def update_purpose(attr, old, new):
    pass
def update_area(attr, old, new):
    pass
def update_time_buy(attr, old, new):
    pass
def update_area(attr, old, new):
    pass
def update_silent(attr, old, new):
    pass
def update_one_area(attr, old, new):
    pass
def update_monthly_fee(attr, old, new):
    pass
def update_down_payment(attr, old, new):
    pass
def update_how_many(attr, old, new):
    pass

width_number = 400

title_div = Div(text=wrap_in_paragraphs('Real Estate Questionnaire', 'black', size=5), width = width_number)
info_div = Div(text=wrap_in_paragraphs("""We're looking to gauge interest in buying some property to satisfy the hippies in the group that want a farm. There are a few important
questions here that need answering to see where everyone's at. Please answer honestly. The answers will be collected and displayed for all, so we can make sound investment decisions.""", 'black', size=3), width = 1000)

text_input = TextInput(value=" ", title="Name", width= width_number)
text_input.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

select_property = Select(title='What type of property are you most interested in?', value='Land', options=sorted(['Land', 'Detached', "Townhome", "Condo"]), width=width_number)
select_property.on_change('value', update_property)

select_time = Select(title='What is your ideal time horizon to own?', value='1-2 years', options=['1-2 years', '3-5 years', '5-10 years',"10+ years",], width=width_number)
select_time.on_change('value', update_time)

select_time_buy = Select(title='When do you want to buy the first property?', value='2 years', options=['Now', '6 months', '1 year',"2 years",], width=width_number)
select_time_buy.on_change('value', update_time)

select_purpose = Select(title='What is the primary purpose of owning the property?', value='Vacation Home', options=sorted(['Vacation Home', 'Long-term Rental', "Short-term Rental", "Land development"]), width=width_number)
select_purpose.on_change('value', update_purpose)

select_area = Select(title='In which area do you think we should purchase?', value='GTA', options=sorted(['Norfolk County', 'GTA', "Quebec", "Eastern BC", 'Ottawa']), width=width_number)
select_area.on_change('value', update_area)

select_silent = Select(title='Would you be active in the management of the properties? Or a silent investor?', value='Silent', options=sorted(['Silent', 'Actively helping']), width=width_number)
select_silent.on_change('value', update_silent)

select_one_area = Select(title='Would you prefer owning anywhere or have a central location?', value='Anywhere', options=sorted(['Anywhere', 'Focus on 1 area']), width=width_number)
select_one_area.on_change('value', update_one_area)

select_monthly_fee = Select(title='Are you comfortable paying a monthly fee (condo fees, electricity, property manager, etc)?', value='Yes', options=sorted(['Yes', 'Yes, for a few months/years', 'No']), width=width_number)
select_monthly_fee.on_change('value', update_monthly_fee)

select_deposit = Select(title='How much could you provide (low-ball) in 4-8 months as a down payment?', value='15K', options=[str(i) + 'K' for i in range(5, 61, 5)], width=width_number)
select_deposit.on_change('value', update_down_payment)

select_how_many = Select(title='How many people are you comfortable going in with?', value='2', options=[str(i) for i in range(2,11)], width=width_number)
select_how_many.on_change('value', update_how_many)

button = Button(label="Send Answers", button_type="primary", width=200)
button.on_click(update_button)

dashboard = column([title_div, info_div,text_input, select_time,select_time_buy, select_silent, select_property, select_purpose, select_area,select_one_area,select_deposit, select_monthly_fee,select_how_many, button])
curdoc().add_root(dashboard)
show(dashboard)
