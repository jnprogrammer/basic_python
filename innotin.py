# parrot = "Norwgian Blue"
#
# letter = input("Enter a char: ")
#
# if letter in parrot:
#     print("{} is in {}".format(letter,parrot))
# else:
#     print("These letters dont match")

activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

