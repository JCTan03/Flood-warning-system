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

    # Plot data
    plt.plot(dates, levels)

    # Add low/high water level marks
    


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()