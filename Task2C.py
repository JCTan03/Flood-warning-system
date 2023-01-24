from floodsystem.flood import stations_highest_rel_level, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    # Obtain latest water levels
    update_water_levels(stations)
    N = 10
    # Obtain list of tuples, where each tuple holds a station at which the latest relative water level is over tol (0.8) and the relative water level at the station
    list_N_station_over_tol = stations_highest_rel_level(stations, N)
    # Print the name of each station at which the current relative level is over tol, with the relative level alongside the name
    for i in range(0, N): 
        print("{}".format(list_N_station_over_tol[i][0]) + " {}".format(list_N_station_over_tol[i][1]))            

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()