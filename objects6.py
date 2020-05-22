class Duck(object):

    def walk(self):
        print("Waddle waddle waddle")

    def swim(self):
        print("Come on in, water is nice")

    def quack(self):
        print("Quack Quack Quack")


class Penguin(object):

    def walk(self):
        print("Waddle waddle slide")

    def swim(self):
        print("Come on in, water is ice")

    def quack(self):
        print("Squack Wacks")


def test_duck(duck):
    duck.walk()
    duck.quack()
    duck.swim()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    pear = Penguin()
    test_duck(pear)
