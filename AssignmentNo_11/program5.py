#Check whther a number is palindrome or not

No = int(input("Enter the number :"))
original_No = No    
reverse = 0
while No != 0:
    digit = No % 10
    reverse = reverse * 10 + digit
    No = No // 10
if original_No == reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")