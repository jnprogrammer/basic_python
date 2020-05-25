def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n - 1)


try:
    print(factorial(44243))
except (RecursionError, ZeroDivisionError):
    print("Can't print factorials that big and")
    print("Can't divide by 0, you know this!")
print("Program ending")

