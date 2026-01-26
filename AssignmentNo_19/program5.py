#filter(), map(), reduce() (prime numbers)

from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [3, 5, 7, 8, 10, 11, 13]

filtered = list(filter(is_prime, numbers))
mapped = list(map(lambda x: x * 2, filtered))
result = reduce(lambda a, b: a if a > b else b, mapped)

print("List after filter =", filtered)
print("List after map =", mapped)
print("Output of reduce =", result)
