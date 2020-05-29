def fibinacci():
    current, previous = 0, 1
    while True:
        current, previous = current + previous, current
        yield current



fib = fibinacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
