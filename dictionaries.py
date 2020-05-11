fruit = {"orange" : "A sweet orange, citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a small, sour citrus fruit",
         "grape" : "A sweet, small bunched fruit",
         "lime" : "A sour, green citrus fruit"}
#
# print(fruit)
#
# print(fruit["apple"])
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped and textured apple"
#
# print(fruit)
#
#
# fruit["pear"] = "Great fruit in hand"
#
# del fruit["grape"]
#
# print(fruit)
#
# fruit.clear()()
#
print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)