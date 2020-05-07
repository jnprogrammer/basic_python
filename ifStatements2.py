name = input("Enter your human name")
age = int(input("How old are you {0}? ".format(name)))

if age >= 18:
    print("You should be auto enrolled to vote by 18")
else:
    print("Look your not old enough but you know the deal!! come back in {0} years".format(18-age))


