from objects5 import Player
from objects5_b import Enemy, Troll, Ogar

tim = Player("Tim")
big_monster = Troll("Big Monster")

print(big_monster)

cool_troll = Troll("Cool Troll")
print(cool_troll)

time_troll = Troll("Time Troll")
print(time_troll)


time_troll.lariat()

blarg = Ogar("Bancan")
print(blarg)

blarg.take_damage(40)

print(blarg)

while blarg.alive:
    blarg.take_damage(3)
