import numpy as np
data = np.random.rand(8)
normalized_data = data * 100
filtered_values = normalized_data[normalized_data > 50]
sorted_values = np.sort(filtered_values)
print("Original Random Values:\n", data)
print("Normalized Values:\n", normalized_data)
print("Filtered Values (>50):\n", filtered_values)
print("Sorted Filtered Values:\n", sorted_values)
