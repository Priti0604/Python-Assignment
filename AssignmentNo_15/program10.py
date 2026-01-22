#count of even numbers using filter() 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = len(list(filter(lambda x: x % 2 == 0, numbers)))      

print("Count of even numbers from 1 to 10 is:", even_numbers)