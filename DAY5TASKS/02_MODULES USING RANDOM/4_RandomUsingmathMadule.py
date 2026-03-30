import random
import math
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 200))
max_val = max(numbers)
min_val = min(numbers)
sqrt_max = math.sqrt(max_val)
log_min = math.log(min_val)
print("Random Numbers:", numbers)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
print("Square root of maximum:", sqrt_max)
print("Logarithm of minimum:", log_min)
