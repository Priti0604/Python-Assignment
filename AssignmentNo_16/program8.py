#Print given number of “*” using function

def print_stars(No):
    for i in range(No):
        print("*", end="")          # here end is used to print in same line


No = int(input("Enter the number of * to print: "))
print_stars(No)       #function call