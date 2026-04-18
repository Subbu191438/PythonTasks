import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)
# Plot line graph
plt.plot(df["Month"], df["Sales"], marker='o')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Line Graph")
plt.show()
