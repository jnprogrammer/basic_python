parrot = "Norwgian Blue"

for character in parrot:
    print(character)


num = input("Enter numbers using separators ")

separators = ""

for char in num:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in num).split()

print("Here is the total:{0} ".format(sum([int(val) for val in values])))