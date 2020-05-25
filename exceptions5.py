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

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle waddle slide")

    def swim(self):
        print("Come on in, water is ice")

    def quack(self):
        print("Squack Wacks")

    def aviate(self):
        print("I used science and built a flying device")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)  # the python way on checking if an object can perform an desired action

        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Can't add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("TEST!! migrate exception handel")  # TODO: remove this test code
            except AttributeError as e:
                print("This can't fly")
                problem = e
        if problem:
            raise problem
