class Account:
    """Simple banking account"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account made for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_bal()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_bal()
        else:
            print("Insufficient funds.")
            self.show_bal()

    def show_bal(self):
        print("Bal is {}".format(self.balance))


if __name__ == '__main__':
    jim = Account("Jim", 0)
    jim.show_bal()

    jim.deposit(1428)
    jim.withdraw(420)
    jim.withdraw(48208)