#Lambda function to multiply two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
multiply = lambda a,b : a * b
print("Multiplication of",a,"and",b,"is :",multiply(a,b))