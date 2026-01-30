#EvenFactor and OddFactor Threads

import threading

def even_factor(num):
    evens = []
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            evens.append(i)
    print("Even Factors:", evens)
    print("Sum of Even Factors:", sum(evens))

def odd_factor(num):
    odds = []
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            odds.append(i)
    print("Odd Factors:", odds)
    print("Sum of Odd Factors:", sum(odds))

number = 36

t1 = threading.Thread(target=even_factor, args=(number,))
t2 = threading.Thread(target=odd_factor, args=(number,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
