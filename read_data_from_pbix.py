import os, glob
import json
import zipfile
import shutil
from pprint import pprint
import pandas as pd
import traceback
from colour import Color
import colorsys
from collections import Counter
import numpy as np
import datetime
import pymongo
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
import time
import logging
import re
from power_bi_aoda_viz import make_dashboards

path = os.getcwd().replace('\\', "/") + "/"
# report_path = path + 'original_dashboards/socio/'
report_path = path + 'reports/'
engine = sqlite3.connect(path + 'power_bi_database.db')

logging.basicConfig(level=logging.INFO, format='%(asctime)s, %(message)s', handlers=[logging.FileHandler("power_bi_parser_log.txt"), logging.StreamHandler()])

mongo_db = pymongo.MongoClient('localhost', 27017)
pbi_mongo = mongo_db['power_bi']
pbi_mongo_dashboards = pbi_mongo['dashboards']
pbi_mongo_uploads = pbi_mongo['uploads']

# misc functions
def error_handling():
    """

    This function returns a string with all of the information regarding the error

    :return: string with the error information
    """
    return traceback.format_exc()
def final_text_clean(text):
    """
    This function takes input text and cleans it up by removing punctuation.
    :param text: input string
    :return: the input string without preceeding and trailing punctuation.
    """
    if text.startswith("'"):
        text = text[1:]
    if text.startswith("''"):
        text = text[2:]
    if text.endswith("'"):
        text = text[:-1]
    if text.endswith("''"):
        text = text[:-2]
    if text.endswith(")"):
        if '(' not in text:
            text = text[:-1]
    return text

# font functions
def get_chart_title_font(visual_data, shades):
    """
    For the input *visual_data* parse the title's attributes from it and return in as a dictionary. The dictionary contains information about font family, font size and alignment of the title.

    :param visual_data: data of the chart in JSON / dictionary form
    :param shades: the colours/shades of the theme for this report
    :return: a dictionary with keys: alignment, font_family and font_size
    """
    # if colour is set by user using 'custom colour'
    try:
        title_font_colour = visual_data['vcObjects']['title'][0]['properties']['color']['solid']['color']['expr']['Literal']['Value']
    except:
        try: # if colour is set by user using one of the theme colours
            col = visual_data['vcObjects']['title'][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['vcObjects']['title'][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['Percent']
            title_font_colour = get_colour_from_theme(col, opacity, shades)
        except: # if not set by user
            try:
                title_font_colour = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value']
            except:
                try:  # if colour is set by user using one of the theme colours
                    col = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                    opacity = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
                    title_font_colour = get_colour_from_theme(col, opacity, shades)
                except:
                    title_font_colour = 'default'
    try: # if alignment set by user
        title_alignment = final_text_clean(visual_data['vcObjects']['title'][0]['properties']['alignment']['expr']['Literal']['Value'])
    except:
        title_alignment = 'default'
    try: # if font size set by user
        title_font_size = final_text_clean(visual_data['vcObjects']['title'][0]['properties']['fontSize']['expr']['Literal']['Value'])
    except:
        title_font_size = 'default'
    print('waste', title_alignment, title_font_colour, title_font_size)
    return {'font_colour' : final_text_clean(title_font_colour), 'alignment': title_alignment, 'font_size':title_font_size}
def get_data_value_font(visual_data, shades):
    return {'font_family': get_font_family(visual_data, indicator = 'labels'), 'font_size':get_font_size(visual_data, indicator = 'labels'), 'font_colour':get_font_colour(visual_data, shades, indicator = 'labels'),  }
def get_card_font(visual_data, shades):
    return {'font_family': get_font_family(visual_data, indicator = 'dataLabels'), 'font_size':get_font_size(visual_data, indicator = 'dataLabels'), 'font_colour':get_font_colour(visual_data, shades, indicator = 'dataLabels'),}
def get_slicer_date_font(visual_data, shades):
    try:
        val = final_text_clean(visual_data['objects']['date'][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value'])
    except:
        try:
            col = visual_data['objects']['date'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects']['date'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
            val = get_colour_from_theme(col, opacity, shades)
        except:
            val = 'default'
    try:
        back = final_text_clean(visual_data['objects']['date'][0]['properties']['background']['solid']['color']['expr']['Literal']['Value'])
    except:
        try:
            col = visual_data['objects']['date'][0]['properties']['background']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects']['date'][0]['properties']['background']['solid']['color']['expr']['ThemeDataColor']['Percent']
            back = get_colour_from_theme(col, opacity, shades)
        except:
            back = 'default'
    font_size = get_font_size(visual_data, 'date')
    font_family = get_font_family(visual_data, 'date')
    return {'font_colour':val, "background_colour":back, 'font_size':font_size, 'font_family':font_family}
def get_font_colour(visual_data, shades, indicator = 'dataLabels'):
    try:
        val = final_text_clean(visual_data['objects'][indicator][0]['properties']['color']['solid']['color']['expr']['Literal']['Value'])
    except:
        try:
            col = visual_data['objects'][indicator][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects'][indicator][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['Percent']
            val = get_colour_from_theme(col, opacity, shades)
        except:
            val = 'default'
    return val
def get_font_size(visual_data, indicator = 'dataLabels'):
    try:
        text = final_text_clean(visual_data['objects'][indicator][0]['properties']['fontSize']['expr']['Literal']['Value'])
    except:
        text = 'default'
    return text
def get_font_family(visual_data, indicator = 'dataLabels'):
    try:
        text = final_text_clean(visual_data['objects'][indicator][0]['properties']['fontFamily']['expr']['Literal']['Value'])
    except:
        text = 'default'
    return text
def get_button_font(visual_data, shades):
    # if user selects - don't show text
    if visual_data['objects']['text'][0]['properties']['show']['expr']['Literal']['Value'].lower() == 'false':
        return {}
    try:
        font_colour = visual_data['objects']['text'][1]['properties']['color']['solid']['color']['expr']['Literal']['Value']
    except:
        try:
            col = visual_data['objects']['text'][1]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects']['text'][1]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
            font_colour = get_colour_from_theme(col, opacity, shades)
        except:
            font_colour = 'default'
    try:
        font_size = final_text_clean(visual_data['objects']['text'][1]['properties']['fontSize']['expr']['Literal']['Value'])
    except:
        font_size =  'default'
    try:
        font_family = final_text_clean(visual_data['objects']['text'][1]['properties']['fontFamily']['expr']['Literal']['Value'])
    except:
        font_family = 'default'
    return {'font_family':font_family, 'font_size':font_size, 'font_colour':font_colour}
def get_textbox_font(visual_data,):
    a = visual_data['objects']['general'][0]['properties']['paragraphs'][0]['textRuns']
    colours = []
    sizes = []
    fams = []

    for i in a:
        try:
            col = i['textStyle']['color']
        except:
            col = 'default'
        colours.append(col)
        try:
            size = final_text_clean(i['textStyle']['fontSize'])
        except:
            size = 'default'
        sizes.append(size)
        try:
            family = final_text_clean(i['textStyle']['fontFamily'])
        except:
            family = 'default'
        fams.append(family)
    return {'font_colour': list(set(colours)), 'font_size': list(set(sizes)), 'font_family': list(set(fams))}
def get_legend_font(visual_data, shades):
    # if legend doesn't appear, return empty dic
    try:
        if visual_data['objects']['legend'][0]['properties']['show']['expr']['Literal']['Value'].lower() == 'false':
            return {}
    except:
        pass
    try:
        font_colour = visual_data['objects']['legend'][0]['properties']['labelColor']['solid']['color']['expr']['Literal']['Value']
    except:
        try:
            col = visual_data['objects']['legend'][0]['properties']['labelColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects']['legend'][0]['properties']['labelColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
            font_colour = get_colour_from_theme(col, opacity, shades,)
        except:
            print('cool', error_handling())
            font_colour = 'default'
    return {'font_family':get_font_family(visual_data, 'legend'), 'font_size':get_font_size(visual_data, 'legend'), 'font_colour':final_text_clean(font_colour)}
def get_slicer_items_font(visual_data, shades):
    try:
        if visual_data['objects']['categoryAxis'][0]['properties']['show']['expr']['Literal']['Value'].lower() == 'false':
            return {}
    except:
        pass
    data_value = {'font_family': get_font_family(visual_data, 'items'), 'font_size': get_font_size(visual_data, 'items')}
    try:
        data_value['font_colour'] = final_text_clean(visual_data['objects']['items'][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value'])
    except:
        try:
            col = visual_data['objects']['items'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['objects']['items'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
            actual_colour = get_colour_from_theme(col, opacity, shades)
            data_value['font_colour'] = actual_colour
        except:
            data_value['font_colour'] = 'default'
    return data_value
def get_axis_font(visual_data, shades, axis_type = 'valueAxis'):
    # labels are showing unless specified not to.
    show_labels = True
    try:
        if visual_data['objects'][axis_type][0]['properties']['show']['expr']['Literal']['Value'].lower() == 'false':
            show_labels = False # labels don't show
    except:
        pass
    data_value = {}
    # if labels are showing, find them, else return none
    if show_labels:
        try: # get the font family of the axis labels
            data_value['font_family'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['fontFamily']['expr']['Literal']['Value'])
        except:
            data_value['font_family'] = 'default'
        try: # get the font size of the axis labels
            data_value['font_size'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['fontSize']['expr']['Literal']['Value'])
        except:
            data_value['font_size'] = 'default'
        try: # get the font colour of the axis labels
            data_value['font_colour'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['labelColor']['solid']['color']['expr']['Literal']['Value'])
        except:
            try:
                col = visual_data['objects'][axis_type][0]['properties']['labelColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects'][axis_type][0]['properties']['labelColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
                actual_colour = get_colour_from_theme(col, opacity, shades)
                data_value['font_colour'] = actual_colour
            except:
                data_value['font_colour'] = 'default'
    else:
        data_value = None

    show_title = True
    try:
        if visual_data['objects'][axis_type][0]['properties']['showAxisTitle']['expr']['Literal']['Value'].lower() == 'false':
            show_title = False # labels don't show
    except:
        pass
    title = {}
    if show_title:
        try:
            title['font_family'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['titleFontFamily']['expr']['Literal']['Value'])
        except:
            title['font_family'] = 'default'
        try:
            title['font_size'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['titleFontSize']['expr']['Literal']['Value'])
        except:
            title['font_size'] = 'default'
        try:
            title['font_colour'] = final_text_clean(visual_data['objects'][axis_type][0]['properties']['titleColor']['solid']['color']['expr']['Literal']['Value'])
        except:
            try:
                col = visual_data['objects'][axis_type][0]['properties']['titleColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects'][axis_type][0]['properties']['titleColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
                actual_colour = get_colour_from_theme(col, opacity, shades)
                title['font_colour'] = actual_colour
            except:
                title['font_colour'] = 'default'
    else:
        title = None
    return {'labels':data_value, 'title': title}
def get_table_font(visual_data, shades):
    q = {}
    # grid values of the table
    try:
        grid_font_size = visual_data['objects']['grid'][0]['properties']['textSize']['expr']['Literal']['Value']
    except:
        grid_font_size = 'default'
    q['grid'] = {'font_size': final_text_clean(grid_font_size)}
    # column header and row header
    mapper = {'columnHeaders':'column_header', 'rowHeaders':'row_header', 'backColorPrimary':'primary_background_colour','backColor':'background_colour','backColorSecondary':'secondary_background_colour','fontColor':'font_colour','fontColorPrimary':'primary_font_colour','fontColorSecondary':'secondary_font_colour'}
    for each in ['columnHeaders', 'rowHeaders']:
        # font size
        try:
            column_header_font_size = visual_data['objects'][each][0]['properties']['fontSize']['expr']['Literal']['Value']
        except:
            column_header_font_size = 'default'
        # font colour
        try:
            column_header_font_colour = visual_data['objects'][each][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value']
        except:
            try:
                col = visual_data['objects'][each][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects'][each][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                column_header_font_colour = get_colour_from_theme(col, opacity, shades)
            except:
                column_header_font_colour = 'default'
        # background colour
        try:
            column_header_background_colour = visual_data['objects'][each][0]['properties']['backColor']['solid']['color']['expr']['Literal']['Value']
        except:
            try:
                col = visual_data['objects'][each][0]['properties']['backColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects'][each][0]['properties']['backColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
                column_header_background_colour = get_colour_from_theme(col, opacity, shades)
            except:
                column_header_background_colour = 'default'
        q[mapper[each]] = {'background_colour':final_text_clean(column_header_background_colour), 'font_colour':final_text_clean(column_header_font_colour), 'font_size': final_text_clean(column_header_font_size)}
    # values of the table
    try:
        values_font_size = visual_data['objects']['values'][0]['properties']['fontSize']['expr']['Literal']['Value']
    except:
        values_font_size = 'default'
    try:
        values_font_family = visual_data['objects']['values'][0]['properties']['fontFamily']['expr']['Literal']['Value']
    except:
        values_font_family = 'default'
    tmp_dict = {'font_size':final_text_clean(values_font_size), 'font_family':final_text_clean(values_font_family)}
    for each in ['backColorPrimary','backColorSecondary','fontColorPrimary','fontColorSecondary',]:
        try:
            tmp_colour = visual_data['objects']['values'][0]['properties'][each]['solid']['color']['expr']['Literal']['Value']
        except:
            try:
                col = visual_data['objects']['values'][0]['properties'][each]['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects']['values'][0]['properties'][each]['solid']['color']['expr']['ThemeDataColor']['Percent']
                tmp_colour = get_colour_from_theme(col, opacity, shades)
            except:
                tmp_colour = 'default'
        if tmp_colour == 'default':
            if each == 'backColorSecondary':
                tmp_colour = '#EEEDED'
            if each == 'backColorPrimary':
                tmp_colour = '#FFF'
        tmp_dict[mapper[each]] = final_text_clean(tmp_colour)
    q['values'] = tmp_dict
    return q
def get_slicer_title_font(visual_data, shades):
    # if colour is set by user using 'custom colour'
    try:
        title_font_colour = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value']
    except:
        try: # if colour is set by user using one of the theme colours
            col = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['vcObjects']['title'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
            title_font_colour = get_colour_from_theme(col, opacity, shades)
        except: # if not set by user
            title_font_colour = 'default'
    output = {'font_colour' : final_text_clean(title_font_colour)}
    try: # if set by user
        output['alignment'] = final_text_clean(visual_data['vcObjects']['title'][0]['properties']['alignment']['expr']['Literal']['Value'])
    except:
        output['alignment'] = 'default'
    try: # if set by user
        output['font_size'] = final_text_clean(visual_data['vcObjects']['title'][0]['properties']['fontSize']['expr']['Literal']['Value'])
    except:
        output['font_size'] = 'default'
    output['type'] = 'title'
    if (output["font_colour"] == 'default' and output["alignment"] == 'default' and output["font_size"] == 'default') or output == 'No fonts detected':
        try:
            if visual_data['objects']['header'][0]['properties']['show']['expr']["Literal"]['Value'] == 'false':
                if visual_data['vcObjects']['title'][0]['properties']['show']['expr']["Literal"]['Value'] == 'false':
                    return
                elif visual_data['vcObjects']['title'][0]['properties']['show']['expr']["Literal"]['Value'] == 'true':
                    return output
        except:
            pass
        # font size
        try:
            header_font_size = visual_data['objects']['header'][0]['properties']['textSize']['expr']['Literal']['Value']
        except:
            header_font_size = 'default'
        # font family
        header_font_family = get_font_family(visual_data, 'header')
        # font colour
        try:
            header_font_colour = visual_data['objects']['header'][0]['properties']['fontColor']['solid']['color']['expr']['Literal']['Value']
        except:
            try:
                col = visual_data['objects']['header'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects']['header'][0]['properties']['fontColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                header_font_colour = get_colour_from_theme(col, opacity, shades)
            except:
                header_font_colour = 'default'
        # background colour
        try:
            header_background_colour = visual_data['objects']['header'][0]['properties']['background']['solid']['color']['expr']['Literal']['Value']
        except:
            try:
                col = visual_data['objects']['header'][0]['properties']['background']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                opacity = visual_data['objects']['header'][0]['properties']['background']['solid']['color']['expr']['ThemeDataColor']['Percent']
                header_background_colour = get_colour_from_theme(col, opacity, shades)
            except:
                header_background_colour = 'default'
        output = {'background_colour': final_text_clean(header_background_colour), 'font_colour': final_text_clean(header_font_colour),
                           'font_size': final_text_clean(header_font_size), 'font_family': final_text_clean(header_font_family), 'type':'header'}
        return output
    return output
def get_gauge_font(visual_data, shades):
    return {pp:{'font_family': get_font_family(visual_data, pp), 'font_size': get_font_size(visual_data, pp), 'font_colour': get_font_colour(visual_data, shades, pp)} for pp in ['labels', 'calloutValue']}

def get_font(chart_type, visual_data, shades):
    # high level function that calls sub functions for different chart types
    try:
        if chart_type == 'card':
            title = get_chart_title_font(visual_data, shades)
            data_value = get_data_value_font(visual_data, shades)
            return {"title": title, 'data_value': data_value}
        elif chart_type == 'multiRowCard':
            title = get_chart_title_font(visual_data, shades)
            data_value = get_card_font(visual_data, shades)
            return {"title": title, 'data_value': data_value}
        elif chart_type == 'textbox':
            return get_textbox_font(visual_data, )
        elif chart_type == 'gauge':
            return get_gauge_font(visual_data, shades)
        elif chart_type == 'slicer':
            title = get_slicer_title_font(visual_data, shades)
            mode = visual_data['objects']['data'][0]['properties']['mode']['expr']['Literal']['Value'].lower()
            if mode == "'dropdown'":
                items = get_slicer_items_font(visual_data, shades)
                return {"title": title, 'items': items}
            elif mode == "'between'":
                dates = get_slicer_date_font(visual_data, shades)
                return {"title":title, 'dates': dates}
        elif chart_type == 'actionButton':
            data_labels = get_button_font(visual_data, shades)
            if data_labels:
                return data_labels
        elif chart_type == 'pivotTable':
            text = get_table_font(visual_data, shades)
            if text:
                return text
        else:
            # create a json with font information
            output = {}
            legend = get_legend_font(visual_data, shades)
            title = get_chart_title_font(visual_data, shades)
            data_labels = get_data_value_font(visual_data, shades)
            # if the element is present, put it into json
            if legend:
                output['legend'] = legend
            if data_labels:
                output['data_labels'] = data_labels
            if title:
                output['title'] = title
            # pie and donut charts don't have value/category axes
            if chart_type in ['donutChart', "pieChart"]:
                return output
            else:
                cat_axis = get_axis_font(visual_data, shades, "categoryAxis")
                val_axis = get_axis_font(visual_data, shades, 'valueAxis')
                if val_axis:
                    output['value_axis'] = val_axis
                if cat_axis:
                    output['category_axis'] = cat_axis
                return output
    except: # some blank text boxes don't have fonts, etc.
        print('error get_font')
        print(error_handling())
        return "No fonts detected"
def add_default_fonts(df_):
    q = []
    for font_, chart in zip(df_['fonts'], df_['chart_type']):
        new_font = {}
        # applies to textbox
        if chart == 'textbox':
            if font_ == 'No fonts detected':
                new_font = 'No fonts detected'
            else:
                for k, v in font_.items():
                    new_font[k] = [pbi_defaults.at['Table and matrix values', k] if colour in ['default', 'inherit'] else colour for colour in v]
        elif chart == 'actionButton':
            new_font = {k:pbi_defaults.at['Button text', k] if v == 'default' else v for k,v in font_.items()}
        elif chart == 'multiRowCard':
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'data_value':
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Multi-row card data labels', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'title':
                    for kk, vv in v.items():
                        if vv == 'default':
                            if kk == 'font_colour' or kk == 'font_size':
                                tmp_dict[kk] = pbi_defaults.at['Multi-row card title *', kk]
                            else:
                                tmp_dict[kk] = vv
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
        elif chart == 'card':
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'data_value':
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Card data labels', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'title':
                    for kk, vv in v.items():
                        if vv == 'default':
                            if kk == 'font_colour' or kk == 'font_size':
                                tmp_dict[kk] = pbi_defaults.at['Visual title', kk]
                            else:
                                tmp_dict[kk] = vv
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
        elif chart == 'slicer':
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'items':
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Slicer items', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'dates':
                    for kk, vv in v.items():
                        try:
                            if vv == 'default':
                                tmp_dict[kk] = pbi_defaults.at['Slicer date range labels', kk]
                            else:
                                tmp_dict[kk] = vv
                        except:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'title':
                    if v: # if the title font exists
                        for kk, vv in v.items():
                            try:
                                if vv == 'default':
                                    if kk == 'font_colour' or kk == 'font_size':
                                        if v['type'] == 'title':
                                            tmp_dict[kk] = pbi_defaults.at['Visual title', kk]
                                        else:
                                            tmp_dict[kk] = pbi_defaults.at['Slicer header', kk]
                                    elif kk == 'alignment':
                                        tmp_dict[kk] = 'left'
                                    else:
                                        tmp_dict[kk] = vv
                                else:
                                    tmp_dict[kk] = vv
                            except:
                                tmp_dict[kk] = vv
                    else:
                        new_font[k] = v
                    new_font[k] = tmp_dict
        elif chart == 'gauge':
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'labels':
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Gauge labels', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'calloutValue':
                        for kk, vv in v.items():
                            if vv == 'default':
                                tmp_dict[kk] = pbi_defaults.at['KPI indicators', kk]
                            else:
                                tmp_dict[kk] = vv
                        new_font[k] = tmp_dict
        elif chart == 'pivotTable':
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'grid':
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Table and matrix grid', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'column_header':
                    for kk, vv in v.items():
                        try:
                            if vv == 'default':
                                try:
                                    tmp_dict[kk] = pbi_defaults.at['Table and matrix column headers', kk]
                                except:
                                    tmp_dict[kk] = vv
                            else:
                                tmp_dict[kk] = vv
                        except:
                            print('asfd', k,v,kk,vv, )
                            print(error_handling())
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'row_header':
                    for kk, vv in v.items():
                        try:
                            if vv == 'default':
                                tmp_dict[kk] = pbi_defaults.at['Matrix row headers', kk]
                            else:
                                tmp_dict[kk] = vv
                        except:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                elif k == 'values':
                    if v: # if the title font exists
                        for kk, vv in v.items():
                            try:
                                if vv == 'default':
                                    if kk == 'primary_font_colour' or kk == 'secondary_font_colour':
                                        tmp_dict[kk] = pbi_defaults.at['Table and matrix values', 'font_colour']
                                    elif kk == 'font_size' or kk == 'font_family':
                                        tmp_dict[kk] = pbi_defaults.at['Table and matrix values', kk]
                                    else:
                                        tmp_dict[kk] = vv
                                else:
                                    tmp_dict[kk] = vv
                            except:
                                tmp_dict[kk] = vv
                    else:
                        new_font[k] = v
                    new_font[k] = tmp_dict
        elif chart in ['donutChart', 'pieChart']:
            for k, v in font_.items():
                tmp_dict = {}
                if k == 'title':
                    for kk, vv in v.items():
                        if vv == 'default':
                            if kk == 'font_colour' or kk == 'font_size':
                                tmp_dict[kk] = pbi_defaults.at['Visual title', kk]
                            elif kk == 'alignment':
                                tmp_dict[kk] = 'left'
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
                else:
                    for kk, vv in v.items():
                        if vv == 'default':
                            tmp_dict[kk] = pbi_defaults.at['Slicer items', kk]
                        else:
                            tmp_dict[kk] = vv
                    new_font[k] = tmp_dict
        else:
            for k, v in font_.items(): # parse the font dictionary
                try:
                    # create new dictionary that fills values by replacing 'default' with values from the pbi_default.csv file.
                    tmp_dict = {}
                    if k == 'legend':
                        tmp_dict = {kk: pbi_defaults.at['Legend text', kk] if vv == 'default' else vv for kk, vv in v.items()}
                    elif k == 'data_labels':
                        tmp_dict = {kk: pbi_defaults.at['Data labels', kk] if vv == 'default' else vv for kk, vv in v.items()}
                    elif k == 'title':
                        tmp_dict = {}
                        for kk, vv in v.items():
                            if kk == 'alignment':
                                if vv == 'default':
                                    tmp_dict[kk] = 'center'
                                else:
                                    tmp_dict[kk] = vv
                            else:
                                if vv == 'default':
                                    tmp_dict[kk] = pbi_defaults.at['Visual title', kk]
                                else:
                                    tmp_dict[kk] = vv
                    elif k == 'category_axis': # category and value axis are inner dictionaries, so handling is different.
                        for zz, xx in font_[k].items():
                            if zz == 'title':
                                try:
                                    tmp_dict[zz] = {kk: pbi_defaults.at['Category axis title', kk] if vv == 'default' else vv for kk, vv in v[zz].items()}
                                except:
                                    tmp_dict[zz] = xx
                            elif zz == 'labels':
                                try:
                                    tmp_dict[zz] = {kk: pbi_defaults.at['Category Axis labels', kk] if vv == 'default' else vv for kk, vv in v[zz].items()}
                                except:
                                    tmp_dict[zz] = xx
                    elif k == 'value_axis':
                        for zz, xx in font_[k].items():
                            if zz == 'title':
                                try:
                                    tmp_dict[zz] = {kk: pbi_defaults.at['Value axis title', kk] if vv == 'default' else vv for kk, vv in v[zz].items()}
                                except:
                                    tmp_dict[zz] = xx
                            elif zz == 'labels':
                                try:
                                    tmp_dict[zz] = {kk: pbi_defaults.at['Value axis labels', kk] if vv == 'default' else vv for kk, vv in v[zz].items()}
                                except:
                                    tmp_dict[zz] = xx
                    new_font[k] = tmp_dict
                except:
                    # worst case, just keep whatever the original font is
                    print(df_.to_string())
                    print(k,v)
                    print(error_handling())
                    new_font[k] = v
        q.append(new_font) # add the modified font to a list, which becomes a series in the larger dataframe that's returned
    df_['fonts'] = q
    return df_

# title functions
def get_title(chart_type, visual_data,):
    def inner_title(stuff):
        # special title specific text cleaning
        if '.' in stuff:
            if "(" in stuff:
                strt = stuff.index('(')
                if ")" in stuff:
                    wow = stuff[strt:stuff.index(')')]
                    return wow.split('.')[1]
            return stuff.split(".")[1]
        return stuff
    # find the title of the chart / visual
    try:
        title = visual_data['vcObjects']['title'][0]['properties']['text']['expr']['Literal']['Value']
    except:
        try:
            if chart_type in ["clusteredColumnChart",'pieChart', 'hundredPercentStackedColumnChart', "clusteredBarChart", 'lineChart']:
                # possibly three dims/measures to concatenate, try 3, then 2 and finally 1
                try:
                    title1 = thing(visual_data['projections']['Y'][0]["queryRef"])
                    try:
                        title3 = inner_title(visual_data['projections']['Series'][0]["queryRef"])
                        title2 = inner_title(visual_data['projections']['Category'][0]["queryRef"])
                        title = title1 + ' by ' + title2 + " and " + title3
                    except:
                        title2 = inner_title(visual_data['projections']['Category'][0]["queryRef"])
                        title = title1 + ' by ' + title2
                except:
                    title = visual_data['projections']['Values'][0]["queryRef"].split('.')[1]
            # tables don't have titles
            elif chart_type == 'tableEx' or chart_type == 'pivotTable':
                title = "Not Found or Dynamic"
            else:
                try:
                    if ' ' in visual_data['projections']['Values'][0]["queryRef"]:
                        split = visual_data['projections']['Values'][0]["queryRef"].split(' ')[0]
                        title = split.split('.')[-1]
                    else:
                        title = visual_data['projections']['Values'][0]["queryRef"].split('.')[-1]
                except:
                    try:
                        title = visual_data['projections']['Values'][0]["queryRef"].split('.')[2]
                    except:
                        title = visual_data['projections']['Values'][0]["queryRef"].split('.')[1]
        # worst-case scenario, output not found
        except:
            title = 'Not Found or Dynamic'
    # remove quotations for strings and the trailing ) from nested values
    return final_text_clean(title)
def get_axis_title(visual_data, axis_type = 'valueAxis'):
    """
    For each of valueAxis and categoryAxis, get the axis title text
    :param visual_data:
    :param axis_type:
    :return:
    """
    try:
        tmp = final_text_clean(visual_data['objects'][axis_type][0]['properties']['titleText']['expr']['Literal']['Value'])
        if tmp == '': # if the title is '', we'll revert to Not Found (this happens when some parts of the title properties are set, but not the actual string)
            return "Not Found"
        else:
            return tmp
    except:
        return 'Not Found'

# colour functions
def get_contrast_ratio(c1, c2):
    """
    This function compares two colours' contrast and outputs a value between 21 (perfect contrast) and 1 (no contrast).
    :param c1: lighter colour
    :param c2: darker colour
    :return: the contrast ratio between the two colours.
    """
    colour1 = Color(c1)
    colour2 = Color(c2)
    return (get_luminance(colour1) + 0.05)/(get_luminance(colour2) + 0.05)
def get_luminance(colour_):
    """
    This function returns a luminance value for the specified colour.
    :param colour: a representation of colour, either as hex or rgb tuple/list
    :return: a luminance value for the colour
    """
    try:
        colour = Color(colour_)
    except:
        colour = Color(rgb=colour_)
    r = colour.get_red()
    b = colour.get_blue()
    g = colour.get_green()
    rgb_dict = {'r':r, 'b':b, 'g':g}
    for key, each in rgb_dict.items():
        if each < 0.03928:
            rgb_dict[key] = each / 12.92
        else:
            rgb_dict[key] = ((each + 0.055)/1.055)**2.4
    return (0.2126 * rgb_dict['r']) + (0.0722*rgb_dict['b']) + (0.7152*rgb_dict['g'])
def check_contrast(df_):
    aoda_fonts = []
    for i in df_.itertuples():
        chart_type = i.chart_type
        background = i.background_colour
        font = i.fonts
        theme = i.base_theme
        try: # get a background colour if it's in that font, else use the default one
            if 'background_colour' not in font.keys():
                bkgrd = background
            else:
                bkgrd = font['background_colour']
            # textbox can have multiple fonts / colours, others can't
            if chart_type == 'textbox':
                p = [get_contrast_ratio(bkgrd, font['font_colour'][i]) for i in range(len(font["font_colour"]))]
                aoda_fonts.append({chart_type:p})
            elif chart_type == 'actionButton':
                p = get_contrast_ratio(bkgrd, font['font_colour'])
                aoda_fonts.append({chart_type:p})
            elif chart_type == 'slicer':
                haha = {}
                for i in font.keys():
                    try:
                        if 'background_colour' in font[i].keys():
                            haha[i] = get_contrast_ratio(font[i]['background_colour'], font[i]['font_colour'])
                        else:
                            haha[i] = get_contrast_ratio(bkgrd, font[i]['font_colour'])
                    except:
                        try:
                            haha[i] = get_contrast_ratio(bkgrd, font[i]['font_colour'])
                        except:
                            haha[i] = np.nan
                aoda_fonts.append(haha)
            elif chart_type == 'pivotTable':
                haha = {}
                for font_key in font.keys():
                    if font_key == 'values':
                        try:
                            haha[font_key] = {}
                            if 'secondary_background_colour' in font[font_key].keys():
                                if font[font_key]['primary_font_colour'] != font[font_key]['secondary_font_colour']:
                                    haha[font_key]['secondary_background_colour'+' <> '+'secondary_font_colour'] = (get_contrast_ratio(font[font_key]['secondary_background_colour'], font[font_key]['secondary_font_colour']))
                                else:
                                    haha[font_key]['secondary_background_colour'+' <> '+'primary_font_colour'] = (get_contrast_ratio(font[font_key]['secondary_background_colour'], font[font_key]['primary_font_colour']))
                            if 'primary_background_colour' in font[font_key].keys():
                                if font[font_key]['primary_font_colour'] != font[font_key]['secondary_font_colour']:
                                    haha[font_key]['primary_background_colour'+' <> '+'secondary_font_colour']=(get_contrast_ratio(font[font_key]['primary_background_colour'], font[font_key]['secondary_font_colour']))
                                else:
                                    haha[font_key]['primary_background_colour'+' <> '+'primary_font_colour']=(get_contrast_ratio(font[font_key]['primary_background_colour'], font[font_key]['primary_font_colour']))
                        except:
                            print('fails values', font)
                            print(error_handling())
                            haha[font_key] = np.nan
                    else:
                        pass
                for font_key in font.keys():
                    if font_key == 'values':
                        pass
                    elif font_key in ['column_header', 'row_header']:
                        try:
                            if font[font_key]['background_colour'] == 'default':
                                haha[font_key] = haha['values']
                            else:
                                haha[font_key] = get_contrast_ratio(font[font_key]['background_colour'], font[font_key]['font_colour'])
                        except:
                            print('fails column_header thing')
                            print(error_handling())
                            haha[font_key] = np.nan
                    else:
                        haha[font_key] = np.nan
                aoda_fonts.append(haha)
            else: # all other chart types
                haha = {}
                for x in font.keys():
                    if x not in ['category_axis', 'value_axis']:
                        if i.data_label_background_colour: # if the data label background is selected by user
                            haha[x] = get_contrast_ratio(i.data_label_background_colour, font[x]['font_colour'])
                        else:
                            haha[x] = get_contrast_ratio(bkgrd, font[x]['font_colour'])
                    else: # category and value axis, they don't have data label background options
                        inner_dict = {}
                        for category in ['title', 'labels']:
                            try:
                                inner_dict[category] = get_contrast_ratio(bkgrd, font[x][category]['font_colour'])
                            except:
                                inner_dict[category] = np.nan
                        haha[x] = inner_dict
                aoda_fonts.append(haha)
        except:
            print('fails check_contrast', chart_type, font, background, )
            print(error_handling())
            aoda_fonts.append({'nada':np.nan})
    df_['font_colour_contrast'] = aoda_fonts
    return df_
def get_background(visual_data, shades, theme):
    try: # colour is set by user and is 'custom colour'
        back_colour = visual_data['vcObjects']['background'][0]['properties']['color']['solid']['color']['expr']['Literal']['Value']
    except:
        try: # colour is set by user and is a derivative of the theme colours
            col = visual_data['vcObjects']['background'][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['ColorId']
            opacity = visual_data['vcObjects']['background'][0]['properties']['color']['solid']['color']['expr']['ThemeDataColor']['Percent']
            back_colour = get_colour_from_theme(col, opacity, shades)
        except:
            try: # using the theme's background
                back_colour = theme['background']
            except: # Theme's background isn't set, default is white or #ffffff
                back_colour = '#ffffff'
    return final_text_clean(back_colour.upper())
def get_colour_from_theme(color, opa, shades):
    # read shades data and output the proper hex colour that matches the shade / theme colour
    tmp= shades[(shades['theme_colorID']==color)&(shades['shade']==opa)].copy().reset_index(drop=True)
    return tmp.at[0, 'hex']
def make_rgb_transparent(rgb, bg_rgb, alpha):
    """
    This function computes the new colour of things, relative to the background and the alpha applied.

    :param rgb: RGB of the text (or other object, like data_value background)
    :param bg_rgb: RGB of the background
    :param alpha: Desired luminance
    :return: RGB of the resultant text or other object, relative to the alpha and background
    """
    return [alpha * c1 + (1 - alpha) * c2
            for (c1, c2) in zip(rgb, bg_rgb)]
def get_data_label_background(overall_bkg, visual_data, shades):
    try:
        tt = visual_data['objects']['labels'][0]['properties']
        if tt['enableBackground']['expr']['Literal']['Value'].lower() == 'true':
            try:
                alpha = int(''.join([i for i in tt['backgroundTransparency']['expr']['Literal']['Value'] if i.isnumeric()])) / 100
            except:
                alpha = 0.9
            try:  # colour is set by user and is 'custom colour'
                back_colour = tt['backgroundColor']['solid']['color']['expr']['Literal']['Value']
            except:
                try:  # colour is set by user and is a derivative of the theme colours
                    col = tt['backgroundColor']['solid']['color']['expr']['ThemeDataColor']['ColorId']
                    opacity = tt['backgroundColor']['solid']['color']['expr']['ThemeDataColor']['Percent']
                    back_colour = get_colour_from_theme(col, opacity, shades)
                except:
                    try:  # using the theme's background
                        back_colour = theme['background']
                    except:  # Theme's background isn't set, default is white or #ffffff
                        back_colour = '#ffffff'
            print('hhh', Color(overall_bkg), Color(final_text_clean(back_colour)))
            return Color(rgb=make_rgb_transparent(Color(overall_bkg).rgb, Color(final_text_clean(back_colour)).rgb, alpha)).get_hex()
        else:
            return
    except:
        print('dumb', error_handling())
        return
# create / run report functions
def run(input_list, email_address=None, ):
    # make the xlsx and csv files
    upload_ID = make_report(input_list, email_address)
    # create README.txt and zip files together
    create_readme()
    with zipfile.ZipFile("output.zip", 'w') as zipf:
        zipf.write("output.csv")
        zipf.write("output.xlsx")
        zipf.write("README.txt")
        [zipf.write(x) for x in [report + ".html" for report in make_dashboards()]]
    logging.info(f"The zip file for upload {upload_ID} has been created.")
    if email_address:
        email_output="""<h2>Thank you!</h2>
                   <p>Hello,<br>
                   This is the output from the dashboard documentation request. The zip file contains two output files (one XLSX file and one CSV file), as well as a readme text file.<br> 
                   Please read the <b>README</b> thoroughly.<br>
                    If there are any questions / comments / concerns, please contact the HHBI team.</p>"""
        # send email
        # send_email(email_address, 'This is the output from the dashboard documentation request.',email_output)
def make_report(input_list, email):
    """
    Parse reports, create a summary based off of those reports, and then create an excel file with all of the data.

    :param input_list: list of reports to parse
    :return: N/A
    """
    current_time = datetime.datetime.now()
    parsed_reports = {str(report).replace(".pbix", ""): parse_data_from_report(report) for report in input_list}
    df = pd.concat(parsed_reports.values())
    print(df.to_string())
    logging.info(f"All {len(parsed_reports.values())} report(s) for {email}'s upload are parsed.")
    summary_table = df.groupby('report_name').agg({'page_number': 'max', "chart_type": list, "dims_measures": list, 'base_theme': 'max', 'pass_aoda':list})
    summary_table["pages"] = summary_table["page_number"] + 1
    summary_table['chart_types'] = [dict(Counter(i)) for i in summary_table['chart_type']]
    for x in summary_table['pass_aoda']:
        p = list(set(x))
        pass_fail = 'Pass'
        if 'Fail' in p:
            pass_fail = 'Fail'
    summary_table['aoda_compliance'] = pass_fail
    dims_measures = []
    for row in summary_table['dims_measures']:
        # flatten list and count the items
        tmp = dict(Counter([t for item in row for t in item.split(' / ')]))
        try:
            del tmp['Not Found']
        except:
            pass
        dims_measures.append(tmp)
    summary_table['dimensions_and_measures'] = dims_measures
    summary_table = summary_table.drop(columns=["chart_type", 'dims_measures', "page_number", 'pass_aoda']).reset_index()
    # downcast to least expensive number or convert to string (so it can be written into SQL DB)
    for table in [summary_table, df]:
        for col in table.columns:
            try:
                table[col] = pd.to_numeric(table[col], downcast="integer")
            except:
                table[col] = table[col].astype(str)

    # upload to MongoDB and get Upload_ID
    result = pbi_mongo_uploads.insert_one({"dashboards":df['dashboard_id'].unique().tolist(), 'email':email, 'upload_datetime':current_time})
    upload_id = str(result.inserted_id)
    logging.info(f"The dashboards were uploaded to the MongoDB Upload database with Upload_Id: {upload_id}")
    summary_table['upload_id'] = upload_id
    df['upload_id'] = upload_id
    # write to SQL
    summary_table.to_sql(f'summary_{str(current_time.month)}_{str(current_time.year)}', engine, if_exists='append', index=False)
    df.to_sql(f'output_{str(current_time.month)}_{str(current_time.year)}', engine, if_exists='append', index=False)
    # write to XLSX/CSV
    try:
        with pd.ExcelWriter('output.xlsx') as writer:
            summary_table.to_excel(writer, sheet_name='dashboard_summary', index=False)
            df.to_excel(writer, sheet_name='full_output', index=False)
            for k, v in parsed_reports.items():
                v.to_excel(writer, sheet_name=k[:30], index=False)
        df.to_csv('output.csv', index=False)
        logging.info(f"Upload {upload_id} has been written to the SQL databases.")
    except:
        logging.info(f'Upload {upload_id} could not be written to the SQL databases.')
        logging.info(error_handling())
        logging.info(f"{k} | {v}")
    return upload_id

def send_email(to, TEXT, HTML, ):
    """
    This function sends emails to the email list depending on the para
    :param TEXT: text to send in an email
    :param HTML: text to send in an email, but in HTML (default)
    :param week_start: integer that indicates if this is the email sent weekly (start of the week, monday at 7am)
    :param error_email: if this is an error email, send an alert with a different message
    :return:
    """
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    # current date, and a date 5 days away
    curtime = datetime.datetime.now().date()
    SUBJECT = 'Dashboard Documentation Results'
    TO = [to]

    # Gmail Sign In
    gmail_sender = 'julienwork789@gmail.com'  # senders email
    gmail_passwd = '12fork34'  # senders password

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    # add the 2 parts of the email (one plain text, one html)
    part1 = MIMEText(TEXT, 'plain')
    part2 = MIMEText(HTML, 'html')
    # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part1)
    msg.attach(part2)

    # add attachment to email
    file = 'output.zip'
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(file, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    msg.attach(attachment)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # connect to the GMAIL server
    server.login(gmail_sender, gmail_passwd) # login to the GMAIL server
    try:
        # send email and confirm email is sent / time it is sent
        server.sendmail(gmail_sender, TO, msg.as_string())
        logging.info(str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")) + f' email was sent to {str(TO)}.')
    except Exception as e:
        # print error if not sent, and confirm it wasn't sent
        logging.info(str(e))
        logging.info(error_handling())
        logging.info(str(curtime) + ' error sending mail')
def create_readme():
    """
    Create a text file with the README information.
    :return: N/A
    """
    with open('README.txt', 'w') as file:
        file.write("README\r")
        file.write("This is the boring readme file that no one reads.")
        file.write('The CSV file (output.csv) is the "full_output" sheet in the XLSX file (output.xlsx)')
        file.write('The XLSX file contains a page with the full output, a summary page and a page with the parsed information for each of the dashboards uploaded.')
        file.write('- HHBI Team')

# main functions
def get_data(visual, theme, shades):
    # location on page
    width = visual['width']
    height = visual['height']
    x_pos = visual['x']
    y_pos = visual['y']
    # visual type and the underlying data are the most important
    visual_data = json.loads(visual['config'])['singleVisual']
    chart_type = visual_data['visualType']
    # sometimes tab order isn't assigned by Power BI
    try:
        tab_order = visual['tabOrder']
    except:
        tab_order = 'Not Found'
    # alt text only appears if author inputs it.
    try:
        alt_text = visual_data['vcObjects']['general'][0]['properties']['altText']['expr']['Literal']['Value']
    except:
        alt_text = 'Not Found'
    # filters only appear when they are applied
    try:
        variable = dict(json.loads(visual['filters'])[0])['filter']["Where"][0]['Condition']['In']['Expressions'][0]['Column']['Property']
        filters_applied = dict(json.loads(visual['filters'])[0])['filter']["Where"][0]['Condition']['In']['Values']
        filters = {variable: [ii[0]['Literal']['Value'].replace("'", "") for ii in filters_applied]}
    except:
        filters = "No filters on visual or none applied"
    # find the measures / dimensions used, get a distinct list of them
    # some visuals like *textbox* don't have measures
    try:
        tmp = visual_data['projections']
        array = [it['queryRef'] for each in tmp.keys() for it in tmp[each]]
        new_array = []
        for each in array:
            try:
                answer = re.match(r"\w{2,12}(\((.+)\))", each)
                new_array.append(answer.group(2))
            except:
                new_array.append(each)
        measures = ' / '.join(list(set(new_array)))
    except:
        measures = 'Not Found'
    background = get_background(visual_data, shades, theme, )
    title = get_title(chart_type, visual_data)
    fonts = get_font(chart_type,visual_data, shades)
    value_axis_text = get_axis_title(visual_data, 'valueAxis')
    cat_axis_text = get_axis_title(visual_data, 'categoryAxis')
    data_label_background_colour = get_data_label_background(background, visual_data, shades)
    if chart_type == 'slicer':
        print(title)
        print(alt_text, chart_type, background)
        try:
            pprint(json.loads(visual['config']))
        except:
            pass
        print()
        print()
    return {'data_label_background_colour':data_label_background_colour, 'category_axis_title':cat_axis_text,'value_axis_title':value_axis_text, 'fonts':fonts, 'chart_type':chart_type,'title': title, 'tab_order': tab_order, "width": width, "height": height, "x_position": x_pos, "y_position": y_pos,'background_colour':background, "alt_text": alt_text, 'dims_measures':measures, 'filters':filters,}
def parse_data_from_report(report):
    try:
        pbix_file = report_path + report
        zip_file = pbix_file.replace('.pbix', ".zip")
        new_dir_name = rf'{pbix_file.replace(".pbix", "/")}'

        shutil.copy(pbix_file, zip_file) # copy pbix file as a zip file
        os.mkdir(new_dir_name) # make directory and extract zip to that directory
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(new_dir_name)
        # get the theme of the dashboard
        try:
            theme_file = [i for i in os.listdir(new_dir_name + '/Report/StaticResources/SharedResources/BaseThemes/') if i.endswith('.json')][0]
            # find the csv of the theme's colours and find the theme for analysis
            theme = json.loads(open(new_dir_name + f'/Report/StaticResources/SharedResources/BaseThemes/{theme_file}', 'r', ).read())
        except:
            theme_file = "CY18SU07.json"
            theme = {}
        shades = pd.read_csv(f'{theme_file.replace(".json", "")}_shades.csv')
        json_file = json.loads(open(new_dir_name + '/Report/Layout', 'r',).read().replace("\x00", ""))
        mongo_output = pbi_mongo_dashboards.insert_one(json_file)
        dashboard_id = str(mongo_output.inserted_id)
        logging.info(f"""Dashboard "{report}" has been uploaded to MongoDB Dashboard database with dashboard_id: {dashboard_id}""")
        dfs = []
        for num, val in enumerate(json_file['sections']):
            df = pd.DataFrame([get_data(visual, theme, shades) for visual in val['visualContainers']])
            df['page_name'] = val['displayName'] # page name
            df['page_number'] = num # page number in report
            try: # sort each page by tab order, sometimes tab order doesn't appear
                df.sort_values('tab_order', ascending=False, inplace=True)
            except:
                pass
            dfs.append(df)
        final = pd.concat(dfs)
        final['report_name'] = report.replace(".pbix", "")
        final['base_theme'] = theme_file.replace(".json","")

        final = add_default_fonts(final)

        final = check_contrast(final)

        final = fails_aoda_because(final)
        final['dashboard_id'] = dashboard_id

        os.remove(zip_file) # destroy zip file
        shutil.rmtree(new_dir_name) # destroy folder from zip file
        return final.reset_index(drop=True)
    except:
        print(error_handling())
        os.remove(zip_file) # destroy zip file
        shutil.rmtree(new_dir_name) # destroy folder from zip file
def fails_aoda_because(df_, ratio = 4.5):
    reasons = []
    pass_fail = []
    for i in df_.itertuples():
        fails_aoda = {}
        try: # if tab order isn't an integer, it isn't set
            _ = int(i.tab_order)
        except:
            fails_aoda['tab_order'] = 'Not set'
        if i.alt_text == 'Not Found': # if alt_text is 'not found', it fails AODA
            fails_aoda['alt_text'] = 'Not set'
        if i.chart_type not in ['textbox', 'actionButton']: # all visuals but a textbox needs a title for AODA
            if i.title == 'Not Found or Dynamic':
                fails_aoda['title'] = 'Not set'
        # check the fonts element of the visual
        for k, v in i.font_colour_contrast.items():
            if isinstance(v, dict): # category axis or value axis
                fails_aoda[k] = {}
                for x, y in v.items():
                    if y < ratio:
                        fails_aoda[k][x] = f'Text contrast ratio is below {ratio}:1'
            elif isinstance(v, list): # textbox
                print(i, k, v)
                for y in v:
                    num = min([int(''.join([z for z in w if z.isnumeric()])) for w in i.fonts['font_size']])
                    if num < 18:
                        if y < ratio:
                            fails_aoda[k] = f'Text contrast ratio is below {ratio}:1'
                    else:
                        if y < 3:
                            fails_aoda[k] = f'Text contrast ratio is below 3:1'
            else: # all other visuals
                if v == 1: # text might be white,
                    if k == 'data_labels':
                        pass
                try:
                    try:
                        num = int(''.join([z for z in i.fonts[k]['font_size'] if z.isnumeric()]))
                    except:
                        num = int(''.join([z for z in i.fonts['font_size'] if z.isnumeric()]))
                    if num < 18: # if not large text
                        if 1 < v < ratio:
                            fails_aoda[k] = f'Text contrast ratio is below {ratio}:1'
                    else: # if large text
                        if 1 < v < 3:
                            fails_aoda[k] = f'Text contrast ratio is below 3:1'
                except:
                    if 1 < v < ratio:
                        fails_aoda[k] = f'Text contrast ratio is below {ratio}:1'

        # for title and textbox visuals, make sure text is over 12pt font.
        try:
            if i.chart_type in ['textbox', 'title']:
                for xx in i.fonts['font_size']:
                    test = int(''.join([z for z in xx if z.isnumeric()]))
                    if test < 12:
                        pprint(fails_aoda)
                        try:
                            if fails_aoda[i.chart_type]:
                                fails_aoda[i.chart_type] += ' | Text size is below 12pt'
                        except:
                                fails_aoda[i.chart_type] = f'Text size is below 12pt'
        except:
            print(error_handling())
            pass
        # check if key-value pair is empty, only return elements that have data and that fail AODA
        for each in [k for k, v in fails_aoda.items() if not v]:
            del fails_aoda[each]
        reasons.append(fails_aoda)
        if fails_aoda:
            pass_fail.append('Fail')
        else:
            pass_fail.append('Pass')
    df_['reason_aoda'] = reasons
    df_['pass_aoda'] = pass_fail
    return df_



# website with default info
# https://docs.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#:~:text=Select%20File%20%3E%20Options%20and%20settings,preview%20feature%20to%20be%20enabled
pbi_defaults = pd.read_csv('pbi_defaults.csv').set_index("visual_objects")
email = 'jragbeer@github.com'
# pbix_files_in_directory = [p for p in os.listdir(report_path) if p == 'tabular_rs03_mod.pbix']
# pbix_files_in_directory = [p for p in os.listdir(report_path) if p == 'tabular_rs05_mod.pbix']
pbix_files_in_directory = [p for p in os.listdir(report_path) if p == 'MMAH_Report_Server_Usage_Statistics.pbix']
# pbix_files_in_directory = [p for p in os.listdir(report_path) if p == 'RS05_MMAH_SMA_Income_Households_Population.pbix']
# pbix_files_in_directory = [p for p in os.listdir(report_path) if p.endswith('.pbix')]
# pbix_files_in_directory = [p for p in os.listdir(report_path) if p in ['tabular_rs05_mod.pbix', 'tabular_rs03_mod.pbix']]
run(pbix_files_in_directory, email)

