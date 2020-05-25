from decimal import *


class Account(object):
    _qb = Decimal('0.00')

    def __init__(self, name: str, opening_balance: float = 100.0):
        self.name = name
        self._bal = Decimal(opening_balance).quantize(Account._qb)
        print("Account created for {}".format(self.name, end=''))
        self.show_bal()

    def deposit(self, amount: float) -> float:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            self._bal += decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._bal

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._bal:
            self._bal -= decimal_amount
            print("{} withdrawn".format(decimal_amount))
            return decimal_amount
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
