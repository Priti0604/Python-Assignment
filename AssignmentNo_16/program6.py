#Check Positive, Negative or Zero using function

def check_number(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

No = int(input("Enter a number: "))
check_number(No)       #function call