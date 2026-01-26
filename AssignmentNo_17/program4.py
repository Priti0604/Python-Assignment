#Return addition of factors of a number


def SumFactors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    return sum

n = int(input("Enter number: "))
print("Sum of factors:", SumFactors(n))
