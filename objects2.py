class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True



kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamham = Kettle("Ham-Ham", 34.99)

print(hamham.price)

print("Models: {} ${} , {} ${}".format(kenwood.make, kenwood.price, hamham.make, hamham.price))

print("Models: {0.make} = {0.price}, {1.make} {1.price}".format(kenwood, hamham))
print(hamham.on)
hamham.switch()
print(hamham.on)
hamham.switch()
print(hamham.on)

Kettle.switch(hamham)
print(hamham.on)

print("*" * 80)

hamham.power = 1.5
print(hamham.power)