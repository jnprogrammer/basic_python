import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            print("CTRL -  D")
            sys.exit(1)



first_number = getint("Please enter 1st number")
second_number = getint("Enter second number that will be used in division")


try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("CAn't divided by zero")
    sys.exit(2)