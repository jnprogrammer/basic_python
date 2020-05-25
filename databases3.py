import sqlite3

con = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to look up")

for row in con.execute("SELECT * FROM contacts WHERE name LIKE ?", (name, )):
    print(row)

con.close()



#
# for row in con.execute("SELECT * FROM sqlite_master"):
#     print(row)