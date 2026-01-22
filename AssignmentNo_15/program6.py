#Minimum element in a list using reduce()

from functools import reduce
numbers = [3, 5, 2, 8, 1, 4]
minimum = reduce(lambda x, y: x if x < y else y, numbers)   
print("Minimum element in the list is:", minimum)