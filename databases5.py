import sqlite3, datetime, pytz
#this is just an exercise file.
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):
    # utc_time = row[0]
    # local_time = pytz.utc.localize(utc_time).astimezone()
for row in db.execute("SELECT * FROM localhistory"):
    print(row)
    # print("{}\t{}".format(utc_time, local_time))
db.close()