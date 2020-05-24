import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = '4nweflFIXBATMANjg@sdjhaf.com' WHERE contacts.name = 'Tom'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows upated".format(update_cursor.rowcount))
print("_" * 50)
print("Are connections the same: {}".format(update_cursor.connection == db))
print("_" * 50)

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("_" * 20)

db.close()