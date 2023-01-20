# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():

    # Build list of stations
    stations = build_station_list()
    for station in stations:
        # check output is boolean as expected
        consistent = station.typical_range_consistent()
        assert type(consistent) is bool

def test_inconsistent_typical_range_stations():

    # Build list of stations
    stations = build_station_list()
    num = len(stations)

    # check does not return more stations than were checked for
    assert num >= len(inconsistent_typical_range_stations(stations))