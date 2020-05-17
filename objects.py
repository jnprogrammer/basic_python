class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamham = Kettle("Ham-Ham", 34.99)

print(hamham.price)

print("Models: {} ${} , {} ${}".format(kenwood.make, kenwood.price, hamham.make, hamham.price))