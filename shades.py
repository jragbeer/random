import cv2
from colour import Color
import os
import pandas as pd

path = os.getcwd().replace("\\", "/") + '/'
# Power BI theme (name can be parsed from ..Report\StaticResources\SharedResources\BaseThemes\)
theme = "CY18SU07"
img = cv2.imread(path + f'themes/{theme}.png', cv2.IMREAD_UNCHANGED) #picture of all of the default colours and shades for the theme
# {shade: pixel} k:v pairs where 0 is the standard colour (top row)
heights = {'0':10, '0.6':30, '0.4':50, '0.2':70, '-0.25':85, '-0.5':100}
# pixel location of each column of colours
widths = [10, 30, 50, 70, 94, 114, 135, 160, 180, 200]
data = []
for shade, h in heights.items():
    for colour_category, w in enumerate(widths):
        tmp = img[h,w]
        r = tmp[2]
        g = tmp[0]
        b = tmp[1]
        color = Color(rgb=(r/255, b/255, g/255))
        data.append({'theme_colorID':colour_category, 'shade':shade,'rgb':(r,g,b), 'rgb_scaled':(r/255,g/255,b/255),'hex':color.get_hex()})
df = pd.DataFrame(data)
def fix_white(df):
    df['shade'] = pd.to_numeric(df['shade'])
    for p in df.itertuples():
        if p.theme_colorID == 0:
            if p.shade == 0.6:
                df.at[p.Index,'shade'] = -0.1
            elif p.shade == 0.4:
                df.at[p.Index, 'shade'] = -0.2
            elif p.shade == 0.2:
                df.at[p.Index, 'shade'] = -0.3
            elif p.shade == -0.25:
                df.at[p.Index, 'shade'] = -0.5
            elif p.shade == -0.5:
                df.at[p.Index, 'shade'] = -0.6
    return df
def fix_black(df):
    for p in df.itertuples():
        if p.theme_colorID == 1:
            if p.shade == -0.25:
                df.at[p.Index, 'shade'] = -0.1
            elif p.shade == -0.5:
                df.at[p.Index, 'shade'] = 0
    return df
df = fix_white(df)
df = fix_black(df)
df.to_csv(f"{theme}_shades.csv", index=False)
