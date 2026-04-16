import numpy as np
import pandas as pd
marks = np.random.randint(0, 101, 10)
df = pd.DataFrame(marks, columns=["Marks"])
passed = df[df["Marks"] >= 40]
mean_marks = np.mean(df["Marks"])
print("All Students Marks:")
for m in df["Marks"]:
    print(m)

print("\nPassed Students:")
for m in passed["Marks"]:
    print(m)

print("\nAverage Marks:", mean_marks)
