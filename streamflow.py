import matplotlib.pyplot as plt
import numpy as np

array2 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
x = array2[:,0].astype('datetime64')
y_1 = array2[:,1].astype(float)
y_2 = array2[:,2].astype(float)
y_3 = array2[:,3].astype(float)
y_4 = array2[:,4].astype(float)
y_5 = array2[:,5].astype(float)

plt.plot(x,y_1, color = 'purple', label = '10163000')
plt.plot(x,y_2, color = 'blue', label = '10155200')
plt.plot(x,y_3, color = 'green', label = '10155500')
plt.plot(x,y_4, color = 'orange', label = '10154200')
plt.plot(x,y_5, color = 'red', label = '10155000')
plt.legend(title = 'Site Numbers', loc='upper right', fontsize = 10)
plt.xlabel('Date', fontsize = 10)
plt.ylabel('Flowrate (cfs)', fontsize = 10)
plt.title('Provo River Streamflow Data (2021)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.show()