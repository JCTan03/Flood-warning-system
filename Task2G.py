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

    # Loop through each station in list
    for station in stations:
        # Check if station has consistent typical low/high data and proper data for relative water level and max relative water level
        if (station.typical_range_consistent() == True) and (station.relative_water_level() != None) and (station.max_relative_water_level() != None):
            # Check if relative water level is over 1.0 (to get stations with moderate/high/severe risk)
            if station.relative_water_level() >= 1.0:
                dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=2))
                # After obtaining the best-fit polynomial function for the station, differentiate the polynomial function
                diff_function = numpy.polyder(polynomial_coeff(station, dates, levels, 4))
                # Find the value of the gradient at the current time
                current_gradient = diff_function(0) 
                # Obtain the value of H, which is the halfway mark between 1.0 and maximum relative water level.
                H = (station.max_relative_water_level() - 1)/2 + 1
                # Categorisation into the different risk warnings - if current gradient is positive (being >= 0.00001), that means water level is rising.
                if station.relative_water_level() >= H and current_gradient > 0.00001:
                    print(station.name + ": Severe")
                elif station.relative_water_level() >= 1.0 and station.relative_water_level() < H and current_gradient > 0.00001:
                    print(station.name + ": High")
                elif station.relative_water_level() >= 0.7 and station.relative_water_level() < 1 and current_gradient >= 0.00001:
                    print(station.name + ": Moderate")
                elif station.relative_water_level() >= 1 and current_gradient <= 0.00001:
                    print(station.name + ": Moderate")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()