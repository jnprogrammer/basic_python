import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australian/Adelaide",
                   '4': "Europse/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("The local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("The local time in UTC {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
