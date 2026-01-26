#Addition of all elements from List

No = int(input("Enter number of elements in the list: "))
list = []
total = 0

for i in range(No):
    element = int(input("Enter element: "))
    list.append(element)    
    total = total + element


print("The sum of all elements in the list is: ", total)


