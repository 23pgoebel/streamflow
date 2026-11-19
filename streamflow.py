import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    array2 = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    dates = array2[:,0].astype('datetime64')
    flows = array2[:,1:].astype(float)
    return dates, flows

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    colors = ['purple', 'blue', 'green', 'orange', 'red']
    for column, (site, color) in enumerate(zip(sites, colors)):
        plt.plot(dates, flows[:, column], color=color, label=site)
    plt.legend(title = 'Site Numbers', loc='upper right', fontsize = 10)
    plt.xlabel('Date', fontsize = 10)
    plt.ylabel('Flowrate (cfs)', fontsize = 10)
    plt.title('Provo River Streamflow Data (2021)', fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)