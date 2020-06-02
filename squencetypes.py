computer_parts = ["cpu", "gpu", "Memory", "SSD", "PSU", "Case", "Mother board", "GPU", ]


for part in computer_parts:
    print(part)


result = True
a_result = result
print(id(result))
print(id(a_result))

a = b = c= d =e =f = computer_parts

print("add Thermal past")
computer_parts.append("thermal past")

print(a)
print(id(a))


for index, character in enumerate("abcdefg"):
    print(index, character)