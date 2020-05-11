shopping_list = ["milk", "spam", "pasta", "flour", "bananas", "channa", "mango", "chicken"]

item_to_find = "mango"
found_at = None

# # for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at index {}".format(found_at))
else:
    print("{} not found".format((item_to_find)))