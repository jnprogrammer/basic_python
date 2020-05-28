import sys


def my_range(n: int):
    print("my range starts")
    start = 0
    while start < n:
        print("my range returns: {}".format(start))
        yield start #yield returns value and goes into a suspended state, then next time called it continues from where it left off.
        start +=1

_ = input("line 12")

#big_range = range(1000)
big_range = my_range(6)
_ = input("line 16")

print("big range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []
_ = input("line 21")
for val in big_range:
    _ = input("line 24 - inside loop")
    big_list.append(val)

print("big list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

