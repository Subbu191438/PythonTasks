import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

print(df)
filtered_df = df[df["Marks"] > 50]
print(filtered_df)
# Plot bar chart
plt.bar(filtered_df["Student"], filtered_df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Scoring More Than 50 Marks")
plt.show()
