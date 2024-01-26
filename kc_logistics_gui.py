from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker, RangeSlider
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, TextInput, CustomJS, Tabs, TabPanel
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout
from dateutil import parser
import time
import datetime
import os
import ast
import numpy as np
import pandas as pd
from pprint import pprint

# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'KC Logistics Data Input'

# pandas settings for terminal output
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

today = datetime.datetime.now()
path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
data_path = path + 'data/'

us_states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

can_province_names = {
  'AB': 'Alberta',
  'BC': 'British Columbia',
  'MB': 'Manitoba',
  'NB': 'New Brunswick',
  'NL': 'Newfoundland and Labrador',
  'NS': 'Nova Scotia',
  'NT': 'Northwest Territories',
  'NU': 'Nunavut',
  'ON': 'Ontario',
  'PE': 'Prince Edward Island',
  'QC': 'Quebec',
  'SK': 'Saskatchewan',
  'YT': 'Yukon'
}

database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv', dtype={"delivery_street_number":str,
                                                                                "pickup_street_number":str}).replace(np.nan, '')
print(database.to_string())
def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags_
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""

def update_kc_id(attkc_idr, old, new):
    pass
def update_edit():
    pass

def update_search():
    new_kc_id = edit_select_kc_id.value
    data_dict_ = database[database['kc_id'] == new_kc_id].iloc[0].to_dict()
    skids_ = ast.literal_eval(data_dict_["commodity_skids"])
    empty_skids_ = {x: (0, 0, 0, 0) for x in range(1, 19)}
    skids_ = {**empty_skids_, **skids_}

    edit_display_div.text = wrap_in_paragraphs(f"""Now viewing {new_kc_id}""")

    # pickup
    edit_pickup_unit_number.value=str(data_dict_["pickup_unit_number"])
    edit_pickup_street_number.value=str(data_dict_["pickup_street_number"])
    edit_pickup_pc.value=str(data_dict_["pickup_pc"])
    edit_pickup_street_name.value=str(data_dict_["pickup_street_name"])
    edit_select_pickup_state.value=str(data_dict_["pickup_state"])
    edit_pickup_city.value=str(data_dict_["pickup_city"])
    edit_pickup_date.value = parser.parse(str(data_dict_['pickup_date'])).date()
    # delivery
    edit_delivery_unit_number.value=str(data_dict_["delivery_unit_number"])
    edit_delivery_street_number.value=str(data_dict_["delivery_street_number"])
    edit_delivery_pc.value=str(data_dict_["delivery_pc"])
    edit_delivery_street_name.value=str(data_dict_["delivery_street_name"])
    edit_select_delivery_state.value=str(data_dict_["delivery_state"])
    edit_delivery_city.value=str(data_dict_["delivery_city"])
    edit_delivery_date.value = parser.parse(str(data_dict_['delivery_date'])).date()
    # other
    edit_other_charge.value=str(data_dict_["charge"])
    edit_other_cost.value=str(data_dict_["cost"])
    edit_other_profit.value=str(data_dict_["profit"])
    edit_other_storage.value = str(data_dict_['storage'])
    edit_other_tailgate.value=str(data_dict_["tailgate"])
    edit_other_special_notes.value=str(data_dict_["special_notes"])
    edit_other_carrier_invoice.value=str(data_dict_["carrier_invoice_status"])
    edit_other_carrier_contact.value = str(data_dict_['carrier_contact'])
    edit_other_customer_contact.value = str(data_dict_['customer_contact'])
    edit_other_customer_invoice.value = str(data_dict_['customer_invoice_status'])
    edit_other_carrier.value = str(data_dict_['carrier'])

    # commodity
    edit_commodity_notes.value=str(data_dict_["commodity_notes"])
    edit_commodity_weight.value=str(data_dict_["commodity_weight"])
    edit_commodity_commodity.value=str(data_dict_["commodity"])
    for y in range(1,19):
        skids_dict[f"edit_commodity_skid_number{y}"].value=str(skids_[y][0])
        skids_dict[f"edit_commodity_skid_length{y}"].value = str(skids_[y][1])
        skids_dict[f"edit_commodity_skid_width{y}"].value = str(skids_[y][2])
        skids_dict[f"edit_commodity_skid_height{y}"].value = str(skids_[y][3])

def update_new():
    pass
def update_create_invoice():
    pass
def update_create_bol():
    pass

def update_create_xx():
    pass

width_number = 400

title_div = Div(text=wrap_in_paragraphs('KC Logistics Data Input', 'black', size=5), width = width_number)
new_info_div = Div(text=wrap_in_paragraphs("""New Data Input for KC Logistics Data """, 'black', size=3), width = 300)

new_select_kc_id = Select(title='KC_ID', value='KC10', options=database['kc_id'].to_list(), width=int(width_number/2))
new_select_kc_id.on_change('value', update_kc_id)

new_pickup_unit_number = TextInput(value=" ", title="pickup_unit_number", width= width_number)
new_pickup_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_street_number = TextInput(value=" ", title="pickup_street_number", width= width_number)
new_pickup_street_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_pc = TextInput(value=" ", title="pickup_pc", width= width_number)
new_pickup_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_street_name = TextInput(value=" ", title="pickup_street_name", width= width_number)
new_pickup_street_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_pickup_state = Select(title='State', value='ON', options=sorted(list(can_province_names.keys()) + list(us_states.keys())), width=width_number)
new_select_pickup_state.on_change('value', update_kc_id)

new_pickup_city = TextInput(value=" ", title="pickup_city", width= width_number)
new_pickup_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_date = DatePicker(title="Pick Up Date", value = "2024-01-01", width=width_number)

new_delivery_date = DatePicker(title="Delivery Date", value = "2024-01-01", width=width_number)

new_button = Button(label="Input Info to Database", button_type="primary", width=200)
# new_button.on_click(update_new)

# EDIT / VIEW PAGE
#################################################################

edit_div_0 = Div(text = '_'*15)
edit_div_1 = Div(text = '_'*15)
edit_div_2 = Div(text = '_'*130)
edit_div_3 = Div(text = '_'*130)

start_kc_id = 'KC10'

data_dict = database[database['kc_id'] == start_kc_id].iloc[0].to_dict()

edit_info_div = Div(text=wrap_in_paragraphs("""Edit/View Data for KC Logistics Data""", 'black', size=4), width = 350)
edit_display_div = Div(text=wrap_in_paragraphs(f"""Now viewing {start_kc_id}""",), width = 350)

edit_select_kc_id = Select(title='KC_ID', value=start_kc_id, options=database['kc_id'].to_list(), width=150)
edit_select_kc_id.on_change('value', update_kc_id)

search_button = Button(label="Search Info in Database", button_type="success", width=150)
search_button.on_click(update_search)

edit_button = Button(label="Edit Info in Database", button_type="primary", width=150)
edit_button.on_click(update_edit)

create_xx_button = Button(label="Create XX", button_type="warning", width=100)
create_xx_button.on_click(update_create_xx)

create_bol_button = Button(label="Create BoL", button_type="warning", width=100)
create_bol_button.on_click(update_create_bol)

create_invoice_button = Button(label="Create Invoice", button_type="warning", width=100)
create_invoice_button.on_click(update_create_invoice)


### PICKUP
edit_div_pickup = Div(text=wrap_in_paragraphs("""Pickup""", 'black', size=3))

edit_pickup_unit_number = TextInput(value=str(data_dict["pickup_unit_number"]), title="Pickup Unit Number", width= width_number)
edit_pickup_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_street_number = TextInput(value=str(data_dict["pickup_street_number"]), title="Pickup Street Number", width= width_number)
edit_pickup_street_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_pc = TextInput(value=str(data_dict["pickup_pc"]), title="Pickup Postal Code/ZIP", width= width_number)
edit_pickup_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_street_name = TextInput(value=str(data_dict["pickup_street_name"]), title="Pickup Street Name", width= width_number)
edit_pickup_street_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_select_pickup_state = Select(title='Pickup State', value=str(data_dict["pickup_state"]), options=sorted(list(can_province_names.keys()) + list(us_states.keys())), width=width_number)
edit_select_pickup_state.on_change('value', update_kc_id)

edit_pickup_city = TextInput(value=str(data_dict["pickup_city"]), title="Pickup City", width= width_number)
edit_pickup_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_date = DatePicker(title="Pick Up Date", value = "2024-01-01", width=width_number)

# DELIVERY
######################################
edit_div_delivery = Div(text=wrap_in_paragraphs("""Delivery""", 'black', size=3))

edit_delivery_unit_number = TextInput(value=str(data_dict["delivery_unit_number"]), title="Delivery Unit Number", width= width_number)
edit_delivery_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_delivery_street_number = TextInput(value=str(data_dict["delivery_street_number"]), title="Delivery Street Number", width= width_number)
edit_delivery_street_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_delivery_pc = TextInput(value=str(data_dict["delivery_pc"]), title="Delivery Postal Code/ZIP", width= width_number)
edit_delivery_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_delivery_street_name = TextInput(value=str(data_dict["delivery_street_name"]), title="Delivery Street Name", width= width_number)
edit_delivery_street_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_select_delivery_state = Select(title='Delivery State', value=str(data_dict["delivery_state"]), options=sorted(list(can_province_names.keys()) + list(us_states.keys())), width=width_number)
edit_select_delivery_state.on_change('value', update_kc_id)

edit_delivery_city = TextInput(value=str(data_dict["delivery_city"]), title="Delivery City", width= width_number)
edit_delivery_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_delivery_date = DatePicker(title="Delivery Date", value = "2024-01-01", width=width_number)

# OTHER
################
edit_div_other = Div(text=wrap_in_paragraphs("""Other""", 'black', size=3))

edit_other_carrier = TextInput(value=str(data_dict["carrier"]), title="Carrier", width= width_number)
edit_other_carrier.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_carrier_contact = TextInput(value=str(data_dict["carrier_contact"]), title="Carrier Contact", width= width_number)
edit_other_carrier_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_customer_contact = TextInput(value=str(data_dict["customer_contact"]), title="Customer Contact", width= width_number)
edit_other_customer_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_customer_invoice = Select(title='Customer Invoice Status', value=str(data_dict["customer_invoice_status"]), options=["UNPAID", "PAID"], width=width_number)
edit_other_customer_invoice.on_change('value', update_kc_id)

edit_other_carrier_invoice = Select(title='Carrier Invoice Status', value=str(data_dict["carrier_invoice_status"]), options=["UNPAID", "PAID"], width=width_number)
edit_other_carrier_invoice.on_change('value', update_kc_id)

edit_other_tailgate = Select(title='Tailgate', value=str(data_dict["tailgate"]), options=["NO", "YES"], width=width_number)
edit_other_tailgate.on_change('value', update_kc_id)

edit_other_storage = Select(title='Storage', value=str(data_dict["storage"]), options=["NO", "YES"], width=width_number)
edit_other_storage.on_change('value', update_kc_id)

edit_other_charge = TextInput(value=str(data_dict["charge"]), title="Charge", width= width_number)
edit_other_charge.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_profit = TextInput(value=str(data_dict["profit"]), title="Profit", width= width_number)
edit_other_profit.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_cost = TextInput(value=str(data_dict["cost"]), title="Cost", width= width_number)
edit_other_cost.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_special_notes = TextInput(value=str(data_dict["special_notes"]), title="Special Notes", width= 900)
edit_other_special_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

# COMMODITY
##################
edit_div_commodity = Div(text=wrap_in_paragraphs("""Commodity""", 'black', size=3))

edit_commodity_commodity = TextInput(value=str(data_dict["commodity"]), title="Commodity", width= width_number)
edit_commodity_commodity.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_commodity_weight = TextInput(value=str(data_dict["commodity_weight"]), title="Weight (LBS)", width= 200)
edit_commodity_weight.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_commodity_notes = TextInput(value=str(data_dict["commodity_notes"]), title="Notes", width= 900)
edit_commodity_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

skids = ast.literal_eval(data_dict["commodity_skids"])
empty_skids = {x:(0,0,0,0) for x in range(1,19)}
skids = {**empty_skids, **skids}

# SKIDS
skids_dict = {}
for x in range(1,19):
    skids_dict[f"edit_commodity_skid_number{x}"] = TextInput(value=str(skids[x][0]), title="Number of Skids", width= 200)
    skids_dict[f"edit_commodity_skid_number{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_height{x}"]  = TextInput(value=str(skids[x][3]), title="Skid Height (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_height{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_length{x}"] = TextInput(value=str(skids[x][1]), title="Skid Length (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_length{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_width{x}"] = TextInput(value=str(skids[x][2]), title="Skid Width (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_width{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

# LAYOUT
new_tab = TabPanel(
    child=column([row([new_info_div,new_select_kc_id]),
                    new_pickup_street_number,
                    new_pickup_street_name,
                    new_pickup_unit_number,
                    new_pickup_city,
                    new_select_pickup_state,
                    new_pickup_pc,
                    new_pickup_date,
                    new_delivery_date,
                    new_button]),
    title="New",
)
edit_tab = TabPanel(
    child=column([row([edit_info_div,edit_select_kc_id, column([row([search_button, edit_button,]),
                                                                row([create_bol_button, create_invoice_button, create_xx_button])])]),
edit_display_div,
                    row([
                        column([edit_div_pickup, edit_pickup_street_number,
                    edit_pickup_street_name,
                    edit_pickup_unit_number,
                    edit_pickup_city,
                    edit_select_pickup_state,
                    edit_pickup_pc,
                    edit_pickup_date,]),
                  edit_div_0,
                  column([edit_div_delivery, edit_delivery_street_number,
                  edit_delivery_street_name,
                  edit_delivery_unit_number,
                  edit_delivery_city,
                  edit_select_delivery_state,
                  edit_delivery_pc,
                    edit_delivery_date,]),]),
edit_div_2,
edit_div_other,
row([
column([edit_other_carrier,
edit_other_carrier_contact,
edit_other_customer_contact,
edit_other_customer_invoice,
edit_other_carrier_invoice,
        ])    ,
edit_div_1,
column([
    edit_other_cost,
edit_other_charge,
edit_other_profit,
edit_other_tailgate,
edit_other_storage,
]),
]),
edit_other_special_notes,
edit_div_3,
edit_div_commodity,
edit_commodity_commodity,
edit_commodity_weight,
edit_commodity_notes,
row([skids_dict[f"edit_commodity_skid_number1"], skids_dict[f"edit_commodity_skid_length1"], skids_dict[f"edit_commodity_skid_width1"], skids_dict[f"edit_commodity_skid_height1"]]),
row([skids_dict[f"edit_commodity_skid_number2"], skids_dict[f"edit_commodity_skid_length2"], skids_dict[f"edit_commodity_skid_width2"], skids_dict[f"edit_commodity_skid_height2"]]),
row([skids_dict[f"edit_commodity_skid_number3"], skids_dict[f"edit_commodity_skid_length3"], skids_dict[f"edit_commodity_skid_width3"], skids_dict[f"edit_commodity_skid_height3"]]),
row([skids_dict[f"edit_commodity_skid_number4"], skids_dict[f"edit_commodity_skid_length4"], skids_dict[f"edit_commodity_skid_width4"], skids_dict[f"edit_commodity_skid_height4"]]),
row([skids_dict[f"edit_commodity_skid_number5"], skids_dict[f"edit_commodity_skid_length5"], skids_dict[f"edit_commodity_skid_width5"], skids_dict[f"edit_commodity_skid_height5"]]),
row([skids_dict[f"edit_commodity_skid_number6"], skids_dict[f"edit_commodity_skid_length6"], skids_dict[f"edit_commodity_skid_width6"], skids_dict[f"edit_commodity_skid_height6"]]),
row([skids_dict[f"edit_commodity_skid_number7"], skids_dict[f"edit_commodity_skid_length7"], skids_dict[f"edit_commodity_skid_width7"], skids_dict[f"edit_commodity_skid_height7"]]),
row([skids_dict[f"edit_commodity_skid_number8"], skids_dict[f"edit_commodity_skid_length8"], skids_dict[f"edit_commodity_skid_width8"], skids_dict[f"edit_commodity_skid_height8"]]),
row([skids_dict[f"edit_commodity_skid_number9"], skids_dict[f"edit_commodity_skid_length9"], skids_dict[f"edit_commodity_skid_width9"], skids_dict[f"edit_commodity_skid_height9"]]),
row([skids_dict[f"edit_commodity_skid_number10"], skids_dict[f"edit_commodity_skid_length10"], skids_dict[f"edit_commodity_skid_width10"], skids_dict[f"edit_commodity_skid_height10"]]),
row([skids_dict[f"edit_commodity_skid_number11"], skids_dict[f"edit_commodity_skid_length11"], skids_dict[f"edit_commodity_skid_width11"], skids_dict[f"edit_commodity_skid_height11"]]),
row([skids_dict[f"edit_commodity_skid_number12"], skids_dict[f"edit_commodity_skid_length12"], skids_dict[f"edit_commodity_skid_width12"], skids_dict[f"edit_commodity_skid_height12"]]),
row([skids_dict[f"edit_commodity_skid_number13"], skids_dict[f"edit_commodity_skid_length13"], skids_dict[f"edit_commodity_skid_width13"], skids_dict[f"edit_commodity_skid_height13"]]),
row([skids_dict[f"edit_commodity_skid_number14"], skids_dict[f"edit_commodity_skid_length14"], skids_dict[f"edit_commodity_skid_width14"], skids_dict[f"edit_commodity_skid_height14"]]),
row([skids_dict[f"edit_commodity_skid_number15"], skids_dict[f"edit_commodity_skid_length15"], skids_dict[f"edit_commodity_skid_width15"], skids_dict[f"edit_commodity_skid_height15"]]),
row([skids_dict[f"edit_commodity_skid_number16"], skids_dict[f"edit_commodity_skid_length16"], skids_dict[f"edit_commodity_skid_width16"], skids_dict[f"edit_commodity_skid_height16"]]),
row([skids_dict[f"edit_commodity_skid_number17"], skids_dict[f"edit_commodity_skid_length17"], skids_dict[f"edit_commodity_skid_width17"], skids_dict[f"edit_commodity_skid_height17"]]),
row([skids_dict[f"edit_commodity_skid_number18"], skids_dict[f"edit_commodity_skid_length18"], skids_dict[f"edit_commodity_skid_width18"], skids_dict[f"edit_commodity_skid_height18"]]),
]),
    title="Edit/View",
)

tt = Tabs(tabs=[edit_tab, new_tab])
dashboard = row([tt])
curdoc().add_root(dashboard)
show(dashboard)

