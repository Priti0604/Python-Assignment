#Program for checking a prime number 

No = int(input("Enter a number: "))
for i in range(2,No):
    if No % i == 0:
        print(No,"is not a prime number")
        break
else:
    print(No,"is a prime number")   
    

