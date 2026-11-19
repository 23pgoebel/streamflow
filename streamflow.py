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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()

# Had AI help me make the table and file.
# Excel Returned 131 as the max and 56.95 for the average as gage 10163000.
def summarize(dates, flows, sites):
    """Print and save the summary statistics for each gauge."""
    header = f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<19}{'Min (cfs)':>10}{'Avg (cfs)':>10}"
    print(header)

    summary_rows = []
    for column, site in enumerate(sites):
        gauge_flows = flows[:, column]
        max_index = np.argmax(gauge_flows)
        max_flow = np.max(gauge_flows)
        min_flow = np.min(gauge_flows)
        avg_flow = np.mean(gauge_flows)
        max_date = str(dates[max_index]).replace("T", " ")

        print(f"{site:<12}{max_flow:>10.1f}   {max_date:<19}{min_flow:>10.1f}{avg_flow:>10.1f}")
        summary_rows.append(
            f"{site},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n"
        )

    with open('streamflow_summary.csv', 'w', encoding='utf-8', newline='') as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")
        file.writelines(summary_rows)

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)