import numpy as np
import matplotlib
import matplotlib.pyplot as plt

"""This module provides functionality for analysing level data
"""

def polyfit(dates, levels, p):
    """function that computes a least-squares fit of a polynomial of degree p to water level data for a station
    Params:
    - water level time history (dates, levels) for a station 
    - p (float), degree of polynomial
    Return:
     tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    """

    # Convert list of dates to list of floats, where the floats are the time in days (including fractions of days) since the year 0001
    x = matplotlib.dates.date2num(dates)

    # Shift dates
    shift = dates[0]
    x_shift = x[0]
    x -= x_shift

    # Find coefficients of best-fit polynomial f(x) of degree p, using x shifted values
    p_coeff = np.polyfit(x, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return (poly, shift)