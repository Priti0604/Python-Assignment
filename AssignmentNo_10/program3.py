#Factorial of a Number
N = int(input("Enter Number : "))
Factorial = 1   
for i in range(1,N+1):
    Factorial = Factorial * i       
print("Factorial of the number is :",Factorial)
