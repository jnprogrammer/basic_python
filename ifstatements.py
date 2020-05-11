name = input("Please enter your name")
age = int(input("How old are ya {0}?".format(name)))

print(age)

if age >= 18:
    print("You should be automatically registered to vote")
