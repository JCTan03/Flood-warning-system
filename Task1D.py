from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    # Obtain set of rivers with stations
    rivers_set = rivers_with_station(stations)
    # Convert set to list and sort 
    rivers_list = list(rivers_set)
    rivers_list.sort()
    # Add first ten rivers by alphabetical order to a new list 
    rivers_list_ten = []
    for i in range(0, 10):
        rivers_list_ten.append(rivers_list[i])
    print("{}".format(len(rivers_set)) + " stations. " + "First 10 - {}".format(rivers_list_ten))
    
    # Obtain dictionary with rivers as keys and stations as values
    d_rivers_stations = stations_by_river(stations)
    # Sort the stations of these 3 rivers by alphabetical order
    for river in ['River Aire', 'River Cam', 'River Thames']:
        d_rivers_stations[river].sort()
        print(d_rivers_stations[river])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

