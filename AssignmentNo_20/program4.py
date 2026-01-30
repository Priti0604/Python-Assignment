#Small, Capital, and Digits Threads

import threading

def count_small(text):
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase:", sum(1 for c in text if c.islower()))

def count_capital(text):
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase:", sum(1 for c in text if c.isupper()))

def count_digits(text):
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", sum(1 for c in text if c.isdigit()))

string = "HelloWorld123Python"

t1 = threading.Thread(target=count_small, args=(string,), name="Small")
t2 = threading.Thread(target=count_capital, args=(string,), name="Capital")
t3 = threading.Thread(target=count_digits, args=(string,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

