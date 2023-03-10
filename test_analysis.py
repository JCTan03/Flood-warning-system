"""Unit test for the analysis module"""

from datetime import datetime, timedelta
import numpy as np

from floodsystem.analysis import polyfit

def test_polyfit():

    # test data
    dates = [datetime.today(), datetime.today()-timedelta(days = 1), datetime.today()-timedelta(days=2)]
    levels = [1,2,3]
    p = 2

    # call function
    poly, d0 = polyfit(dates, levels, p)

    # check output is valid type
    assert type(poly) == np.poly1d
    assert type(d0) == datetime