import datetime, pytz


class Account:
    """Simple banking account"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance__ = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), self.__balance__))
        print("Account made for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance__ += amount
            self.show_bal()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance__:
            self.__balance__ -= amount
            self.show_bal()
            self._transaction_list.append((Account._current_time(), -amount))

        else:
            print("Insufficient funds.")
            self.show_bal()

    def show_bal(self):
        print("Bal is {}".format(self.__balance__))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    jim = Account("Jim", 0)

    jim.deposit(1428)
    jim.withdraw(420)
    jim.withdraw(48208)
    jim.deposit(344234)
    jim.withdraw(70400)
    jim.show_transactions()
    print("$" * 100)
    tank = Account("Tank", 7038443)
    tank.deposit(8400)
    tank.withdraw(200000)
    tank.show_transactions()
    tank.show_bal()
    print(tank.__dict__)
    tank._Account__balance = 40
    tank.show_bal()