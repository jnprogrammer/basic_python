shopping_list = ["milk", "spam", "pasta", "flour", "bananas", "channa", "mango", "chicken"]

for item in shopping_list:
    if item == "spam":
        print("Don't Buy {}".format(item))
        break
    print("Buy " + item)
