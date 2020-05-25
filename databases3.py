import sqlite3

con = sqlite3.connect("contacts.sqlite")

for row in con.execute("SELECT * FROM sqlite_master"):
    print(row)

con.close()