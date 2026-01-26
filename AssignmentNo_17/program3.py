#Return factorial of a number

def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial is:", Factorial(n))
