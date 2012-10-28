import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
x = np.linspace(0, 10*np.pi, 100)
y = np.random.randn(len(x)).cumsum()
fig, ax = plt.subplots(1)
ax.plot(x, y)

# place x-ticks on the integer multiples of pi
class PiLocator(ticker.Locator):

    def __call__(self):
        vmin, vmax = self.axis.get_view_interval()
        imin = np.ceil(vmin/np.pi)
        imax = np.floor(vmax/np.pi)
        return np.arange(imin, imax)*np.pi

class PiFormatter(ticker.Formatter):
    def __call__(self, x, pos=None):
        i = int(x/np.pi)
        return r'$%d\pi$'%i

ax.xaxis.set_major_locator(PiLocator())
ax.xaxis.set_major_formatter(PiFormatter())
ax.fmt_xdata = lambda x: '%.4f'%x



plt.show()
