def theCount(first, multi, divide):
    thecount = (first * multi) // divide
    print(thecount)


def fact(n):
    """Calculate n iteratively"""
    results = 1
    if n > 1:
        for f in range(2, n + 1):
            results *= f
    return results


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fib_basic(n):
    if n <2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    fib_cache = {}
    if n in fib_cache:
       return fib_cache[n]
    #Normal fib sequence
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = value
    return value

for n in range(1,10):
    print(n," : ", fibonacci(n))
# for i in range(130):
#     print(i, fibonacci(i))
#
# theCount(45, 2, 6)
