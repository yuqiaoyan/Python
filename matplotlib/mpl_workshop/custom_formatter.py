import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# a random walk
prices = (1 + 0.01*np.random.randn(30)).cumprod() * 10
fig, ax = plt.subplots(1)
ax.plot(prices)
ax.grid()

# format the y tick labels as dolllars
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%.2f'))

plt.show()
