import colorsys
import datetime
import json
import logging
import os
import shutil
import traceback
from pprint import pprint
import numpy as np
import pandas as pd

def make_dashboards(file_name= "output.xlsx"):
    """

    This function creates interactive plots for every chart in every report represented by the *file_name*. Each chart is colour-coded (green or red, representing pass/fail).
    Each report contains tabs that represent each page. Each chart has a tooltip that explains what causes that chart to fail AODA. The tooltip is shown when hovering over the chart with a mouse.

    This function creates an HTML file that shows all of the information. The HTML file is named the same as the sheet name inside the input XLSX file.

    :param file_name: the input file that contains all of the dashboard information
    :return: a list of each report in the input file
    """
    from bokeh.events import ButtonClick, SelectionGeometry
    from bokeh.io import curdoc
    from bokeh.layouts import widgetbox, row, column, gridplot, layout
    from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, Label, Button, DatePicker, CustomJS, Panel, RangeSlider
    from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FactorRange, BoxAnnotation, Tabs
    from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
    from bokeh.plotting import figure, show, output_file
    from colour import Color


    path = os.getcwd().replace('\\', "/") + "/"
    xl_file = pd.ExcelFile(path + file_name)

    def make_fail_tooltip(rdf_):
        """
        This function creates a column in the input dataframe and returns that dataframe. When an item such as a *textbox* contains multiple AODA
        violations, this function creates the tooltip that is formatted correctly.

        :param rdf_: dataframe associated with with Power BI visuals that fail AODA
        :return: a dataframe with a new column. The new column represents the HTML tooltip
        """
        array = []
        for i in rdf_["reason_aoda"]:
            result = json.loads(i.replace("'", '"'))
            html_string = '<ul>' # outer list for HTML
            for k, v in result.items():
                tmp = k.replace("_", " ").split()
                fun = ' '.join([x.capitalize() for x in tmp])
                if isinstance(v, dict):
                    inner_string = "<ul>" # inner list for HTML
                    for kk, vv in v.items():
                        if ' <> ' in kk:
                            inner_string += f"<li>{' <> '.join([c.replace('_', ' ').capitalize() for c in kk.split(' <> ')])}: {vv}</li>" # break up words and capitalize
                        else:
                            inner_string += f"<li>{kk.replace('_', ' ').capitalize()}: {vv}</li>" # break up words and capitalize
                    inner_string += "</ul>"
                    html_string += f"""<li>{fun}: {inner_string}</li>"""
                else:
                    if " | " in v:
                        # if multiple infractions for the type of text, split and put each as a new list item in the HTML
                        ttt = v.split(' | ')
                        for each in ttt:
                            inner_string = "<ul>"  # inner list for HTML
                            inner_string += f"<li>{each.replace('_', ' ').capitalize()}</li>"  # break up words and capitalize
                            inner_string += "</ul>"
                        html_string += f"""<li>{fun}: {inner_string}</li>"""
                    else:
                        html_string += f"""<li>{fun}: {v}</li>"""
            html_string += '</ul>'
            array.append(html_string)
        rdf_['new'] = array
        return rdf_

    tabs = {}
    dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names if sheet_name not in ['full_output', 'dashboard_summary']}
    for report_name in dfs.keys():
        tdf = dfs[report_name]
        charts = {}
        for pg in tdf['page_name']:
            df = tdf[tdf['page_name'] == pg][["reason_aoda", "pass_aoda",'title','chart_type', 'width', 'height', 'x_position', 'y_position', ]].copy()
            df['left'] = df['x_position']
            df['right'] = df['x_position'] + df['width']
            df['top']= -1*(df['y_position'] + df['height'])
            df['bottom'] = -1*df['y_position'] # y_position in Power BI is 0 at the top, versus 0 at the bottom for this charting app
            df['colour'] = np.where(df['pass_aoda'] == 'Pass','#2f7531', '#7a0a0a') # colours of the glyphs (pass == green, fail == red)

            rdf = df[df['pass_aoda'] == 'Fail'].copy()
            gdf = df[df['pass_aoda'] == 'Pass'].copy()
            rdf = make_fail_tooltip(rdf)

            green_source = ColumnDataSource({'colour':gdf['colour'],'chart_type':gdf['chart_type'], 'pass_aoda':gdf['pass_aoda'], 'top':gdf["top"],'bottom':gdf['bottom'], 'right':gdf['right'], 'left':gdf['left']})
            red_source = ColumnDataSource({'reasons':rdf['new'], 'colour':rdf['colour'],'chart_type':rdf['chart_type'],'pass_aoda':rdf['pass_aoda'],'top':rdf["top"],'bottom':rdf['bottom'], 'right':rdf['right'], 'left':rdf['left']})
            # plot + glyphs
            p = figure(plot_width=1200, plot_height=700, x_axis_label=None, x_axis_type=None, y_axis_label=None, y_axis_type=None, toolbar_location = None,)
            p.quad(top='top', bottom='bottom', left='left', right='right', source = red_source, color="firebrick", alpha= 0.3, name = 'red')
            p.quad(top='top', bottom='bottom', left='left', right='right', source = green_source, color="forestgreen", alpha = 0.3, name = 'green')
            # hovertools
            green_TOOLTIPS = """
                <div>
                    <div>
                        <span style="font-size: 13px; font-weight: bold;">Chart Type: @chart_type</span>
                    </div>
                    <div>
                        <span style="font-size: 20px; font-weight: bold; color: @colour{safe};">@pass_aoda{safe}</span>
                    </div>
                </div>
            """
            red_TOOLTIPS = """
                <div>
                    <div>
                        <span style="font-size: 13px; font-weight: bold;">Chart Type: @chart_type</span>
                    </div>
                    <div>
                        <span style="font-size: 20px; font-weight: bold; color: @colour{safe};">@pass_aoda{safe}</span>
                    </div>
                    <div>
                        <span style="font-size: 13px; font-weight: bold;">Reasons:</span>
                        <span style="font-size: 12px; font-weight: bold;">@reasons{safe}</span>
                    </div>
    
                </div>
            """
            p.add_tools(HoverTool(tooltips=green_TOOLTIPS, names=['green']))
            p.add_tools(HoverTool(tooltips=red_TOOLTIPS, names=['red']))
            # plot attributes
            p.outline_line_width = 4
            p.outline_line_alpha = 0.3
            p.outline_line_color = "black"
            p.axis.axis_line_color = None
            p.grid.grid_line_color = None
            charts[pg] = p

        output_file(f'{report_name}.html')
        pages = {each: Panel(child=row([charts[each]]), title=f"{each}") for each in charts.keys()}
        tabs[report_name] = Tabs(tabs=list(pages.values()))
        # output
        show(tabs[report_name])
    return list(dfs.keys()) #return a list of all report names


