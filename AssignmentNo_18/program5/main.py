import MarvelousNum

n = int(input("Enter number of elements: "))
lst = []
sum_prime = 0

for i in range(n):
    lst.append(int(input("Enter element: ")))

for num in lst:
    if MarvelousNum.ChkPrime(num):
        sum_prime = sum_prime + num

print("Addition of prime numbers is:", sum_prime)
