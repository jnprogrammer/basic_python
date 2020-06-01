#nested comprehensions

burgers = ["regular", "Veggy", "Spicy"]
toppings = ["Cheese\nTomatos\nMustard\nKetchup", "Pepper Jack Cheese\nTomatos\nHot Buffalo sauce\nSpicy Mustard", "cats", "Other . . ."]

meals = [(buger, toppings) for buger in burgers for topping in toppings]
print(meals)

print()


for burger in burgers:
    for topping in toppings:
        print((burger, topping))


