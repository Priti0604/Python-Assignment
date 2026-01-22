#Print all odd numbers till given number
N = int(input("Enter Number : "))
print("Odd numbers till", N, "are:")
for i in range(1, N+1):
    if i % 2 != 0:
        print(i, end=' ')
        