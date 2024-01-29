from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker, RangeSlider
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, TextInput, CustomJS, Tabs, TabPanel
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column
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

database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv',
                       dtype={"delivery_street_number":str,
                                                                                "pickup_street_number":str}).replace(np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')
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

def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False
def update_kc_id(attr, old, new):
    pass
def update_edit():
    try:
        global database, skids_dict

        for x, y in skids_dict.items():
            assert y.value.isnumeric(), f"{x} ({y}) is not a number"

        edit_comm_dict = {x: (skids_dict[f"edit_commodity_skid_number{x}"].value,
                             skids_dict[f"edit_commodity_skid_length{x}"].value,
                             skids_dict[f"edit_commodity_skid_width{x}"].value,
                             skids_dict[f"edit_commodity_skid_height{x}"].value,
                             )
                         for x in range(1, 19)
                         }

        to_db_dict = {
            "kc_id": edit_select_kc_id.value,
            "pickup_unit_number": edit_pickup_unit_number.value,
            "pickup_street_number": edit_pickup_street_number.value,
            "pickup_pc": edit_pickup_pc.value.replace(' ', ""),
            "pickup_street_name": edit_pickup_street_name.value,
            "pickup_state": edit_select_pickup_state.value,
            "pickup_city": edit_pickup_city.value,
            "pickup_date": edit_pickup_date.value,

            "delivery_unit_number": edit_delivery_unit_number.value,
            "delivery_street_number": edit_delivery_street_number.value,
            "delivery_pc": edit_delivery_pc.value.replace(' ', ""),
            "delivery_street_name": edit_delivery_street_name.value,
            "delivery_state": edit_select_delivery_state.value,
            "delivery_city": edit_delivery_city.value,
            "delivery_date": edit_delivery_date.value,

            "carrier": edit_other_carrier.value,
            "carrier_contact": edit_other_carrier_contact.value,
            "customer_contact": edit_other_customer_contact.value,
            "customer_invoice_status": edit_other_customer_invoice.value,
            "carrier_invoice_status": edit_other_carrier_invoice.value,
            "tailgate": edit_other_tailgate.value,
            "storage": edit_other_storage.value,
            "charge": edit_other_charge.value,
            "profit": edit_other_profit.value,
            "cost": edit_other_cost.value,
            "special_notes": edit_other_special_notes.value,

            "commodity": edit_commodity_commodity.value,
            "commodity_weight": edit_commodity_weight.value,
            "commodity_notes": edit_commodity_notes.value,
            "commodity_skids": str(edit_comm_dict),
        }
        # ensure the postal code/zip codes are somewhat correct
        assert len(to_db_dict['pickup_pc']) >= 5, "Pickup PC too short"
        assert len(to_db_dict['pickup_pc']) <= 7, "Pickup PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['pickup_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Pickup ZIP / Postal Code ({to_db_dict['pickup_pc']})"

        assert len(to_db_dict['delivery_pc']) >= 5, "Delivery PC too short"
        assert len(to_db_dict['delivery_pc']) <= 7, "Delivery PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['delivery_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Delivery ZIP / Postal Code ({to_db_dict['delivery_pc']})"

        # ensure that the fields have the required entries
        assert len(to_db_dict['delivery_street_number']) > 1, "Delivery Street Number  needs to be filled."
        assert len(to_db_dict['delivery_city']) > 1, "Delivery City needs to be filled."
        assert len(to_db_dict['delivery_street_name']) > 1, "Delivery Street Name needs to be filled."

        assert len(to_db_dict['pickup_street_number']) > 1, "Pickup Street Number  needs to be filled."
        assert len(to_db_dict['pickup_city']) > 1, "Pickup City needs to be filled."
        assert len(to_db_dict['pickup_street_name']) > 1, "Pickup Street Name needs to be filled."

        assert len(to_db_dict['carrier_contact']) > 1, "Carrier Contact needs to be filled."
        assert len(to_db_dict['customer_contact']) > 1, "Customer Contact needs to be filled."
        assert len(to_db_dict['carrier']) > 1, "Carrier needs to be filled."

        # ensure that only numbers are entered into Charge/Profit/Cost fields
        assert is_number_tryexcept(str(to_db_dict['charge'])), f"Charge is not a number ({str(to_db_dict['charge'])})"
        assert is_number_tryexcept(str(to_db_dict['cost'])), f"Cost is not a number ({str(to_db_dict['cost'])})"
        assert is_number_tryexcept(str(to_db_dict['profit'])), f"Profit is not a number ({str(to_db_dict['profit'])})"
        assert float(to_db_dict['charge']) - float(to_db_dict['cost']) == float(
            to_db_dict['profit']), "Charge - Cost =/= Profit"

        # assert the commodity information (aside from skids that was already done)
        assert str(to_db_dict['commodity_weight']).isnumeric(), "Commodity Weight is not a number"
        assert len(to_db_dict['commodity']) > 1, "Commodity needs to be filled."
        assert len(to_db_dict['commodity_skids']) > 6, "Commodity Skids needs to be filled."

        # assert that the delivery date is after the pickup date
        assert to_db_dict['delivery_date'] >= to_db_dict['pickup_date'], "Pickup Date must be before Delivery Date"

        # add the new data to the database file and write it to disk
        database_modified = pd.concat([database, pd.DataFrame(to_db_dict, index=[0])], ignore_index=True)
        # print(database_modified.to_string())
        database_modified.to_csv(data_path + 'kc_logistics_corp_booking_data.csv', index=False)

        # confirm that data for the KC_ID was added to the database file.
        edit_display_div.text = wrap_in_paragraphs(f"Data for {edit_select_kc_id.value} passed to the database")
        time.sleep(2)
        # reset the database file, with the newest row added
        database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv', dtype={"delivery_street_number": str,
                                                                                        "pickup_street_number": str}).replace(
            np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')
    except Exception as iee:
        print(iee)
        edit_display_div.text = wrap_in_paragraphs(f"Error: {iee}")

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
    try:
        global database, new_skids_dict

        for x,y in new_skids_dict.items():
            assert y.value.isnumeric(), f"{x} ({y}) is not a number"

        new_comm_dict = {x:(new_skids_dict[f"new_commodity_skid_number{x}"].value,
                            new_skids_dict[f"new_commodity_skid_length{x}"].value,
                            new_skids_dict[f"new_commodity_skid_width{x}"].value,
                            new_skids_dict[f"new_commodity_skid_height{x}"].value,
                            )
            for x in range(1,19)
        }

        to_db_dict = {
        "kc_id": new_select_kc_id.value,
        "pickup_unit_number": new_pickup_unit_number.value,
        "pickup_street_number": new_pickup_street_number.value,
        "pickup_pc": new_pickup_pc.value.replace(' ', ""),
        "pickup_street_name": new_pickup_street_name.value,
        "pickup_state": new_select_pickup_state.value,
        "pickup_city": new_pickup_city.value,
        "pickup_date": new_pickup_date.value,

        "delivery_unit_number": new_delivery_unit_number.value,
        "delivery_street_number": new_delivery_street_number.value,
        "delivery_pc": new_delivery_pc.value.replace(' ', ""),
        "delivery_street_name": new_delivery_street_name.value,
        "delivery_state": new_select_delivery_state.value,
        "delivery_city": new_delivery_city.value,
        "delivery_date": new_delivery_date.value,

        "carrier": new_other_carrier.value,
        "carrier_contact": new_other_carrier_contact.value,
        "customer_contact": new_other_customer_contact.value,
        "customer_invoice_status": new_other_customer_invoice.value,
        "carrier_invoice_status": new_other_carrier_invoice.value,
        "tailgate": new_other_tailgate.value,
        "storage": new_other_storage.value,
        "charge": new_other_charge.value,
        "profit": new_other_profit.value,
        "cost": new_other_cost.value,
        "special_notes": new_other_special_notes.value,

        "commodity": new_commodity_commodity.value,
        "commodity_weight": new_commodity_weight.value,
        "commodity_notes": new_commodity_notes.value,
        "commodity_skids":str(new_comm_dict),
        }
        # ensure the postal code/zip codes are somewhat correct
        assert len(to_db_dict['pickup_pc']) >= 5, "Pickup PC too short"
        assert len(to_db_dict['pickup_pc']) <= 7, "Pickup PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['pickup_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Pickup ZIP / Postal Code ({to_db_dict['pickup_pc']})"

        assert len(to_db_dict['delivery_pc']) >= 5, "Delivery PC too short"
        assert len(to_db_dict['delivery_pc']) <= 7, "Delivery PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['delivery_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Delivery ZIP / Postal Code ({to_db_dict['delivery_pc']})"

        # ensure that the fields have the required entries
        assert len(to_db_dict['delivery_street_number']) > 1 , "Delivery Street Number  needs to be filled."
        assert len(to_db_dict['delivery_city']) > 1 , "Delivery City needs to be filled."
        assert len(to_db_dict['delivery_street_name']) > 1 , "Delivery Street Name needs to be filled."

        assert len(to_db_dict['pickup_street_number']) > 1 , "Pickup Street Number  needs to be filled."
        assert len(to_db_dict['pickup_city']) > 1 , "Pickup City needs to be filled."
        assert len(to_db_dict['pickup_street_name']) > 1 , "Pickup Street Name needs to be filled."

        assert len(to_db_dict['carrier_contact']) > 1 , "Carrier Contact needs to be filled."
        assert len(to_db_dict['customer_contact']) > 1 , "Customer Contact needs to be filled."
        assert len(to_db_dict['carrier']) > 1 , "Carrier needs to be filled."

        # ensure that only numbers are entered into Charge/Profit/Cost fields
        assert is_number_tryexcept(str(to_db_dict['charge'])), f"Charge is not a number ({str(to_db_dict['charge'])})"
        assert is_number_tryexcept(str(to_db_dict['cost'])), f"Cost is not a number ({str(to_db_dict['cost'])})"
        assert is_number_tryexcept(str(to_db_dict['profit'])), f"Profit is not a number ({str(to_db_dict['profit'])})"
        assert float(to_db_dict['charge']) - float(to_db_dict['cost']) == float(to_db_dict['profit']), "Charge - Cost =/= Profit"

        # assert the commodity information (aside from skids that was already done)
        assert str(to_db_dict['commodity_weight']).isnumeric(), "Commodity Weight is not a number"
        assert len(to_db_dict['commodity']) > 1 , "Commodity needs to be filled."
        assert len(to_db_dict['commodity_skids']) > 6 , "Commodity Skids needs to be filled."

        # assert that the delivery date is after the pickup date
        assert to_db_dict['delivery_date'] >= to_db_dict['pickup_date'] , "Pickup Date must be before Delivery Date"

        # add the new data to the database file and write it to disk
        database_modified = pd.concat([database, pd.DataFrame(to_db_dict, index=[0])], ignore_index=True)
        # print(database_modified.to_string())
        database_modified.to_csv(data_path + 'kc_logistics_corp_booking_data.csv', index=False)

        # confirm that data for the KC_ID was added to the database file.
        new_display_div.text = wrap_in_paragraphs(f"Data for {new_select_kc_id.value} passed to the database")
        time.sleep(2)
        # reset the database file, with the newest row added
        database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv', dtype={"delivery_street_number": str,
                                                                                        "pickup_street_number": str}).replace(
            np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')
        # find the next KC_ID value
        next_kc_id_ = 'KC' + str(max([int(x[2:]) for x in database['kc_id'].values]) + 1)
        new_select_kc_id.value = next_kc_id_
        new_select_kc_id.options = [next_kc_id_]
        edit_select_kc_id.options = database['kc_id'].to_list()

        # reset some fields so that a double tab doesn't add a second row of the same data
        new_delivery_unit_number.value = ""
        new_delivery_pc.value = ""
        new_delivery_street_number.value = ""
        new_delivery_street_name.value = ""
        new_delivery_city.value = ""

        new_pickup_street_number.value = ""
        new_pickup_pc.value = ""
        new_pickup_unit_number.value = ""
        new_pickup_street_name.value = ""
        new_pickup_city.value = ""

        new_other_profit.value = ""
        new_other_cost.value = ""
        new_other_charge.value = ""
        new_other_carrier.value = ""
        new_other_carrier_contact.value = ""
        new_other_customer_contact.value = ""

        new_commodity_commodity.value = ""
        new_commodity_weight.value = ""
        new_commodity_notes.value = ""

    except Exception as eee:
        print(eee)
        new_display_div.text = wrap_in_paragraphs(f"Error: {eee}")

    
def update_create_invoice():
    pass
def update_create_bol():
    pass

def update_create_loadconf():
    pass

def update_kc_id_next(attkc_idr, old, new):
    pass

width_number = 400

title_div = Div(text=wrap_in_paragraphs('KC Logistics Data Input', 'black', size=5), width = width_number)
new_info_div = Div(text=wrap_in_paragraphs("""New Data Input for KC Logistics Data """, 'black', size=3), width = 300)

new_display_div = Div(text="")

next_kc_id = 'KC' + str(max([int(x[2:]) for x in database['kc_id'].values]) + 1)

new_select_kc_id =  Select(title='KC_ID', value=next_kc_id, options=[next_kc_id], width=width_number)
new_select_kc_id.on_change('value', update_kc_id_next)

new_div_0 = Div(text = '_'*15)
new_div_1 = Div(text = '_'*15)
new_div_2 = Div(text = '_'*130)
new_div_3 = Div(text = '_'*130)

### PICKUP
new_div_pickup = Div(text=wrap_in_paragraphs("""Pickup""", 'black', size=3))

new_pickup_unit_number = TextInput(value=str(""), title="Pickup Unit Number", width= width_number)
new_pickup_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_street_number = TextInput(value=str(""), title="Pickup Street Number", width= width_number)
new_pickup_street_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_pc = TextInput(value=str(""), title="Pickup Postal Code/ZIP", width= width_number)
new_pickup_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_street_name = TextInput(value=str(""), title="Pickup Street Name", width= width_number)
new_pickup_street_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_pickup_state = Select(title='Pickup State', value=str(""), options=sorted(list(can_province_names.keys()) + list(us_states.keys())), width=width_number)
new_select_pickup_state.on_change('value', update_kc_id)

new_pickup_city = TextInput(value=str(""), title="Pickup City", width= width_number)
new_pickup_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_date = DatePicker(title="Pick Up Date", value = "2024-01-01", width=width_number)

# DELIVERY
######################################
new_div_delivery = Div(text=wrap_in_paragraphs("""Delivery""", 'black', size=3))

new_delivery_unit_number = TextInput(value=str(""), title="Delivery Unit Number", width= width_number)
new_delivery_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_delivery_street_number = TextInput(value=str(""), title="Delivery Street Number", width= width_number)
new_delivery_street_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_delivery_pc = TextInput(value=str(""), title="Delivery Postal Code/ZIP", width= width_number)
new_delivery_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_delivery_street_name = TextInput(value=str(""), title="Delivery Street Name", width= width_number)
new_delivery_street_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_delivery_state = Select(title='Delivery State', value=str(""), options=sorted(list(can_province_names.keys()) + list(us_states.keys())), width=width_number)
new_select_delivery_state.on_change('value', update_kc_id)

new_delivery_city = TextInput(value=str(""), title="Delivery City", width= width_number)
new_delivery_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_delivery_date = DatePicker(title="Delivery Date", value = "2024-01-01", width=width_number)

# OTHER
################
new_div_other = Div(text=wrap_in_paragraphs("""Other""", 'black', size=3))

new_other_carrier = TextInput(value=str(""), title="Carrier", width= width_number)
new_other_carrier.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_carrier_contact = TextInput(value=str(""), title="Carrier Contact", width= width_number)
new_other_carrier_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_customer_contact = TextInput(value=str(""), title="Customer Contact", width= width_number)
new_other_customer_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_customer_invoice = Select(title='Customer Invoice Status', value=str("UNPAID"), options=["UNPAID", "PAID"], width=width_number)
new_other_customer_invoice.on_change('value', update_kc_id)

new_other_carrier_invoice = Select(title='Carrier Invoice Status', value=str("UNPAID"), options=["UNPAID", "PAID"], width=width_number)
new_other_carrier_invoice.on_change('value', update_kc_id)

new_other_tailgate = Select(title='Tailgate', value=str("NO"), options=["NO", "YES"], width=width_number)
new_other_tailgate.on_change('value', update_kc_id)

new_other_storage = Select(title='Storage', value=str("NO"), options=["NO", "YES"], width=width_number)
new_other_storage.on_change('value', update_kc_id)

new_other_charge = TextInput(value=str(0.0), title="Charge", width= width_number)
new_other_charge.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_profit = TextInput(value=str(0.0), title="Profit", width= width_number)
new_other_profit.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_cost = TextInput(value=str(0.0), title="Cost", width= width_number)
new_other_cost.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_special_notes = TextInput(value=str(""), title="Special Notes", width= 900)
new_other_special_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

# COMMODITY
##################
new_div_commodity = Div(text=wrap_in_paragraphs("""Commodity""", 'black', size=3))

new_commodity_commodity = TextInput(value=str(""), title="Commodity", width= width_number)
new_commodity_commodity.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_commodity_weight = TextInput(value=str(""), title="Weight (LBS)", width= 200)
new_commodity_weight.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_commodity_notes = TextInput(value=str(""), title="Notes", width= 900)
new_commodity_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


new_skids = {x:(0,0,0,0) for x in range(1,19)}

# SKIDS
new_skids_dict = {}
for x in range(1,19):
    new_skids_dict[f"new_commodity_skid_number{x}"] = TextInput(value=str(new_skids[x][0]), title="Number of Skids", width= 200)
    new_skids_dict[f"new_commodity_skid_number{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_height{x}"]  = TextInput(value=str(new_skids[x][3]), title="Skid Height (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_height{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_length{x}"] = TextInput(value=str(new_skids[x][1]), title="Skid Length (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_length{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_width{x}"] = TextInput(value=str(new_skids[x][2]), title="Skid Width (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_width{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_button = Button(label="Input Info to Database", button_type="primary", width=200)
new_button.on_click(update_new)

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

create_loadconf_button = Button(label="Create Load Conf.", button_type="warning", width=100)
create_loadconf_button.on_click(update_create_loadconf)

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
    child=column([row([new_info_div, new_select_kc_id, new_button]),
                  new_display_div,
                  row([
                      column([new_div_pickup, new_pickup_street_number,
                              new_pickup_street_name,
                              new_pickup_unit_number,
                              new_pickup_city,
                              new_select_pickup_state,
                              new_pickup_pc,
                              new_pickup_date, ]),
                      new_div_0,
                      column([new_div_delivery, new_delivery_street_number,
                              new_delivery_street_name,
                              new_delivery_unit_number,
                              new_delivery_city,
                              new_select_delivery_state,
                              new_delivery_pc,
                              new_delivery_date, ]), ]),
                  new_div_2,
                  new_div_other,
                  row([
                      column([new_other_carrier,
                              new_other_carrier_contact,
                              new_other_customer_contact,
                              new_other_customer_invoice,
                              new_other_carrier_invoice,
                              ]),
                      new_div_1,
                      column([
                          new_other_cost,
                          new_other_charge,
                          new_other_profit,
                          new_other_tailgate,
                          new_other_storage,
                      ]),
                  ]),
                  new_other_special_notes,
                  new_div_3,
                  new_div_commodity,
                  new_commodity_commodity,
                  new_commodity_weight,
                  new_commodity_notes,
                  row([new_skids_dict[f"new_commodity_skid_number1"], new_skids_dict[f"new_commodity_skid_length1"],
                       new_skids_dict[f"new_commodity_skid_width1"], new_skids_dict[f"new_commodity_skid_height1"]]),
                  row([new_skids_dict[f"new_commodity_skid_number2"], new_skids_dict[f"new_commodity_skid_length2"],
                       new_skids_dict[f"new_commodity_skid_width2"], new_skids_dict[f"new_commodity_skid_height2"]]),
                  row([new_skids_dict[f"new_commodity_skid_number3"], new_skids_dict[f"new_commodity_skid_length3"],
                       new_skids_dict[f"new_commodity_skid_width3"], new_skids_dict[f"new_commodity_skid_height3"]]),
                  row([new_skids_dict[f"new_commodity_skid_number4"], new_skids_dict[f"new_commodity_skid_length4"],
                       new_skids_dict[f"new_commodity_skid_width4"], new_skids_dict[f"new_commodity_skid_height4"]]),
                  row([new_skids_dict[f"new_commodity_skid_number5"], new_skids_dict[f"new_commodity_skid_length5"],
                       new_skids_dict[f"new_commodity_skid_width5"], new_skids_dict[f"new_commodity_skid_height5"]]),
                  row([new_skids_dict[f"new_commodity_skid_number6"], new_skids_dict[f"new_commodity_skid_length6"],
                       new_skids_dict[f"new_commodity_skid_width6"], new_skids_dict[f"new_commodity_skid_height6"]]),
                  row([new_skids_dict[f"new_commodity_skid_number7"], new_skids_dict[f"new_commodity_skid_length7"],
                       new_skids_dict[f"new_commodity_skid_width7"], new_skids_dict[f"new_commodity_skid_height7"]]),
                  row([new_skids_dict[f"new_commodity_skid_number8"], new_skids_dict[f"new_commodity_skid_length8"],
                       new_skids_dict[f"new_commodity_skid_width8"], new_skids_dict[f"new_commodity_skid_height8"]]),
                  row([new_skids_dict[f"new_commodity_skid_number9"], new_skids_dict[f"new_commodity_skid_length9"],
                       new_skids_dict[f"new_commodity_skid_width9"], new_skids_dict[f"new_commodity_skid_height9"]]),
                  row([new_skids_dict[f"new_commodity_skid_number10"], new_skids_dict[f"new_commodity_skid_length10"],
                       new_skids_dict[f"new_commodity_skid_width10"], new_skids_dict[f"new_commodity_skid_height10"]]),
                  row([new_skids_dict[f"new_commodity_skid_number11"], new_skids_dict[f"new_commodity_skid_length11"],
                       new_skids_dict[f"new_commodity_skid_width11"], new_skids_dict[f"new_commodity_skid_height11"]]),
                  row([new_skids_dict[f"new_commodity_skid_number12"], new_skids_dict[f"new_commodity_skid_length12"],
                       new_skids_dict[f"new_commodity_skid_width12"], new_skids_dict[f"new_commodity_skid_height12"]]),
                  row([new_skids_dict[f"new_commodity_skid_number13"], new_skids_dict[f"new_commodity_skid_length13"],
                       new_skids_dict[f"new_commodity_skid_width13"], new_skids_dict[f"new_commodity_skid_height13"]]),
                  row([new_skids_dict[f"new_commodity_skid_number14"], new_skids_dict[f"new_commodity_skid_length14"],
                       new_skids_dict[f"new_commodity_skid_width14"], new_skids_dict[f"new_commodity_skid_height14"]]),
                  row([new_skids_dict[f"new_commodity_skid_number15"], new_skids_dict[f"new_commodity_skid_length15"],
                       new_skids_dict[f"new_commodity_skid_width15"], new_skids_dict[f"new_commodity_skid_height15"]]),
                  row([new_skids_dict[f"new_commodity_skid_number16"], new_skids_dict[f"new_commodity_skid_length16"],
                       new_skids_dict[f"new_commodity_skid_width16"], new_skids_dict[f"new_commodity_skid_height16"]]),
                  row([new_skids_dict[f"new_commodity_skid_number17"], new_skids_dict[f"new_commodity_skid_length17"],
                       new_skids_dict[f"new_commodity_skid_width17"], new_skids_dict[f"new_commodity_skid_height17"]]),
                  row([new_skids_dict[f"new_commodity_skid_number18"], new_skids_dict[f"new_commodity_skid_length18"],
                       new_skids_dict[f"new_commodity_skid_width18"], new_skids_dict[f"new_commodity_skid_height18"]]),
                  ]),
    title="New",
)
edit_tab = TabPanel(
    child=column([row([edit_info_div,edit_select_kc_id, column([row([search_button, edit_button,]),
                                                                row([create_bol_button, create_invoice_button, create_loadconf_button])])]),
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
