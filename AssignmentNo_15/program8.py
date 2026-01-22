#Number divisible by both 3 and 5 using filter()

number = range(1, 101)
divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, number))
print("Numbers divisible by both 3 and 5 from 1 to 100 are:", divisible_by_3_and_5)