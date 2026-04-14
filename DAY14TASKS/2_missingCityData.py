import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
s = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])
missing = s.isna()
print(s)
print(missing)
