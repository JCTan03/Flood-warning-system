from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import get_sorted_names


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # cambridge city centre coordinate
    cambridge_cc = (52.2053, 0.1218)

    # get stations within r km from cambridge_cc
    r = 10
    stations_within_r = stations_within_radius(stations, cambridge_cc, r)

    # print station names ordered alphabetically
    print(get_sorted_names(stations_within_r))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
