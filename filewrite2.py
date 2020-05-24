trini_foods = "Roti", "Stew Chicken", "Fried Bake", "Curry Chicken", "Aloo pie", "Salt Fish", "Tamarind chutney", "Doubles"

restaurant = "The Roti Spot", "Josh", "Est. 2025", (
    (1, "Curry Chicken Roti", "$25"), (2, "Curry Goat Roti", "$30"), (3, "Curry Veggie Roti", "$20"))

with open("The Roti Spot menu.txt", 'w') as restaurant_file:
    print(restaurant, file=restaurant_file)
print("*" * 64)


with open("The Roti Spot menu.txt", 'r') as restaurant_file:
    contents = restaurant_file.readline()

read_restaurant = eval(contents)
print(read_restaurant)
name, owner, year_est, menu = read_restaurant

print(name)
print(owner)
print(year_est)