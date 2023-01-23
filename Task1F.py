from floodsystem.stationdata import build_station_list
from floodsystem.utils import get_sorted_names
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # get inconsistent stations
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # print station names ordered alphabetically
    print(get_sorted_names(inconsistent_stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
