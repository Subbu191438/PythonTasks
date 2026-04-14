import pandas as pd
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
result = S1 + S2
final = result.fillna(0)
print("Result with NaN:")
print(result)
print("\nFinal result:")
print(final)
