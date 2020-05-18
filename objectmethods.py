import datetime, pytz


class Account:
    """Simple banking account"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account made for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_bal()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_bal()
            self.transaction_list.append((Account._current_time(), -amount))

        else:
            print("Insufficient funds.")
            self.show_bal()

    def show_bal(self):
        print("Bal is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "Depositied"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    jim = Account("Jim", 0)
    jim.show_bal()

    jim.deposit(1428)
    jim.withdraw(420)
    jim.withdraw(48208)
    jim.deposit(344234)
    jim.withdraw(70400)
    jim.show_transactions()
