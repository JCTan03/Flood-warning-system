# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """checks the typical high/low range data for consistency
        return True if consistent, return False if inconsistent/unavailable
        """
        # check if data is unavailable
        if self.typical_range == None:
            return False
        # check if low > high (invalid data)
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        # otherwise, range is consistent
        else:
            return True


def inconsistent_typical_range_stations(stations):
    """ returns list of stations from the input stations list (type MonitoringStation object) that have inconsistent data"""
    
    # List to return
    inconsistent_stations = []

    # Loop through each station in list
    for station in stations:
        # Check if station is inconsistent
        if station.typical_range_consistent() == False:
            # if inconsistent, add station to list to return
            inconsistent_stations.append(station)
    
    # return list
    return inconsistent_stations

