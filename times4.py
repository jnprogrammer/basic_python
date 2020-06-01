import timeit


def timester():
    for i in range(1, 13):
        for j in range(1, 13):
            print("{0} time {1} is {2}".format(j, i, i * j))
        print("_" * 30)


temp = timeit.timeit(timester, globals=globals(), number=3000)
print("Loop time:\t{}".format(temp))