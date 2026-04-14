import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])
total = np.sum(marks, axis=1)
avg = np.mean(total)
above_avg = total[total > avg]

print("Total marks:", total)
print("Above average:", above_avg)
