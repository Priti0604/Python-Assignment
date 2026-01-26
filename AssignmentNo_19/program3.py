#filter(), map(), reduce() (range 70 to 90)

from functools import reduce

numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

filtered = list(filter(lambda x: x >= 70 and x <= 90, numbers))
mapped = list(map(lambda x: x + 10, filtered))
result = reduce(lambda a, b: a * b, mapped)

print("List after filter =", filtered)
print("List after map =", mapped)
print("Output of reduce =", result)
