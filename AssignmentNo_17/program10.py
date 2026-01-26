#Accept a number and return the sum of its digits.


No = int(input("Enter a number: "))
sum = 0
for i in range(len(str(No))):
    digit = No % 10         #extracts last digit
    sum = sum + digit       #adds last digit to sum
    No = No // 10           #removes last digit

print("The sum of digits in the number is: ", sum)