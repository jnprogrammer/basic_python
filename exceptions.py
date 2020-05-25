def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(44243))
except RecursionError:
    print("Can't print factorials that big")
print("Program ending")
