entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("all: {}".format(any(entries)))

print("Iterable with a 'false' Value")
entries_with_zero = [1, 2, 0, 4, 6]

print("all: {}".format(all(entries_with_zero)))
print("all: {}".format(any(entries_with_zero)))