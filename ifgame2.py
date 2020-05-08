answer = 7
guess = int(input("Please guess number between 1 and 10: "))

if guess == answer:
    print("you got it right !!")
else:
    if guess < answer:
        print("Please guess higher, last try")
    else:
        print("Please guess lower, last try")
    guess = int(input())
    if guess == answer:
        print("you did it !")
    else:
        print("Sorry you didn't get it.")