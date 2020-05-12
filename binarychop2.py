low = 1
high = 1000

print("Think of a number between {} and {}".format(low, high))

input("Press ENTER to start")

guesses = 1

while low != high:
    #print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Do I guess higher or lower ? \n "
                     "Enter h or l, or c if guess is correct"
                     .format(guess).casefold())

    if high_low == "h":
        #guess higher, the low end of the range becomes 1 greater than the guess
        #pass
        low = guess + 1
    elif high_low == "l":
        #guess lower. the high end of the range becomes one less than the guess.
        #pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    #guesses = guesses + 1 augmented assignment better
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))