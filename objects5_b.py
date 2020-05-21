class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=3, attack=2):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.attack = attack
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life ! {0.lives} left".format(self))
            else:
                print("{0.name} is dead?".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points} Attack Points: {0.attack}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        #super(Troll, self).__init__(name=name, lives=710, hit_points=420)
        super().__init__(name=name, lives=710, hit_points=420, attack=420)

    def lariat(self):
        print("RaGE Larraiat!! !! {0.name} Attacks with a ferocious Lariat".format(self))

class Ogar(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=2, hit_points=42, attack=3)