import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('TEST DATA', 010101011, 'dont@fakemail.com')")
db.execute("INSERT INTO contacts VALUES('Blankets', 5555555, 'bankers@fakemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())

for name, phone, email in cursor:
    print(name, phone, email)

cursor.close()
db.commit()
db.close()
