#odd numbers using filter()

numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers from 10 to 21 are:", odd_numbers)