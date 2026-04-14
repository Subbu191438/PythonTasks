import pandas as pd
import numpy as np
S = pd.Series([10, 50, 30, 80, 20])
updated = np.where(S > 40, 0, S)
updated_series = pd.Series(updated)
print(updated_series)
