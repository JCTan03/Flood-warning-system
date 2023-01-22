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

def calculate_distance(a,b):
    """
    Task 1B: Calculates great-circle distance between two points on a sphere, given their longitude and latitude (coordinates).
    Uses Haversine library.

    Param:
    - a: tuple, a coordinate
    - b: tuple, a coordinate

    """

    distance = haversine(a,b)   # in km
    return distance

def stations_by_distance(stations, p):
    """
    Task 1B: Calculate and return a list of all stations and their distances from coordinate p in tuples.
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
    Task 1C: Returns a list of all 'stations' (type MonitoringStation) within radius 'r' (type float, in km) of a geographic coordinate 'centre' (tuple of floats)
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

def rivers_with_station(stations):
    """
    Task 1D: Returns a set of with the names of the rivers with a monitoring station.
    """
    names_of_rivers = []
    # Loop through each station to see which river has a station, and add the name of that river to a list
    for station in stations:
        if station.river != None:
            names_of_rivers.append(station.river)
    # Converts the list to a set and returns it
    return set(names_of_rivers)


def stations_by_river(stations):
    """
    Task 1D: Returns a dictionary that maps river names to a list of station objects on a given river.
    """
    d_stations_by_river = {}
    # If a river does not exist as a key, create a new list with the station name as the value. If the river already exists as a key, append the corresponding station to the list.  
    for station in stations:
        if station.river in d_stations_by_river:
            d_stations_by_river[station.river].append(station.name)
        else:
            d_stations_by_river[station.river] = [station.name]
    return d_stations_by_river

def rivers_by_station_number(stations, N):
    """
    Task 1E: Returns a list of N (river name, number of stations) tuples, sorted by the number of stations
    """
    tuples_river_station = []
    # Obtain a dictionary that maps river names to a list of station objects on a given river.
    dict_rivers_station = stations_by_river(stations)
    # Create list of tuples of (river name, number of stations)
    for key in dict_rivers_station:
        tuples_river_station.append((key, len(dict_rivers_station[key])))
    # Sort list of tuples by 2nd element (number of stations) by descending order
    tuples_river_station_sorted = sorted_by_key(tuples_river_station, 1, reverse=True)
    # Create new list of N tuples 
    list_N_stations = []
    for i in range(0, N):
        list_N_stations.append(tuples_river_station_sorted[i])
    # If there are more rivers with the same number of stations as the N-th entry, include these rivers in the list
    while (tuples_river_station_sorted[len(list_N_stations)][1] == list_N_stations[N-1][1]):
        list_N_stations.append(tuples_river_station_sorted[len(list_N_stations)])
    return list_N_stations


