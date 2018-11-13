import numpy as np
import math
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter,DataRange1d , Band, SingleIntervalTicker


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

# y values
y = np.array([20.3, 25.43, 30.2, 27.9, 28.1, 28.2, 32, 25.5, 28.2, 25.5])

# easier to plot 8 vs 8000
X = np.array([x for x in np.arange(len(y))])

#mean array, difference array,
ymean = np.array([y.mean() for x in y])
diffs = y - ymean
kk = []
for x in range(len(y)):
    try:
        if np.sign(ymean[0] - y[x]) == np.sign(ymean[0] - y[x+1]):
            pass
        else:
            kk.append([x,x+1])
    except:
        pass
# print(kk)

ydict={'y{}'.format(x): np.linspace(y[x],y[x+1], 1000) for x in range(len(y)-1)}

# 1000 points between each value in y
xx = np.array([x for x in np.linspace(0, len(y)-1, (len(y)-1) * 1000)])

def func(origy, avgarray, xinput, inputvals):
    print(inputvals, )

    def dofirstthing(inputvals, avgarray):
        num1 = 0
        num2 = inputvals[1]
        theta = math.atan(np.abs(origy[num2] - origy[num1]) / len(origy[:num2]))
        degrees = theta * 180 / math.pi
        tri1adj = (avgarray[0] - origy[num1]) * math.atan(math.radians(90 - degrees))
        cc, magicnumber = find_nearest(xinput, tri1adj)
        xx1 = xinput[:magicnumber].copy()
        newy = np.linspace(origy[num1], origy[num2], 1000)
        find, _ = find_nearest(newy, avgarray[0])
        k = list(newy).index(find)
        newy = np.array([x for x in np.linspace(newy[0], newy[k], magicnumber)])
        return xx1, newy, magicnumber

    def domiddlething(inputvals2, ymean, magicnumber, othernums):
        num1 = inputvals2[0]
        num2 = inputvals2[1]
        theta2 = math.atan(np.abs(y[num2] - y[num1]) / 1)
        degrees2 = theta2 * 180 / math.pi
        tri2adj = np.abs((ymean[0] - y[num2])) * math.atan(math.radians(90 - degrees2))
        cc2, magicnumber2 = find_nearest(xx, tri2adj)
        # print(magicnumber2)
        xx2 = xx[magicnumber:num2 * 1000 - magicnumber2].copy()
        # print(xx2)
        if inputvals2 == inputvals[1]:
            ar = np.linspace(ymean[0], y[othernums[0]], inputvals[0][1]*1000 - magicnumber)
        else:
            ar = np.array([])
        for i in range(othernums[0],othernums[1]):
            ar = np.concatenate((ar, np.linspace(y[i], y[i+1])), axis = None )


        newy2 = np.concatenate((ar, np.linspace(y[i+1], ymean[0], 1000-magicnumber2)), axis = None)

        # newy2 = np.concatenate((np.linspace(ymean[0], y[2], inputvals[0][1]*1000 - magicnumber), np.linspace(y[2], y[3], 1000),
        #                         np.linspace(y[3], y[4], 1000), np.linspace(y[4], y[5], 1000),
        #                         np.linspace(y[5], y[6], 1000), np.linspace(y[6], ymean[0], 1000 - magicnumber2)),axis=None)

        if othernums[1] - othernums[0] ==1:
            newy2= np.concatenate((np.linspace(ymean[0], y[num1], len(xx[(num1*1000)-magicnumber2: num1 * 1000]))), (np.linspace( y[num1], ymean[0],len(xx[num1 * 1000:magicnumber]))),axis = None)

        return xx2, newy2, magicnumber2

    crazydict = {}
    magdict= {}
    for x in range(len(inputvals)-1):
        print('here, ',x)
        if x == 0:
            crazydict['x{}'.format(x)], crazydict['newy{}'.format(x)], magdict['mag{}'.format(x)] = dofirstthing(inputvals[x] ,avgarray)
        elif x == len(kk)-1:
            pass
        else:
            crazydict['x{}'.format(x)], crazydict['newy{}'.format(x)], magdict['mag{}'.format(x)] = domiddlething(inputvals[x], avgarray, magdict['mag{}'.format(x-1)], [inputvals[x-1][1], inputvals[x][0]])
    p = magdict['mag{}'.format(x)]
    crazydict['x{}'.format(x+1)] = xx[p:].copy()
    crazydict['newy{}'.format(x + 1)] = np.linspace(avgarray[0], y[9], len(crazydict['x{}'.format(x+1)]))
    ymean = np.array([y.mean() for x  in range(len(xx))])

    data = ColumnDataSource(data = crazydict)

    return ymean, data
h, d = func(origy = y, avgarray = ymean, xinput = xx, inputvals = kk)

for x in d.data:
    print(x)