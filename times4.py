import timeit

setArg = "??"


def timetable():
    for i in range(1, 13):
        for j in range(1, 13):
            print("{0} time {1} is {2}".format(j, i, i * j))
        print("_" * 30)

factorial_test1 = """\
def fact1(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result


x = fact1(130)
"""

factorial_test2 = """\
def fact2(n):
    if n <= 1:
        return 1
    else:
        return n * fact2(n - 1)


y = fact2(130)
"""
temp1 = timeit.timeit(factorial_test1, number=3000)
temp2 = timeit.timeit(factorial_test2, number=3000)

out1 = "Fact1 time: {}".format(timeit.timeit(factorial_test1))
out2 = "Fact2 time: {}".format(timeit.timeit(factorial_test2))
print(out1)
print(out2)

with open("fact_times.txt", 'w') as fact_file:
    print(out1, "\n", out2, file=fact_file)