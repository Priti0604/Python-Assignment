#Display vertical line star pattern using function

def vertical_line_stars(num):
    for i in range(num):
        print("*")  

number = int(input("Enter number of stars to print vertically: "))
vertical_line_stars(number)
