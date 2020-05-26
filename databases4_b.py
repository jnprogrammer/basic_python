import datetime, sqlite3, pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           " amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")

class Account(object):

    @staticmethod
    def _current_time():
        #return pytz.utc.localize(datetime.datetime.utcnow())
        local_time = pytz.utc.localize(datetime.datetime.utcnow())
        return local_time.astimezone()

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

    def _save_update(self, amount):
        new_bal = self._bal + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_bal, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        db.commit()
        self._bal = new_bal

    def deposit(self, amount: int) -> float:
        if amount > 100.0:
            self._save_update(amount)
            print("{} has deposited {:.2f}".format(self.name, amount / 100))
        return self._bal / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._bal:
            self._save_update(-amount)
            # new_bal = self._bal - amount
            # withdrawal_time = Account._current_time(self)
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_bal, self.name))
            # db.execute("INSERT INTO history VALUES(?, ? ,?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            print("{} has withdrawn {:.2f}".format(self.name, amount / 100))
            return amount / 100
        else:
            print("{}, Your account has insufficient funds to withdraw {}".format(self.name, amount))
            return self._bal / 100

    def show_bal(self):
        print("\n{}'s Account Balance is {:.2f}".format(self.name, self._bal / 100))



if __name__ == '__main__':
    j = Account("J")
    j.deposit(400000)
    j.deposit(13476825)
    j.show_bal()
    print("*" * 45)
    ebb = Account("Ebb")
    ebb.withdraw(43853)
    print("*" * 45)
    tuvo = Account("TuVo")
    tuvo.deposit(424528)
    tuvo.withdraw(53553)
    print("*" * 45)
    ebb.deposit(424228)
    ebb.withdraw(30000)