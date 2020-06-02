import timeit
from statistics import mean, stdev

def fact1(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result


# x = fact1(130)



def fact2(n):
    if n <= 1:
        return 1
    else:
        return n * fact2(n - 1)


# y = fact2(130)


if __name__ == '__main__':
    list1 = timeit.repeat("x = fact1(130) ", setup="from __main__ import fact1", number=30, repeat=3)
    list2 = timeit.repeat("x = fact2(130) ", setup="from __main__ import fact2", number=30, repeat=3)

    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))