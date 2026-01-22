#Print all even numbers till given number
N = int(input("Enter Number : "))
print("Even numbers till",N,"are :")        
for i in range(1,N+1):
    if i % 2 == 0:
        print(i)    
        