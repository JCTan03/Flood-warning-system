from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    threshold = 1.0
    list_stations_over_threshold = stations_level_over_threshold(stations, 1.0)
    # check that the list of tuples is in descending order
    for i in range(0, len(list_stations_over_threshold) - 1):
        assert list_stations_over_threshold[i][1] >= list_stations_over_threshold[i+1][1]
    # check that the last tuple is above tolerance
    assert list_stations_over_threshold[len(list_stations_over_threshold) - 1][1] > threshold