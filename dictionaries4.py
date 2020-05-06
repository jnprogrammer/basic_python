fruit = {"orange" : "A sweet orange, citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a small, sour citrus fruit",
         "grape" : "A sweet, small bunched fruit",
         "lime" : "A sour, green citrus fruit"}

print(fruit)

veg = {"Cabbage" : "Great with corn beef",
       "Sprouts": "mmmmm, lovely",
       "spinach" : "So yummy on anything!!"}

print(veg)

veg.update(fruit)
print(veg)
print( " %% " * 50)
fruit.update(veg)

print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)

print(nice_and_nasty)
print(veg)
print(fruit)