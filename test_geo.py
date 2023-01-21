"""Unit test for the geo module"""

from floodsystem.geo import calculate_distance, stations_by_distance, stations_within_radius
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