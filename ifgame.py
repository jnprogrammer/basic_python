answer = 7

guess = int(input("Please guess number between 1 and 10: "))


if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("You did it")
    else:
        print("You didn't get it in two tries")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You did it")
    else:
        print("You didn't get it in two tries")
elif guess > answer:
    print("you got it first time")

