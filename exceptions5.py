class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("I'm Flying. This is fun")
        elif self.ratio == 1:
            print("This is heavy but I'm flying")
        else:
            print("I'm to heavy to fly")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle waddle waddle")

    def swim(self):
        print("Come on in, water is nice")

    def quack(self):
        print("Quack Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle waddle slide")

    def swim(self):
        print("Come on in, water is ice")

    def quack(self):
        print("Squack Wacks")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        self.flock.append(duck)

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("This can't fly")
        if problem:
            raise problem



