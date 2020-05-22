class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
        self._attack = 5

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @property
    def lives(self, lives):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            self._lives = 0

    @property
    def level(self, level):
        return self._level

    @level.setter
    def level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    #lives = property(_get_lives, _set_lives)
    #level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level; {0.level}, Attack Power: {0.attack} Score {0.score}".format(self)
