class Kettle(object):

    power_source = "electricity"
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
print(kenwood.power_source)
print(Kettle.__dict__)
print(hamham.__dict__)
print(kenwood.__dict__)

print("Switch power to Tesla batteries")
Kettle.power_source = "Tesla Batteries"

print(kenwood.power_source)
print(hamham.power_source)