fruit = {"orange" : "A sweet orange, citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a small, sour citrus fruit",
         "grape" : "A sweet, small bunched fruit",
         "lime" : "A sour, green citrus fruit"}



print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)


for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)


print(dict(f_tuple))