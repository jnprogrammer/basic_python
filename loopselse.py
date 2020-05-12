numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        print("Those numbers are not valid!!")
        break
else: # else in for loops only run a block if there isn't a break before it in the for loop
    print("All those numbers are fine")