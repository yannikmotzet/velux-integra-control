import shutter_control
import sun_event
import datetime
import getpass
from crontab import CronTab

working_dir = "/home/pi/"
python_dir = "/usr/bin/python3"

cron = CronTab(user=getpass.getuser())

sunrise_time = sun_event.get_next_sunrise()
sunset_time = sun_event.get_next_sunset()

if sunrise_time < sunset_time:
    job = cron.new(command = python_dir + " " + working_dir + 'velux-integra-control/sunrise_automation.py')
    job.dom.on(sunrise_time.strftime('%d'))
    job.month.on(sunrise_time.strftime('%m'))
    job.hour.on(sunrise_time.strftime('%H'))
    job.minute.on(sunrise_time.strftime('%M'))
    #cron.remove_all(command='/home/pi/velux/shutter_sunset.py')
    cron.write()

else:
    job = cron.new(command = python_dir + " " + working_dir + 'velux-integra-control/sunset_automation.py')
    job.dom.on(sunset_time.strftime('%d'))
    job.month.on(sunset_time.strftime('%m'))
    job.hour.on(sunset_time.strftime('%H'))
    job.minute.on(sunset_time.strftime('%M'))
    #cron.remove_all(command='/home/pi/velux/shutter_sunrise.py')
    cron.write()


