'''Project Title: Railway Gauge Data Analysis
# Analyze railway gauge dataset using NumPy, Pandas, Matplotlib'''
#Import Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("railway_gauges 1.csv")
print(df.head())
max_row=df.iloc[[df["Total"].idxmax()]]
print(max_row)
df=df.drop("Total",axis=1)
ax=df.plot(x="Year",kind="bar")
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Total")
plt.title("Gauges:Number of railway tracks installed per year")
plt.savefig("rail_gauges.png")
plt.show()
#Sample project
# │── railway_gauge_data.csv
# │── main.py
# │── graphs/
# │     ├── (all saved graphs)
# │── Sample Project.pdf
