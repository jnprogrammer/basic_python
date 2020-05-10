parrot = "Norwgian Blue"

for character in parrot:
    print(character)


num = "9,223;373:036 854, 775; 807"
separators = ""

for char in num:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in num).split()

print([int(val) for val in values])