import pytz
import datetime

country = 'Europe/Moscow'

timezone_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=timezone_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))