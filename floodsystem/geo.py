# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from . import datafetcher
from .station import MonitoringStation

import random
from haversine import haversine
from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    names_of_rivers = []
    for station in stations:
        names_of_rivers.append(station.river)
    return set(names_of_rivers)


def stations_by_river(stations):
    d_stations_by_river = {}
    for station in stations:
        if station.river in d_stations_by_river:
            d_stations_by_river[station.river].append(station.name)
        else:
            d_stations_by_river[station.river] = [station.name]
    return d_stations_by_river

def calculate_distance(a,b):
    """
    Calculates great-circle distance between two points on a sphere, given their longitude and latitude (coordinates).
    Uses Haversine library.

    Param:
    - a: tuple, a coordinate
    - b: tuple, a coordinate

    """

    distance = haversine(a,b)   # in km
    return distance

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

def stations_within_radius(stations, centre, r):
    """
    Returns a list of all 'stations' (type MonitoringStation) within radius 'r' (type float, in km) of a geographic coordinate 'centre' (tuple of floats)
    """
    # List of stations within radius r to output
    stations_within_r = []
    
    # Loop through each station
    for station in stations:
        # Check if the distance from station to 'centre' is less than 'r'
        if calculate_distance(station.coord, centre) <= r:
            stations_within_r.append(station)
    
    # return list stations_within_r
    return stations_within_r
