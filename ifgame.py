answer = 7

guess = int(input("Please guess number between 1 and 1o: "))

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("you got it first time")

