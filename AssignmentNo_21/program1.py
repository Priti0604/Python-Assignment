#Prime and NonPrime Threads

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers(numbers):
    print("Prime Numbers:")
    for n in numbers:
        if is_prime(n):
            print(n, end=" ")
    print()

def non_prime_numbers(numbers):
    print("Non-Prime Numbers:")
    for n in numbers:
        if not is_prime(n):
            print(n, end=" ")
    print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t1 = threading.Thread(target=prime_numbers, args=(numbers,))
t2 = threading.Thread(target=non_prime_numbers, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

