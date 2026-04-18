import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)
# Create subplots (1 row, 3 columns)
plt.figure(figsize=(15,5))

# Line Graph (Trend)
plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

# Bar Chart (Comparison)
plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# Pie Chart (Distribution)
plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution")
plt.tight_layout()
plt.show()
