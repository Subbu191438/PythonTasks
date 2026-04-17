import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

# Line graph
plt.figure()
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Marks Trend")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Bar chart
plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Student vs Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Pie chart (Pass > 50)
pass_count = (df["Marks"] > 50).sum()
fail_count = (df["Marks"] <= 50).sum()

plt.figure()
plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df.index, df["Marks"])
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
