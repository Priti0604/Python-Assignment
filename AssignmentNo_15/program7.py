#String having length greater than 5 using filter()

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
long_strings = list(filter(lambda s: len(s) > 5, strings))      
print("Strings with length greater than 5 are:", long_strings)