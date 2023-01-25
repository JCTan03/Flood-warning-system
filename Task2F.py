import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # update live water levels
    update_water_levels(stations)

    # get first 5 stations with highest relative water level
    stations_first_5_rel_water_level = stations_highest_rel_level(stations, 5)

    # plot each station's last 2 days water levels and best-fit polynomial degree 4
    for station in stations_first_5_rel_water_level:
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()