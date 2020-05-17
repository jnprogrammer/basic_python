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


for i in range(130):
    print(i, fact(i))

theCount(45, 2, 6)
