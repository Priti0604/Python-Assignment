#Lambda function to check odd number

is_odd = lambda a,b : a if(a % 2 !=0) else b
print("Odd number between 10 and 21 is :",is_odd(10,21))