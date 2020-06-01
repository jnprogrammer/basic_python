menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []

for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
print(meals)


meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(meals)

other_meals = [meal  for meal in menu if "spam" in meal or "egg" in meal if not ("bacon" in meal and "sausage" in meal)]

print(other_meals)