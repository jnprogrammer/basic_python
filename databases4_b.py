class Account(object):

    def __init__(self, name: str, opening_balance: int = 100):
        self.name = name
        self._bal = opening_balance
        print("Account created for {}".format(self.name, end=''))
        self.show_bal()

    def deposit(self, amount: int) -> float:
        if amount > 100.0:
            self._bal += amount
            print("{:.2f} deposited".format(amount/100))
        return self._bal /100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._bal:
            self._bal -= amount
            print("{} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("Account has insufficient funds")
            return self._bal /100

    def show_bal(self):
        print("Your Account Balance is {:.2f}".format(self._bal /100))


if __name__ == '__main__':
    j = Account("J")
    j.deposit(400000)
    j.deposit(13476825)
    j.show_bal()
