import datetime
import pytz
from suntime import Sun, SunTimeException
from dateutil import tz
import time

latitude = 39.521322
longitude = 2.776954

last_sr_file = ".last_sunrise"
last_ss_file = ".last_sunset"

# write utc time to file
def write_sun_event(file, time):
    file = open(file, mode='w')
    file.write(time)

# read utc time from file and return next event in local time
def read_sun_event(file):
    with open(file) as f:
        contents = f.readlines()
    sun_event_time_utc = datetime.datetime.strptime(datetime.date.today().strftime('%d.%m.%Y-') + contents[-1] + ' UTC', '%d.%m.%Y-%H:%M %Z')
    # make timezone aware
    sun_event_time_utc = pytz.utc.localize(sun_event_time_utc)
    sun_event_time_local = sun_event_time_utc.astimezone(tz.tzlocal())
    if datetime.datetime.now(tz.tzlocal()) < sun_event_time_local:
        return sun_event_time_local
    else:
        return sun_event_time_local + datetime.timedelta(days=1)

def get_next_sunrise():
    sun = Sun(latitude, longitude)
    try:
        today_sr_utc = sun.get_sunrise_time()
        today_sr_local = today_sr_utc.astimezone(tz.tzlocal())
    # in case of exception use time of last sunrise
    except SunTimeException as e:
        return read_sun_event(last_sr_file)
    # check if next event is today or tomorrow
    if datetime.datetime.now(tz.tzlocal()) < today_sr_local:
        write_sun_event(last_sr_file, today_sr_utc.strftime('%H:%M'))
        return today_sr_local
    else:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow_sr_utc = sun.get_sunrise_time(tomorrow)
        tomorrow_sr_local = tomorrow_sr_utc.astimezone(tz.tzlocal())
        write_sun_event(last_sr_file, tomorrow_sr_utc.strftime('%H:%M'))
        return tomorrow_sr_local

def get_next_sunset():
    sun = Sun(latitude, longitude)
    try:
        today_ss_utc = sun.get_sunset_time()
        today_ss_local = today_ss_utc.astimezone(tz.tzlocal())
    # in case of exception use time of last sunset
    except:
        return read_sun_event(last_ss_file)
    # check if next event is today or tomorrow
    if datetime.datetime.now(tz.tzlocal()) < today_ss_local:
        write_sun_event(last_ss_file, today_ss_utc.strftime('%H:%M'))
        return today_ss_local
    else:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow_ss_utc = sun.get_sunset_time(tomorrow)
        tomorrow_ss_local = tomorrow_ss_utc.astimezone(tz.tzlocal())
        write_sun_event(last_ss_file, tomorrow_ss_utc.strftime('%H:%M'))
        return tomorrow_ss_local
