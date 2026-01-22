#Find the sum of digits of a number 

No = int(input("Enter the number :"))
sum = 0
while No != 0:
    digit = No % 10
    sum = sum + digit
    No = No // 10
print("Sum of digits is", sum)