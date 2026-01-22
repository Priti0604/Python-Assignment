#Lambda function to return largest of three numbers

largest = lambda a,b,c : a if (a > b and a > c) else (b if b > c else c)
print("Largest of 10, 20 and 30 is :",largest(10,20,30))