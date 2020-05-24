import sqlite3

db = sqlite3.connect("contacts.sqlite")

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()