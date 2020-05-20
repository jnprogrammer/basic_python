from objects5 import Player
from objects5_b import Enemy, Troll

tim = Player("Tim")
monster = Enemy("Big Monster", 12, 42)

print(monster)

cool_troll = Troll("Cool Troll", 18, 23)
print("The cool Troll stats - {}".format(cool_troll))

time_troll = Troll("Time Troll", 18, 420)
print(time_troll)