#Count the number of digits in a number

No = int(input("Enter the Number :"))
count = 0
while No != 0:
    No = No // 10
    count = count + 1
print("The number of digits in the number is:", count)