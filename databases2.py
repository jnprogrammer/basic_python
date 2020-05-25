import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "whatTHisand@that.com"
phone = 248982004
name = input("Enter the name of a user to find them")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.name = '{}'".format(new_email, name)
update_sql = "UPDATE contacts SET email = ? WHERE name = ?"

print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, name))
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