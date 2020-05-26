import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=3, attack=2):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._attack = attack
        self._alive = True

    def check_life(self, _alive):
        return self._alive

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life ! {0._lives} left".format(self))
            else:
                print("{0._name} is dead?".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points} Attack Points: {0._attack}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=710, hit_points=420)
        super().__init__(name=name, lives=710, hit_points=420, attack=420)

    def lariat(self):
        print("RaGE Larraiat!! !! {0._name} Attacks with a ferocious Lariat".format(self))


class Ogar(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=2, hit_points=42, attack=3)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("{0._name} Dodges the attack !!".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):

        if not self.dodge():
            super().take_damage(damage=damage)
