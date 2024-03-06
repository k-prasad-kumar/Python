#recursion using memoization
from functools import lru_cache

#our own memoization function

fib_cache = {}

def fib(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")

    if n < 0:
        raise ValueError("n must be a positive integer")

    if n in fib_cache:
        return fib_cache[n]

    if n == 0 or n == 1:
        value =  n
    else:
        value = fib(n-1) + fib(n-2)

    fib_cache[n] = value
    return value


for i in range(0,301):
    print(i,fib(i))


#using python decorator

@lru_cache(maxsize=1000)
def fib_lru(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")

    if n < 0:
        raise ValueError("n must be a positive integer")

    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,1001):
    print(i,fib_lru(i))