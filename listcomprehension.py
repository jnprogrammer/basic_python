print(__file__)

numbers = [1, 2, 3, 4, 5, 6,]

number = int(input("Enter a number I'll square it"))

squares = []

for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])