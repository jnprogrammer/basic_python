import shelve

# trini_foods = ["Roti", "Stew Chicken", "Fried Bake", "Curry Chicken", "Aloo pie", "Salt Fish", "Tamarind chutney", "Doubles"]
#
# american_foods = ["Burgers", "Pizza", "Apple Pie", "Tex-mex", "Southern BBQ", "Deep Dish Pizza", "Clam Chowder", "Lobster rolls"]
#
# fast_foods = ["Mcdonalds", "Burger King", "Chick-fila", "dominos", "Pizza hut", "five guys"]
soup = ["Ramen noodles"]

with shelve.open('foods', writeback=True) as foods:
    # foods["trini_foods"] = trini_foods
    # foods["fast_foods"] = fast_foods
    # foods["american_foods"] = american_foods
    # foods["soup"] = soup
    # temp_foods = foods["american_foods"]
    # temp_foods.append("peanut butter")
    # foods["american_foods"] = temp_foods
    #
    # temp_foods = foods["trini_foods"]
    # temp_foods.append("Pholourie")
    # foods["trini_foods"] = temp_foods
    # foods["soup"].append("miso")
    foods["soup"] = soup
    # foods.sync()  Don't use sync, use the method above.
    soup.append("apple cream pasta")




    for snack in foods:
        print(snack, foods[snack])

