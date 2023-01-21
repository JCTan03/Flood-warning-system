from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)
    rivers_list = list(rivers_set)
    rivers_list.sort()
    rivers_list_ten = []
    for i in range(0, 10):
        rivers_list_ten.append(rivers_list[i])
    print("{}".format(len(rivers_set)) + " stations. " + "First 10 - {}".format(rivers_list_ten))

    d_rivers_stations = stations_by_river(stations)
    d_rivers_stations['River Aire'].sort()
    d_rivers_stations['River Cam'].sort()
    d_rivers_stations['River Thames'].sort()
    print(d_rivers_stations['River Aire'])
    print(d_rivers_stations['River Cam'])
    print(d_rivers_stations['River Thames'])
                            

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

