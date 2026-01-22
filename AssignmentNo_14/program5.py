#Lambda function to check even number

is_even = lambda a,b : a if (a % 2 == 0) else b
print("Even number between 10 and 21 is :",is_even(10,21))