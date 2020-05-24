import pickle

with open("restaurant.pickle", 'rb') as restaurant_pickled:
    restaurant_data = pickle.load(restaurant_pickled)

print(restaurant_data)

name, owner, year_opened, menu = restaurant_data

print(name)
print(owner)
print(year_opened)
for item in menu:
    menu_position, dish, price = item
    print(menu_position, dish, price)