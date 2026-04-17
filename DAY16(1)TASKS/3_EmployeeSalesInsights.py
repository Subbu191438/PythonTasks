import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salaries=np.array([25000,30000,28000,40000,50000,35000])
departments=["HR","IT","HR","IT","sales","sales"]
df=pd.DataFrame({
    "Department":departments,
    "Salary":salaries
    })
print(df)
#Line Graph
plt.plot(df.index, df["Salary"], marker='o')
plt.xlabel("Index")
plt.ylabel("Salary")
plt.title("Salary Trend")
plt.show()
#Bar Chart
dept_avg = df.groupby("Department")["Salary"].mean()

plt.bar(dept_avg.index, dept_avg.values)
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Department-wise Salary")
plt.show()
#PieChart
dept_count = df["Department"].value_counts()
plt.pie(dept_count.values, labels=dept_count.index, autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()
#Histogram
plt.hist(df["Salary"])
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.show()
#Scatter Plot
plt.scatter(df.index, df["Salary"])
plt.xlabel("Index")
plt.ylabel("Salary")
plt.title("Index vs Salary")
plt.show()
