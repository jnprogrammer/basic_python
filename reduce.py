import timeit, functools


def cal_vals(x, y: int):
    return x * y

numbers = [2, 3, 5, 8, 13]


reduce_val = functools.reduce(cal_vals, numbers)
print(reduce_val)

result = 1
for x in numbers:
    result *= x
print(result)



result = cal_vals(2, 3)
result = cal_vals(result, 5)
result = cal_vals(result, 8)


