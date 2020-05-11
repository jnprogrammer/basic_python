shopping_list = ["milk", "spam", "pasta", "flour", "bananas", "channa", "mango", "chicken"]

item_to_find = "spam"
found_at = None

# for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Item found at index {}".format(found_at))