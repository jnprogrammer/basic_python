from objects5 import Player

tim = Player("Tim")

print(tim.name)
print(tim)
tim.lives -= 1
print(tim)

tim.level += 50
print(tim)

tim.level += 76
print(tim)

tim.level -= 43
print(tim)

tim.score = 43800
print(tim)