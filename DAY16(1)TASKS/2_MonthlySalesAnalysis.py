import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales=np.array([100,150,200,180,220,300])
months=["jan","feb","mar","apr","may","jun"]
df=pd.DataFrame({
    "month":months,
    "sales":sales
    })
print(df)
#line Bar
plt.plot(df["month"],df["sales"],
marker='o')
plt.xlabel("month")
plt.ylabel("sales")
plt.title("sales trend")
plt.show()
#bar Graph
plt.bar(df["month"],df["sales"]),
plt.xlabel("month")
plt.ylabel("sales")
plt.title("months-wise sales")
plt.show()
#Pie Chart
plt.pie(["sales"],labels=df["months"],
autopct="%1.1f%%")
plt.title("sales contribution by month")
plt.show()
#histogram
plt.hist(df["sales"])
plt.xlabel("sales")
plt.ylabel("frequency")
plt.title("sales Distribution")
plt.show()
#Scatter plot
plt.scatter(df.index,df["sales"])
plt.xlabel("month Index")
plt.ylabel("sales")
plt.title("Index vs Sales")
plt.show()

