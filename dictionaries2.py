fruit = {"orange" : "A sweet orange, citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a small, sour citrus fruit",
         "grape" : "A sweet, small bunched fruit",
         "lime" : "A sour, green citrus fruit"}



print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#
#     print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we don't have a " + dict_key)


print(fruit)

ordered_key = sorted(list(fruit.keys()))
#ordered_key.sort()
# for f in ordered_key:
#     print(f + " - " + fruit[f])


for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])


for val in fruit.values():
    print(val)

print('-' * 50)

for key in fruit:
    print(fruit[key])


fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "Great on pizza !!"
print(fruit_keys)
