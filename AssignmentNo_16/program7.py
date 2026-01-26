#Check whether number is divisible by 5 using function

def Devisible_by_5(No):
    if No % 5 == 0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

No = int(input("Enter a number: "))
Devisible_by_5(No)       #function call
        