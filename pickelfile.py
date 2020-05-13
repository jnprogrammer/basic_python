import pickle

restaurant = "The Roti Spot", "Josh", "Est. 2025", (
    (1, "Curry Chicken Roti", "$25"), (2, "Curry Goat Roti", "$30"), (3, "Curry Veggie Roti", "$20"), (4, "Surrel Drink", "$5"))


with open("restaurant.pickle", 'wb') as pickle_file:
    pickle.dump(restaurant, pickle_file)

