#using function Check whether number is Even or Odd


def check_even_odd(No):
    if No % 2 ==0:
        print("Even Number")
    else:
        print("Odd Number")

No = int(input("Enter a number: "))
check_even_odd(No)