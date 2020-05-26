import sqlite3

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           " amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    def __init__(self, name: str, opening_balance: int = 10000):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._bal = row
            print("Retrieved Recorded for {}".format(self.name), end='')
        else:
            self.name = name
            self._bal = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("\nAccount created for {}".format(self.name), end='')

        self.show_bal()

    def deposit(self, amount: int) -> float:
        if amount > 100.0:
            self._bal += amount
            print("{:.2f} deposited".format(amount / 100))
        return self._bal / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._bal:
            self._bal -= amount
            print("{} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("Account has insufficient funds")
            return self._bal / 100

    def show_bal(self):
        print("\nYour Account Balance is {:.2f}".format(self._bal / 100))


if __name__ == '__main__':
    j = Account("J")
    j.deposit(400000)
    j.deposit(13476825)
    j.show_bal()
    print("*" * 45)
    ebb = Account("Ebb")
    ebb.show_bal()