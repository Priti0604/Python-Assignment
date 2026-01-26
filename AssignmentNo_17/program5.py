#Check whether number is prime

def is_prime(No):
    if No <= 1:
        print(No, "is not a prime number")
        return
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            print(No, "is not a prime number")
            return
    print(No, "is a prime number")


No = int(input("Enter a number: "))
is_prime(No)       #function call