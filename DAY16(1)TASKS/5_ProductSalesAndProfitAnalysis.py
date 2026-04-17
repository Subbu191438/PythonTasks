import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})
#Line Graph
print(df)
plt.plot(df["Product"], df["Sales"], marker='o')
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()
#Bar Chart
plt.bar(df["Product"], df["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product vs Sales")
plt.show()
#Pie Chart
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Contribution")
plt.show()
#Histogram
plt.hist(df["Profit"])
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.title("Profit Distribution")
plt.show()
#Scatter Plot
plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()
