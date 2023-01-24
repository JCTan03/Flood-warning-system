from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    # update live water levels
    update_water_levels(stations)

    # get first 10 stations with highest relative water level
    stations_first_10_rel_water_level = stations_highest_rel_level(stations, 10)

    # print each station name and corresponding water level
    for station in stations_first_10_rel_water_level:
        print(station.name, station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()