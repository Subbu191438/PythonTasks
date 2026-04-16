import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
unique_numbers = set(numbers)
print("Numbers:", numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Unique numbers:", unique_numbers)
