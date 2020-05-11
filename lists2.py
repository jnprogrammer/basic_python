shopping_list = ["milk", "pasta", "flour", "bananas", "channa", "mango", "spam"]

# for item in shopping_list:
#     if item !="spam" :
#         print("Buy " + item)


for item in shopping_list:
    if item == "spam":
        print("Don't Buy {}".format(item))
        continue
    print("Buy " + item)