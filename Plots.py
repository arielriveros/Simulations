from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import spline
import sys

x = [i for i in range(-10, 10)]
y1 = [t**2 for t in x]
y2 = [np.cos(t)*15 for t in x]
y3 = [-np.power(t, 2) + 20 for t in x]


def smooth_plot(xaxis, yaxis, smoothness, color, show):
    xaxis = np.array(xaxis)
    yaxis = np.array(yaxis)
    x_smooth = np.linspace(xaxis.min(), xaxis.max(), smoothness)
    y_smooth = spline(xaxis, yaxis, x_smooth)
    plt.plot(x_smooth, y_smooth, color)
    plt.grid()
    if show:
        plt.show()
    else:
        pass


smooth_plot(x, y1, 300, "r", False)
smooth_plot(x, y2, 300, "g", False)
smooth_plot(x, y3, 300, "y", True)

sys.exit()
