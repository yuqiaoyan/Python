import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as colors

"""
segmentdata argument is a dictionary with a red, green and blue
entries. Each entry should be a list of *x*, *y0*, *y1* tuples,
forming rows in a table.

Example: suppose you want red to increase from 0 to 1 over
the bottom half, green to do the same over the middle half,
and blue over the top half.  Then you would use::

    cdict = {'red':   [(0.0,  0.0, 0.0),
                       (0.5,  1.0, 1.0),
                       (1.0,  1.0, 1.0)],

             'green': [(0.0,  0.0, 0.0),
                       (0.25, 0.0, 0.0),
                       (0.75, 1.0, 1.0),
                       (1.0,  1.0, 1.0)],

             'blue':  [(0.0,  0.0, 0.0),
                       (0.5,  0.0, 0.0),
                       (1.0,  1.0, 1.0)]}

Each row in the table for a given color is a sequence of
*x*, *y0*, *y1* tuples.  In each sequence, *x* must increase
monotonically from 0 to 1.  For any input value *z* falling
between *x[i]* and *x[i+1]*, the output value of a given color
will be linearly interpolated between *y1[i]* and *y0[i+1]*::

    row i:   x  y0  y1
                   /
                  /
    row i+1: x  y0  y1

Hence y0 in the first row and y1 in the last row are never used.
"""

cdict = {'red':   ((0.0,  1.0, 1.0),
                   (0.5,  0.5, 0.5),
                   (1.0,  0.0, 0.0)),

         'green': ((0.0,  0.0, 0.0),
                   (0.5,  0.5, 0.5),
                   (1.0,  1.0, 1.0)),

         'blue':  ((0.0,  0.0, 0.0),
                   (0.5,  0.5, 0.5),
                   (1.0,  0.0, 0.0
                    ))}


short_long = colors.LinearSegmentedColormap('shortlong', cdict)


delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = Z2-Z1  # difference of Gaussians

im = plt.imshow(Z, interpolation='bilinear', cmap=short_long,
                origin='lower', extent=[-3,3,-3,3])


plt.show()
