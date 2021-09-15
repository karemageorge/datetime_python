import datetime
import pytz

d = datetime.date(2016, 7, 24) # prints out the date
print(d)

tday = datetime.date.today() # prints out todays date
print(tday)

tday = datetime.date.today() # prints out todays year
print(tday.year)

tday = datetime.date.today() # prints out todays day
print(tday.day)


# note the difference between ISOweekday and weekday 
# for weekday monday is 0 and sunday 6
# for iso weekday monday is 1 and sunday 7
tday = datetime.date.today() # prints out todays weekday returns 2 = wednesday
print(tday.weekday())

tday = datetime.date.today() # prints out todays weed day prints 3 = wednesday
print(tday.isoweekday())

# time deltas - difference between two dates or times
tdelta = datetime.timedelta(days=7) # can be days hours 
print(tday+tdelta) # returns the date of the day seven days in the future 

 
 # DATETIME.TIME (HRS, MINS, SECS, MICROSECS)
t = datetime.time(9, 30, 45, 10000)
print(t)

#DATETIME.DATETIME (YEAR, MONTH, DAY, hrs, mins, secs)
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)
tdelta = datetime.timedelta(hours=12)
print(dt+tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


# install pytz for timezones

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC) # the last part makes it timezone aware
print(dt) # returns 2016-07-27 12:30:45+00:00

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('Africa/Nairobi'))
print(dt_mtn)

# check pytz timezones
for tz in pytz.all_timezones:
    print(tz)


# https://www.youtube.com/watch?v=eirjjyP2qcQ



# print in a certain format code

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
#strftime - converts datetime to string
print(dt_mtn.strftime('%B %d, %Y')) # check the formats in the documentation

# strptime - converts a string into a datetime
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
