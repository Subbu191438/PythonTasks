import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temps = np.array([28, 30, 32, 31, 29])
temp_series = pd.Series(temps)
print(temp_series)
# Plot line graph
temp_series.plot(marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Day Number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
