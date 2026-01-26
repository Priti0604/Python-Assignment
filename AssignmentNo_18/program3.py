#Minimum number from List

n = int(input("Enter number of elements: "))
list = []

for i in range(n):
    element =int(input("Enter element: "))
    list.append(element)

print("Minimum number is:", min(list))