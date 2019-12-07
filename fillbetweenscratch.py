import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import bokeh
from collections import Counter
from pprint import pprint
a = np.random.randint(1,500)
np.random.seed(a)
print('seed',a)
def main(p, X, y, below_colour, above_colour, ymean=None):
    y = np.array(y)
    X = np.array(X)
    if not ymean:
        ymean = y.mean()
    print('y', y)
    print('split line', ymean)
    diffs = y - ymean
    change_points = []
    for i in range(len(y)):
        try:
            if np.sign(ymean - y[i]) != np.sign(ymean - y[i + 1]):
                change_points.append((i, i + 1))
        except IndexError:
            pass
    def make_glyph_coords(x_in, y_in, split, change_points, diffs, idx, last_x=None,):
        """

        This function checks whether it is the first, last or neither. Then calculates the next angle to draw.

        :param x_in: x points of input
        :param y_in: y points of input
        :param change_points: a list of tuples containing where the change points are
        :param diffs: list of differences between y point and mean for each x point
        :param idx: index of change point in list, starts at 0
        :param last_x: last x point to be calculate
        :param adjacent: distance between x points, assuming 1 now
        :return: the ouput of an inner function
        """

        def first_glpyh(x_in, y_in, split, change_points, diffs, idx, theta):
            triangle_adjacent_1 = np.around(
                x_in[change_points[0][1]] - (np.abs(diffs[change_points[0][1]]) / np.tan(theta)), 3)
            triangle_adjacent_2 = np.around(
                x_in[change_points[0][0]] + (np.abs(diffs[change_points[0][0]]) / np.tan(theta)), 3)
            avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2


            x_array = [x_in.min(), x_in.min(), ]
            y_array = [split, y_in[idx], ]

            # COMMENT OUT/IN TO CHANGE ORDER OF VERTICES
            x_array = [avg, x_in.min(), x_in.min()]
            y_array = [split,split, y_in[idx], ]

            # if glyph is above live and diff is positive
            if diffs[0] > 0:
                above_below = 'above'
                for i, k in enumerate(diffs):
                    if i == 0:
                        continue
                    if k > 0:
                        x_array.append(x_in[i])
                        y_array.append(y_in[i])
                    elif k < 0:
                        break
            # if the glyph will be below line and diff is negative
            elif diffs[0] < 0:
                above_below = 'below'
                for i, k in enumerate(diffs):
                    if i == 0:
                        continue
                    if k < 0:
                        x_array.append(x_in[i])
                        y_array.append(y_in[i])
                    elif k > 0:
                        break
            # COMMENT IN/OUT TO CHANGE ORDER OF VERTICES
            # x_array.append(avg)
            # y_array.append(split)

            # COMMENT IN/OUT TO CLOSE SHAPE
            # x_array.append(x_array[0])
            # y_array.append(y_array[0])
            return x_array, y_array, avg, above_below

        def last_glpyh(x_in, y_in, split, diffs, idx, last_x):

            x_array = [last_x, x_in[idx], x_in[idx], ]
            y_array = [split, split, y_in[idx], ]

            if diffs[-1] > 0:
                for u in range(len(y_in) - 2, 0, -1):
                    if diffs[u] > 0:
                        x_array.append(x_in[u])
                        y_array.append(y_in[u])
                    else:
                        break
                above_below = 'above'
            else:
                for u in range(len(y_in) - 1, 0, -1):
                    if diffs[u] < 0:
                        x_array.append(x_in[u])
                        y_array.append(y_in[u])
                    else:
                        break
                above_below = 'below'
            return x_array, y_array, None, above_below

        def middle_glyph(x_in, y_in, split, change_points, diffs, idx, theta):
            if diffs[change_points[idx][0]] > 0:
                triangle_adjacent_1 = np.around(
                    x_in[change_points[idx][0]] + (np.abs(diffs[change_points[idx][0]]) / np.tan(theta)), 3)
                if diffs[change_points[idx][1]] > 0:
                    triangle_adjacent_2 = np.around(
                        x_in[change_points[idx][1]] - (np.abs(diffs[change_points[idx][1]]) / np.tan(theta)), 3)
                else:
                    triangle_adjacent_2 = triangle_adjacent_1
                avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
                above_below = 'above'
            else:
                triangle_adjacent_1 = np.around(
                    x_in[change_points[idx][0]] + (np.abs(diffs[change_points[idx][0]]) / np.tan(theta)), 3)
                triangle_adjacent_2 = np.around(
                    x_in[change_points[idx][1]] - (np.abs(diffs[change_points[idx][1]]) / np.tan(theta)), 3)
                avg = (triangle_adjacent_1 + triangle_adjacent_2) / 2
                above_below = 'below'

            x_array = [last_x] + [x_in[x] for x in range(change_points[idx - 1][1], change_points[idx][0] + 1)] + [avg]
            y_array = [split] + [x for x in y_in[change_points[idx - 1][1]:change_points[idx][0] + 1]] + [split]
            return x_array, y_array, avg, above_below

        # check if this is the last glyph to be drawn
        if idx == len(change_points):
            idx = -1
        # calculate dimensions of triangle and angle
        height = np.around(np.abs(diffs[change_points[idx][0]]) + np.abs(diffs[change_points[idx][1]]), 3)
        adjacent = np.abs(x_in[change_points[idx][1]])-np.abs(x_in[change_points[idx][0]])
        hypotenuse = np.sqrt(adjacent**2 + height ** 2)
        theta = np.around(np.arctan(np.abs(height / adjacent)), 8)
        # if the first glyph to be drawn
        if idx == 0:
            return first_glpyh(x_in, y_in, split, change_points, diffs, idx, theta)
        # if the last glyph to be drawn
        elif idx == -1:
            return last_glpyh(x_in, y_in, split, diffs, idx, last_x)
        # if a glyph in the middle of the endpoints
        else:
            return middle_glyph(x_in, y_in, split, change_points, diffs, idx, theta)

    # the patches to plot
    patches = {f"{x + 1}": {} for x in range(len(change_points) + 1)}
    # above or below dictionary, helps to colour the patches
    a_b_dict = {f"{x + 1}": {'words': None, 'colour': None} for x in range(len(change_points) + 1)}
    x_point = None

    # for each change point (pass the line to switch at)
    for x in range(1, len(change_points) + 2):
        # calculate x, y, right-most point on x-axis, position of patch
        patches[str(x)]["x"], patches[str(x)]["y"], x_point, a_b_dict[str(x)]["words"] = make_glyph_coords(X, y, split, change_points, diffs,  x - 1, x_point)

        # assign colour based on position of patch
        if a_b_dict[str(x)]['words'] == 'below':
            a_b_dict[str(x)]['colour'] = below_colour
        elif a_b_dict[str(x)]['words'] == 'above':
            a_b_dict[str(x)]['colour'] = above_colour
    # initial data
    line_dict = {"x": X, "y": y, "ymean": [split for x in range(len(y))],}
    patch_sources = {x+1: ColumnDataSource(data = {'x': i["x"], 'y': i['y'],}) for x,i in enumerate(patches.values())}
    # create single CDS for all of the glyphs
    line_source = ColumnDataSource(data=line_dict)
    p.line('x', 'y', source=line_source, line_width=3, )
    p.line('x', 'ymean', source=line_source, line_width=3, )
    patch_glyphs = {}
    for x in range(1, len(change_points) + 2):
        patch_glyphs[str(x)] = p.patch(f'x', f"y", source=patch_sources[x],
                                       fill_color=a_b_dict[str(x)]['colour'], alpha=0.5)
    return p
# y values
below_colour = "red"
above_colour = "green"
y = np.array([np.random.randint(10, 80) for x in range(10)])
X = np.array(sorted([np.random.randint(10, 80) for x in range(10)]))

# ensure that each x value is unique
check = True
while check:
    if max(Counter(X).values()) > 1:
        X = np.array(sorted([np.random.randint(10, 80) for x in range(10)]))
    else:
        check = False
ymean = y.mean()
split = np.random.randint(y.min()+1,y.max()-1)

# plot 2 lines (data, data's average) and then each patch
TOOLS = "pan,wheel_zoom,reset,hover,save"
p = figure(plot_width=1400, plot_height=800, title=f"Fill Between Example, seed : {a}", tools=TOOLS)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"
p = main(p, X, y, below_colour, above_colour, split)
show(p)
