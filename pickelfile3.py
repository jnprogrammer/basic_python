import pickle

restaurant = "The Roti Spot", "Josh", "Est. 2025", (
    (1, "Curry Chicken Roti", "$25"), (2, "Curry Goat Roti", "$30"), (3, "Curry Veggie Roti", "$20"), (4, "Surrel Drink", "$5"))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("restaurant.pickle", 'wb') as pickle_file:
    pickle.dump(restaurant, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=0)

with open("restaurant.pickle", 'rb') as restaurant_pickled:
    restaurant_data = pickle.load(restaurant_pickled)
    even_list = pickle.load(restaurant_pickled)
    odd_list = pickle.load(restaurant_pickled)
    x = pickle.load(restaurant_pickled)

print(restaurant_data)

name, owner, year_opened, menu = restaurant_data

print(name)
print(owner)
print(year_opened)
for item in menu:
    menu_position, dish, price = item
    print(menu_position, dish, price)

print('=' * 40)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(x)