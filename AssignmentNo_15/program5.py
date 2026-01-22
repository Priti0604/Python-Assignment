#Maximum  element in a list using reduce()

from functools import reduce
numbers = [3, 5, 2, 8, 1, 4]
maximum = reduce(lambda x, y: x if x > y else y, numbers)   
print("Maximum element in the list is:", maximum)