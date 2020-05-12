trini_foods = "Roti", "Stew Chicken", "Fried Bake", "Curry Chicken", "Aloo pie", "Salt Fish", "Tamarind chutney", "Doubles"

resturant = "The Roti Spot", "Josh", "Est. 2025", (
    (1, "Curry Chicken Roti", "$25"), (2, "Curry Goat Roti", "$30"), (3, "Curry Veggie Roti", "$20"))

with open("The Roti Spot menu.txt", 'w') as resturant_file:
    print(resturant, file=resturant_file)
print("*" * 64)


with open("The Roti Spot menu.txt", 'r') as resturant_file:
    contents = resturant_file.readline()

read_resturant = eval(contents)
print(read_resturant)
name, owner, year_est, menu = read_resturant

print(name)
print(owner)
print(year_est)