import random

highest = 10

answer = random.randint(1, highest)
#print(answer) #TODO: Remove after testing
#guess = int(input("Please guess number between 1 and 10: "))
guess = 0

while guess != answer:
    guess = int(input("Please guess number between 1 and 10: "))
    if guess == answer:
        print("you got it right !!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("you did it !")
        # else:
        #     print("Sorry you didn't get it")
        #     continue