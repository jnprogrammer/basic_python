def avg(*args):
    print(type(args))
    print("args is {}:".format(args)) # tells python to expect a tuple
    print("*args is: ", *args) # *args tells python to expect an unpacked tuple
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(avg(1, 2, 3, 4, 5, 6, 7, 8, 9))


def build_tuple(*args):
    return print(args)

build_tuple((43,53,53,53,52,243,233,445,3,432))