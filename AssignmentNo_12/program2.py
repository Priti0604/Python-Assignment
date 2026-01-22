#print factors of a number
 
No= int(input("Enter the number :"))
print("Factors of", No, "are:")
for i in range(1, No + 1):
    if No % i == 0:
        print(i)