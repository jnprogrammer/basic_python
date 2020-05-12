print("Please choose your option form the list below:")
stuff = ["1:\tLearn Python", "2:\tLearn Java", "3:\tLearn Go", "4:\tLearn JavaScript", "5:\tLearn c++", "0:\t Exit"]

for i in range(len(stuff)):
    print(stuff[i])

while True:
    choice = input("\nChoose an activity . . just not Java\n")
    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}\n".format(choice))
        for i in range(len(stuff)):
            print(stuff[i])
    else:
        print("Pick again")
        for i in range(len(stuff)):
            print(stuff[i])
