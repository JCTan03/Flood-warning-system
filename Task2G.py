'''
Our implementation of Task 2G:
We looked at 2 factors: current relative water level, as well as 
whether the water level at a station is rising or falling.
We took into account a new piece of data - the highest ever water level at each station.
We obtained the maximum relative water level using this data, M.
H is the halfway mark between 1.0 and M.
a) Severe: H <= Current relative water level <= M, rising 
b) High:   1.0 <= Current relative water level < H, rising
c) Moderate: 0.7 <= Current relative water level < 1.0, rising OR
             Current relative water level >= 1.0, falling
d) Low: Current relative water level < 0.7, rising OR falling
'''
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import polynomial_coeff
import numpy

def run():
    """
    Task 2G: Return a list of lists, where each tuple holds (i) a station (object) name, 
    (ii) the relative water level at the station, 
    (iii) whether the relative water level is greater than the max.
    The list is sorted by the relative level in descending order.
    """ 
    # Build list of stations
    stations = build_station_list()

    # update live water levels
    update_water_levels(stations)

    list_stations_over_1 = []
    # Loop through each station in list
    for station in stations:
        # Check if station has consistent typical low/high data and proper data for relative water level and max relative water level
        if (station.typical_range_consistent() == True) and (station.relative_water_level() != None) and (station.max_relative_water_level() != None):
            # Check if relative water level is over tol
            if station.relative_water_level() >= 1.0:
                dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=2))
                diff_function = numpy.polyder(polynomial_coeff(station, dates, levels, 4))
                current_gradient = diff_function(0) 
                H = (station.max_relative_water_level() - 1)/2 + 1
                # Categorisation
                if station.relative_water_level() >= H and current_gradient >= 0:
                    print(station.name + ": Severe")
                elif station.relative_water_level() >= 1.0 and station.relative_water_level() < H and current_gradient >= 0:
                    print(station.name + ": High")
                elif station.relative_water_level() >= 0.7 and station.relative_water_level() < 1 and current_gradient >= 0:
                    print(station.name + ": Moderate")
                elif station.relative_water_level() >= 1 and current_gradient < 0:
                    print(station.name + ": Moderate")
                else:
                    print(station.name + ": Low")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()