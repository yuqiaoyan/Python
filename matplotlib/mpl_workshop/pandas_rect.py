import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.widgets as widgets

converters = {'Date' : cbook.todate('%Y-%m-%d') }
df = pandas.read_csv('data/CROX.csv', converters=converters)
df = df.sort('Date')
df = df[-500:] # get the two years or so
df['daily_return'] = df['Adj Close']/df['Adj Close'].shift(1) - 1

def on_rectangle_select(event_press, event_release):
    'args the press and release events'
    x1, y1 = event_press.xdata, event_press.ydata
    x2, y2 = event_release.xdata, event_release.ydata
    print "RECT: (%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2)

    if x1>x2:
        x1, x2 = x2, x1

    if y1>y2:
        y1, y2 = y2, y1

    x = df[xfield]
    y = df[yfield]
    # find the region of the dataframe in the selection
    mask = (x>=x1) & (x<=x2) & (y>=y1) & (y<=y2)
    print(df[mask].to_string())


# create a new figure and replot
xfield, yfield = 'Volume', 'daily_return'
fig, ax = plt.subplots(1)
ax.grid()
line, = ax.plot(df[xfield], df[yfield], 's')

rect_select = widgets.RectangleSelector(
    ax, on_rectangle_select, drawtype='box', useblit=True,
    button=[1,], # use left button
    minspanx=5, minspany=5, spancoords='pixels',  # ignore rects that are too small
    )

plt.show()
