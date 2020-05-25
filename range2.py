my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)

print(small_decimals.index(3))

odd = range(1,10000,2)
print(odd)

print(odd[985])


sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than one million:"))
if x in sevens:
    print("{} is divisible by seven".format(x))
else:
    print("{} is not divisible by seven".format(x))

print(small_decimals)
my_range = small_decimals[:2]
print(my_range)
print(my_range.index(4))