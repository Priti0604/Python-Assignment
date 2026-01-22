#print reverse of a number\

No = int(input("Enter the number :"))
reverse = 0
while No != 0:
    digit = No % 10
    reverse = reverse * 10 + digit
    No = No // 10  
print("Reverse of the number is", reverse)