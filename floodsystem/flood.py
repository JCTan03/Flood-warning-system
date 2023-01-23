from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """
    Task 2B: Return a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol 
    and (ii) the relative water level at the station. The list is sorted by the relative level in descending order

    """ 
    list_stations_over_threshold = []
    # Loop through each station in list
    for station in stations:
        # Check if station has consistent typical low/high data and proper data for relative water level
        if (station.typical_range_consistent() == True) and (station.relative_water_level() != None):
            # Check if relative water level is over tol
            if station.relative_water_level() > tol:
                # Append station and relative water level as a tuple to the list
                list_stations_over_threshold.append((station.name, station.relative_water_level()))
    # Sort list of tuples by 2nd element (relative level) by descending order
    stations_over_threshold_sorted = sorted_by_key(list_stations_over_threshold, 1, reverse=True)
    return stations_over_threshold_sorted

def stations_highest_rel_level(stations, N):
    """
    Task 2C: Return a list of the N stations (objects) at which the water level, relative to the 
    typical range, is highest. The list is sorted in descending order by relative level.
    
    """ 
    list_stations_over_threshold = []
    list_N_stations_over_threshold = []
    # Loop through each station in list
    for station in stations:
        # Check if station has consistent typical low/high data and proper data for relative water level
        if (station.typical_range_consistent() == True) and (station.relative_water_level() != None):
            # Append station and relative water level as a tuple to the list
            list_stations_over_threshold.append((station.name, station.relative_water_level()))
    # Sort list of tuples by 2nd element (relative level) by descending order
    list_stations_over_threshold_sorted = sorted_by_key(list_stations_over_threshold, 1, reverse=True)
    for i in range(0, N):
        list_N_stations_over_threshold.append(list_stations_over_threshold_sorted[i])
    return list_N_stations_over_threshold
