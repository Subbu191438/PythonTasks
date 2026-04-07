def number_generator(n):
    for i in range(1, n + 1):
        yield 
gen = number_generator(5)

for num in gen:
    print(num)
