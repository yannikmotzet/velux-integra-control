import os
import sys
import datetime
import getpass
from crontab import CronTab
import shutter_control
import sun_event

repo_dir = os.path.dirname(os.path.realpath(__file__))
cron = CronTab(user=getpass.getuser())

sunrise_time = sun_event.get_next_sunrise()
sunset_time = sun_event.get_next_sunset()

if sunrise_time < sunset_time:
    job = cron.new(command = "python3 " + repo_dir + '/sunrise_automation.py')
    job.dom.on(sunrise_time.strftime('%d'))
    job.month.on(sunrise_time.strftime('%m'))
    job.hour.on(sunrise_time.strftime('%H'))
    job.minute.on(sunrise_time.strftime('%M'))
    cron.remove_all(command = repo_dir + '/sunset_automation.py')
    cron.write()

else:
    job = cron.new(command = "python3 " + repo_dir + '/sunset_automation.py')
    job.dom.on(sunset_time.strftime('%d'))
    job.month.on(sunset_time.strftime('%m'))
    job.hour.on(sunset_time.strftime('%H'))
    job.minute.on(sunset_time.strftime('%M'))
    cron.remove_all(command = repo_dir + '/sunrise_automation.py')
    cron.write()


