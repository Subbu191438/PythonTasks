import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)
#Line Graph
plt.plot(df["Day"], df["Temperature"], marker='o')
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.show()
#Bar Chart
plt.bar(df["Day"], df["Temperature"])
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Day-wise Temperature")
plt.show()
#Pie Chart
high = (df["Temperature"] > 30).sum()
low = (df["Temperature"] <= 30).sum()

plt.pie([high, low], labels=["High", "Low"], autopct="%1.1f%%")
plt.title("High vs Low Temperature")
plt.show()
#Histogram
plt.hist(df["Temperature"])
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")
plt.show()
#Scatter Plot
plt.scatter(df.index, df["Temperature"])
plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.title("Index vs Temperature")
plt.show()
