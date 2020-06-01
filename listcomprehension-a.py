print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Enter a number I'll square it"))

squares = [number ** 2 for number in numbers]

index_pos = numbers.index(number)

print(squares[index_pos])


inch_measurement = (3, 4, 7)

cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)



cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])
print(cm_measurement)