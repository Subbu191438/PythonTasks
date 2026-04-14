import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})
df["Status"] = ["Pass" if x >= 50 else "Fail" for x in df["Marks"]]
passed = df[df["Status"] == "Pass"]
avg_marks = passed["Marks"].mean()
print(df)
print("\nPassed Students:")
print(passed)
print("\nAverage Marks of Passed Students:", avg_marks)
