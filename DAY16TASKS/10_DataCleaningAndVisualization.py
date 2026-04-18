import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array([100, np.nan, 200, 150, np.nan, 300])
series = pd.Series(data)
print(series)
# Calculate mean (ignores NaN automatically)
mean_value = series.mean()

# Replace NaN with mean
cleaned_series = series.fillna(mean_value)

print("Mean value:", mean_value)
print(cleaned_series)
# Line graph
cleaned_series.plot(marker='o')

plt.title("Line Graph of Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

plt.show()
# Filter values greater than average
above_avg = cleaned_series[cleaned_series > mean_value]

# Bar chart
plt.bar(above_avg.index, above_avg.values)

plt.title("Values Greater Than Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.show()
