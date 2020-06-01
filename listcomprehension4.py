#nested comprehensions

burgers = ["regular", "Veggy", "wHO DID THIS !?!?"]
toppings = ["Cheese\nTomatos\nMustard\nKetchup", "Pepper Jack Cheese\nTomatos\nHot Buffalo sauce\nSpicy Mustard", "cats", "Other . . ."]

meals = [(buger, toppings) for buger in burgers for topping in toppings]
# print(meals)

print()


# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))


for meals in [(buger, toppings) for buger in burgers for topping in toppings]:
    print(meals)

for meals in [(burger, toppings) for topping in toppings for burger in burgers]:
    print(meals)

