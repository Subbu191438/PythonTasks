employees = [[101, "A"], [102, "B"], [103, "C"]]

shallow_copy = employees.copy()
shallow_copy[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow_copy)
