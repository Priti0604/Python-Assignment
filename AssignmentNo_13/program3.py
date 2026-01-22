#Program to check whether a number is Perfect Number

No = int(input("Enter the number :"))
sum = 0
for i in range(1, No):
    if No % i == 0:
        sum = sum + i       
if sum == No:
    print(No, "is a Perfect Number")    
else:
    print(No, "is not a Perfect Number")
    