import numpy as np
matrix = np.random.randint(0, 51, size=(3, 3))
filtered_values = matrix[matrix > 25]
print("Random Matrix:\n", matrix)
print("Filtered values (>25):", filtered_values)
