# print("=" *80)
# even = set(range(0, 40, 2))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print('=' * 80)
#
#
# print(even)
# print(squares)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# # print("^" * 20)
# # print(sorted(even))
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print((squares.symmetric_difference(even)))

#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error, does nothing . . .!
# print(squares)
#
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")
#
# print("=" *80)
# even = set(range(0, 40, 2))
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print('=' * 80)
#
#
# print(even)
# print(squares)
#
# if squares.issubset(even):
#     print("Squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))

print(even)
even.add(3)

