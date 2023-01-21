# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from . import datafetcher
from .station import MonitoringStation

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