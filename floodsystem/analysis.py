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