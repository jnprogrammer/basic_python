import shelve

#with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['apple'] = "1 fruit"
fruit['lemon'] = "2 fruit"
fruit['grape'] = "3 fruit"
fruit['lime'] = "4 fruit"
fruit['orange'] = "5 fruit"

# print(fruit["apple"])
# print(fruit["lime"])
#
# fruit["apple"] = "Great in a pie"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
#
# while True:
#     shelf_key = input("Enter a fruit: ")
#     if shelf_key == "quit":
#         break
#     if shelf_key in fruit:
#         description = fruit[shelf_key]
#         print(description)
#     else:
#         print("We don't have " + shelf_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())
fruit.close()
