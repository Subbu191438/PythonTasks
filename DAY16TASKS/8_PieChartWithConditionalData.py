import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
scores = np.array([40, 60, 80, 30, 90])
score_series = pd.Series(scores)

print(score_series)
# Count Pass and Fail
pass_count = (score_series > 50).sum()
fail_count = (score_series <= 50).sum()

print("Pass:", pass_count)
print("Fail:", fail_count)
labels = ["Pass", "Fail"]
counts = [pass_count, fail_count]

# Plot pie chart
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pass vs Fail Distribution")
plt.show()
