import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas


# load some Yahoo Finance CSV data from CROX, parsing the datestrings
# to python date objects
import matplotlib.cbook as cbook
converters = {'Date' : cbook.todate('%Y-%m-%d') }
df = pandas.read_csv('data/CROX.csv', converters=converters)
df = df.sort('Date')
df = df[-500:] # get the two years or so

# compute daily price differences and returns and add them to the
# dataframe
prices = df['Adj Close']
prices_last = prices.shift(1)
df['price_delta'] = prices - prices_last
df['daily_return'] = df['price_delta'] / prices_last

print df[-5:].to_string()

#xfield, yfield = 'Date', 'Adj Close'
#fig, ax = plt.subplots(1)
#ax.plot(df[xfield], df[yfield])

class PandasPlotter:
    def __init__(self, dataframe, xfield, yfield, ax=None, **kwargs):
        """
        make a plot of xfield vs yfield in pandas dataframe

        kwargs are passed on to pyplot.plot
        """
        self.xfield = xfield
        self.yfield = yfield
        self.dataframe = dataframe

        # create an axes if none is provided
        if ax is None:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(1)
        self.fig = ax.figure
        self.ax = ax

        self.line, = ax.plot(self.dataframe[self.xfield],
                             self.dataframe[self.yfield],
                             **kwargs)


        # set useblit True on gtkagg for enhanced performance
        import matplotlib.widgets as widgets
        self.span = widgets.SpanSelector(
            ax, self.on_select, 'horizontal',useblit=True,
            rectprops=dict(alpha=0.5, facecolor='red') )

        x = self.dataframe[self.xfield]
        # mpl converts dates to floats runder the hood so we'll have
        # to special case some stuff below if dates are involved
        self._is_xdate = ( isinstance(x[0], datetime.date) or
                           isinstance(x[0], datetime.datetime))


        if self._is_xdate:
            # this func rotates the x tick labels to make some room
            # for long date labels
            self.fig.autofmt_xdate()

        self.fig.tight_layout()

    def on_select(self, xmin, xmax):
        """
        callback when the span selector selects a region between xmin
        and xmax
        """

        print('SELECT: xmin=%s, xmax=%s'%(xmin, xmax))

        x = self.dataframe[self.xfield]
        if self._is_xdate:
            # mpl represents dates internally as floats, so convert x
            # to the same type coming back from the widget
            import matplotlib.dates as dates
            x = dates.date2num(x)

        # find the region of the dataframe in the selection
        mask = (x>=xmin) & (x<=xmax)
        print(self.dataframe[mask].to_string())


pplot = PandasPlotter(df, 'Date', 'Adj Close')
#pplot = PandasPlotter(df, 'Volume', 'Adj Close', linestyle='', marker='o')
plt.show()
