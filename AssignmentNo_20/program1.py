#Even and Odd Threads

import threading

def print_even():
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def print_odd():
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

t1 = threading.Thread(target=print_even, name="Even")
t2 = threading.Thread(target=print_odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()

def print_even():
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def print_odd():
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

t1 = threading.Thread(target=print_even, name="Even")
t2 = threading.Thread(target=print_odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()

