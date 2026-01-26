#Frequency of a number in List

n = int(input("Enter number of elements: "))
list = []

for i in range(n):
    elements = int(input("Enter element: "))
    list.append(elements)

search = int(input("Enter element to search: "))

count = list.count(search)

print("Frequency is:", count)
