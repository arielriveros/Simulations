from matplotlib import pyplot as plt
import numpy as np
import Equations
from scipy.interpolate import spline
import sys


def smooth_plot(x_axis, y_axis, smoothness, color, show):
    x_axis = np.array(x_axis)
    y_axis = np.array(y_axis)
    x_smooth = np.linspace(x_axis.min(), x_axis.max(), smoothness)
    y_smooth = spline(x_axis, y_axis, x_smooth)
    plt.plot(x_smooth, y_smooth, color)
    plt.grid()
    if show:
        plt.show()
    else:
        pass



sys.exit()
