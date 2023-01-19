# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import random
from .utils import sorted_by_key  # noqa

def calculate_distance(a,b):
    """IN PROGRESS

    Calculates great-circle distance between two points on a sphere, given their longitude and latitude (coordinates)

    Param:
    - a: tuple, a coordinate
    - b: tuple, a coordinate

    """

    # to implement

    return random.random()

def stations_by_distance(stations, p):
    """Calculate and return a list of all stations and their distances from coordinate p in tuples.
    List is of tuples (station, distance) and is sorted by ascending distance.
    Each station is represented as a MonitoringStation object. Each distance is represented as a float. 

    Param:
    - stations: list of MonitoringStation objects, stations
    - p: tuple of floats, coordinate

    """

    # List of tuples to return
    stations_by_distance_from = []

    # Loop through each station
    for station in stations:
        # Calculate distance between station and coordinate p using Haversine formula
        distance = calculate_distance(p, station.coord)
        # Define station distance tuple and add to list
        station_distance = (station, distance)
        stations_by_distance_from.append(station_distance)

    # Sort list by distance
    stations_by_distance_sorted = sorted_by_key(stations_by_distance_from, 1)

    # Return list
    return stations_by_distance_sorted