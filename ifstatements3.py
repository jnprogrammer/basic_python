name = input("What's your name?  ")
age = int(input("How old are you? "))

if 18 <= age < 30:
    print("You got on Vacation some times")
elif age > 30:
    print("you should retire.")
else:
    print("Your just a kid, go enjoy it")