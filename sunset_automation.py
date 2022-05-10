import os
import sys
import getpass
from crontab import CronTab
import shutter_control
import sun_event

repo_dir = os.path.dirname(os.path.realpath(__file__))
cron = CronTab(user=getpass.getuser())

shutter_control.shutter_close()
sunrise_time = sun_event.get_next_sunrise()
job = cron.new(command = "python3 " + repo_dir + '/sunrise_automation.py')
job.dom.on(sunrise_time.strftime('%d'))
job.month.on(sunrise_time.strftime('%m'))
job.hour.on(sunrise_time.strftime('%H'))
job.minute.on(sunrise_time.strftime('%M'))
cron.remove_all(command = repo_dir + '/sunset_automation.py')
cron.write()
