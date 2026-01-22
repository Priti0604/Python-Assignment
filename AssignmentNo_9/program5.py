#Program to check whether number is divisible by 3 and 5

def chkDivisible(No):
    if (No % 3 == 0) and (No % 5 == 0):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

No = int(input("Enter Number : "))
chkDivisible(No)            