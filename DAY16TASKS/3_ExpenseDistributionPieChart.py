import numpy as np
import matplotlib.pyplot as plt
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
# Plot pie chart
plt.pie(expenses, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Monthly Expense Distribution")
plt.show()
