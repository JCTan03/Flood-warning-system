from .analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt


"""This module contains a collection of functions related to
plotting water level data.

"""

def plot_water_levels(station, dates, levels):
    """Function to plot station water level data against time, with plot lines for low and high water level marks
    Axis are labelled, title is the station name
    
    Params:
    - station: MonitoringStation object
    - dates: list of datetime objects
    - levels: list of floats
    """

    # Plot level data
    plt.plot(dates, levels)

    # Add low/high water level marks
    lows = [station.typical_range[0]]*len(dates)
    highs = [station.typical_range[1]]*len(dates)

    plt.plot(dates, lows)
    plt.plot(dates, highs)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """function that plots the water level data and the best-fit polynomial"""

    # Plot water level data
    plt.plot(dates, levels)
    
    # Get best-fit polynomial
    poly, d0 = polyfit(dates, levels, p)

    # Plot polynomial on same graph
    dates_float = matplotlib.dates.date2num(dates)
    d0_float = matplotlib.dates.date2num([d0])[0]
    plt.plot(dates, poly(dates_float-d0_float))

    # Add low/high water level marks
    lows = [station.typical_range[0]]*len(dates)
    highs = [station.typical_range[1]]*len(dates)

    plt.plot(dates, lows)
    plt.plot(dates, highs)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.show()
