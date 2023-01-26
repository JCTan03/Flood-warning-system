# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    max_value = 5.5
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, max_value, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.max_value == max_value
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():

    # Build list of stations
    stations = build_station_list()
    for station in stations:
        # check output is boolean as expected
        consistent = station.typical_range_consistent()
        assert type(consistent) is bool

def test_relative_water_level():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        # check if output is a float
        if station.relative_water_level() != None:
            assert type(station.relative_water_level()) is float
            # check if relative water level is greater than 1 if it is higher than the typical high
            if station.latest_level > station.typical_range[1]:
                assert station.relative_water_level() > 1

def test_max_relative_water_level():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        # check if output is a float
        if station.max_relative_water_level() != None:
            assert type(station.max_relative_water_level()) is float

def test_inconsistent_typical_range_stations():

    # Build list of stations
    stations = build_station_list()
    num = len(stations)

    # check does not return more stations than were checked for
    assert num >= len(inconsistent_typical_range_stations(stations))