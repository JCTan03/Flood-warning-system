from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    tolerance = 0.8
    # Obtain list of tuples, where each tuple holds a station at which the latest relative water level is over tol (0.8) and the relative water level at the station
    list_station_over_tol = stations_level_over_threshold(stations, tolerance)
    # Print the name of each station at which the current relative level is over tol, with the relative level alongside the name
    for i in range(0, len(list_station_over_tol)): 
        print("{}".format(list_station_over_tol[i][0]) + " {}".format(list_station_over_tol[i][1]))            

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()