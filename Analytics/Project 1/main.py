#Project Title: Railway Gauge Data Analysis
#===============================================================================
# Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
#1.Import Required Libraries
#===============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#===============================================================================
'''Scenario 1: Basic Data Loading & Cleaning
You are given a CSV file containing railway gauge data.
👉 Tasks:
1. Load the dataset into a Pandas DataFrame.
2. Display the first 5 rows and column names.
3. Check for missing values and replace them with 0.
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.'''
df= pd.read_csv("railway_gauges 1.csv")
print(df.head())
print(df.columns)
df = df.fillna(0)
cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"] 
df[cols] = df[cols].apply(pd.to_numeric,errors='coerce')
#===============================================================================
''' Scenario 2: Simple Visualization
You want a quick understanding of total railway track growth.
👉 Tasks:
1. Extract Year and Total columns.
2. Plot a line graph showing Total tracks over years.
3. Add:
○ Title
○ X and Y labels
4. Identify whether the trend is increasing or decreasing.'''

x=df["Year"]
y=df["Total"]
plt.plot(x,y,marker="o")
plt.title("Total Railway Tracks Over Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
plt.tight_layout()
plt.show()
print("Trend is increasing year by yaer")
#===============================================================================
'''Scenario 3: Filtering + Bar Chart
You are asked to analyze modern railway expansion.
👉 Tasks:
1. Filter the dataset for years after 2000.
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
3. Plot a grouped bar chart comparing all three gauges.
4. Add legend and proper labels.
5. Identify which gauge dominates in recent years.'''

df2=df[df["Year"]>2000]
x=df2["Year"]
plt.bar(x-0.2, df2["Broad"], width=0.2, label="Broad")
plt.bar(x, df2["Metre"], width=0.2, label="Metre")
plt.bar(x+0.2, df2["Narrow"], width=0.2, label="Narrow")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Gauge Length")
plt.show()
#===============================================================================
'''Scenario 4: Feature Engineering + Pie Chart
You want to analyze the contribution of each gauge type.
👉 Tasks:
1. Calculate total sum of each gauge across all years.
2. Create a new structure (Series/DataFrame) for totals.
3. Plot a pie chart showing percentage contribution.
4. Add percentage labels (autopct).
5. Interpret which gauge contributes the most.'''

totals = df[["Broad", "Metre", "Narrow"]].sum()
plt.pie(totals, labels=totals.index, autopct="%1.1f%%")
plt.title("Gauge Contribution")
plt.savefig("Graphs/gauge_pie.png")
plt.show()
#===============================================================================
'''Scenario 5: Advanced Analysis + Multiple Graphs
You are asked to perform a complete analysis of railway trends.
👉 Tasks:
1. Create new columns:
○ % Broad Gauge
○ % Metre Gauge
○ % Narrow Gauge
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
3. Plot:
○ Line graph for all gauges
○ Stacked bar chart showing composition
4. Highlight:
○ Years with highest growth
○ Decline in any gauge
5. Provide a final conclusion:
👉 “Is the railway system shifting towards a single dominant gauge?”'''

df["%Broad"] = df["Broad"] / df["Total"] * 100
df["%Metre"] = df["Metre"] / df["Total"] * 100
df["%Narrow"] = df["Narrow"] / df["Total"] * 100

growth = np.diff(df["Total"])

# Line graph
plt.plot(df["Year"], df["Broad"], label="Broad")
plt.plot(df["Year"], df["Metre"], label="Metre")
plt.plot(df["Year"], df["Narrow"], label="Narrow")
plt.legend()
plt.savefig("Graphs/all_gauges.png")
plt.show()

# Stacked bar
plt.bar(df["Year"], df["Broad"], label="Broad")
plt.bar(df["Year"], df["Metre"], bottom=df["Broad"], label="Metre")
plt.bar(df["Year"], df["Narrow"], bottom=df["Broad"]+df["Metre"], label="Narrow")
plt.legend()
plt.savefig("Graphs/stacked.png")
plt.show()
#===============================THE END=========================================

