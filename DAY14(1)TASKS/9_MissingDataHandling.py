import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
series = pd.Series(arr)
mean_val = series.mean()
updated = series.fillna(mean_val)
print(updated)
