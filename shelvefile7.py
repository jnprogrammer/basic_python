import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "lettuce", "tomato", "bread"],
                     "breans_on_toast": ["beans", "bread"],
                     "scrambles eggs": ["eggs", "butter", "milk"],
                     "ramen": ["ramen", "left over chicken", "left over veggies"]}

books["tesla cars"] = {"CyberTruck": ["804km Battery Range", "Tri motor"],
                        "Model Y": ["508km Battery Range", "Duel motor"]}


print(books["recipes"])
print(books["recipes"]["scrambles eggs"])

print(books["tesla cars"]["CyberTruck"])

books.close()

