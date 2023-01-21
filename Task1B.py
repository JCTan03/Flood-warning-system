from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Get distances from cambridge city centre
    cambridge_cc = (52.2053, 0.1218)
    stations_by_distance_from = stations_by_distance(stations, cambridge_cc)

    # Get and output 10 closest with relevant information
    stations_by_distance_10_closest = stations_by_distance_from[:10]
    output_10_closest = []
    for station_distance in stations_by_distance_10_closest:
        output_10_closest.append((station_distance[0].name, station_distance[0].town, station_distance[1]))
    print(output_10_closest)

    # Get and output 10 furthest with relevant information
    stations_by_distance_10_furthest = stations_by_distance_from[:10]
    output_10_furthest = []
    for station_distance in stations_by_distance_10_furthest:
        output_10_furthest.append((station_distance[0].name, station_distance[0].town, station_distance[1]))
    print(output_10_furthest)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
