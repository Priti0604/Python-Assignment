#Addition of Prime Numbers from List (Using Function & Module)

def ChkPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
   