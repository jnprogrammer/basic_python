class Account(object):

    def __init__(self, name: str, opening_balance: float = 100.0):
        self.name = name
        self._bal = opening_balance
        print("Account created for {}".format(self.name, end=''))
        self.show_bal()

    def deposit(self, amount: float) -> float:
        if amount > 100.0:
            self._bal += amount
            print("{} deposited".format(amount))
        return self._bal

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._bal:
            self._bal -= amount
            print("{} withdrawn".format(amount))
            return amount
        else:
            print("Account has insufficient funds")
            return self._bal

    def show_bal(self):
        print("Your Account Balance is {}".format(self._bal))


if __name__ == '__main__':
    j = Account("J")
    j.deposit(4000)
    j.deposit(13425.24)
    j.show_bal()
