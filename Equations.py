import numpy as np


def movement_equation(x0, v0, a0, finish):
    return [x0 + v0*x + 0.5*a0*x**2 for x in np.arange(0, finish, 0.01)]

