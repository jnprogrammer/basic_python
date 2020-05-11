for i in range(10, 0, -2):
    print("i is now {}".format(i))

name = input("What's your name?  ")
age = int(input("How old are you? "))

if age in range(16,66):
    print("You got on Vacation some times")
elif age > 30:
    print("you should retire.")
else:
    print("Your just a kid, go enjoy it")