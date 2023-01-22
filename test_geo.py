"""Unit test for the geo module"""

from floodsystem.geo import calculate_distance, stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def test_calculate_distance():
    """Test calculate distance"""
    distance = calculate_distance((1.0,2.0),(2.0,3.0))
    assert type(distance) is float
    assert distance > 0


def test_stations_by_distance():
    """Test stations by distance"""

    # Build list of stations
    stations = build_station_list()
    stations_by_distance_from = stations_by_distance(stations, (1.0, 2.0))
    num = len(stations)

    assert num == len(stations_by_distance_from) # all stations returned

    for i in range(1, num):
        assert stations_by_distance_from[i-1][1] <= stations_by_distance_from[i][1] # ascending order by distance

def test_stations_within_radius():
    """Test stations within radius"""

    # Build list of stations within -1 km
    stations = build_station_list()
    stations_within_negative_r = stations_within_radius(stations, (1.0, 2.0), -1)

    # Check that there are no stations within negative radius
    assert len(stations_within_negative_r) == 0

def test_rivers_with_station():
    """Test rivers_with_station"""
    stations = build_station_list()
    set_rivers_with_station = rivers_with_station(stations)
    # check that the set has elements
    assert len(set_rivers_with_station) != 0 

def test_stations_by_river():
    """Test stations_by_river"""
    stations = build_station_list()
    set_rivers_with_station = rivers_with_station(stations)
    d_stations_by_river = stations_by_river(stations)
    # check that the number of keys in the dictionary is the same as the number of elements in set_rivers_with_station
    assert len(d_stations_by_river.keys()) == len(set_rivers_with_station)