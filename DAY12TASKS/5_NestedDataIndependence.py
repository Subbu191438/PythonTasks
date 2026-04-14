import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

deep_copy = copy.deepcopy(classes)

classes[0][1][0] = 100

print("Original:", classes)
print("Deep Copy:", deep_copy)
