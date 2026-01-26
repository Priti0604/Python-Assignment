#Accept one number and display the following pattern.


n = int(input("Enter the number: "))

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()