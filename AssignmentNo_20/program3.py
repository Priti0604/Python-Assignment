#EvenList and OddList Threads
   
import threading

def even_list(lst):
    evens = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
    print("Even List:", evens)
    print("Sum:", sum(evens))

def odd_list(lst):
    odds = []
    for i in lst:
        if i % 2 != 0:
            odds.append(i)
    print("Odd List:", odds)
    print("Sum:", sum(odds))

numbers = [10, 21, 32, 43, 54, 65, 76]

t1 = threading.Thread(target=even_list, args=(numbers,))
t2 = threading.Thread(target=odd_list, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()
