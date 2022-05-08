import shutter_control
import sun_event
import getpass
from crontab import CronTab

working_dir = "/home/pi/"
python_dir = "/usr/bin/python3"

cron = CronTab(user=getpass.getuser())

shutter_control.shutter_close()
sunrise_time = sun_event.get_next_sunrise()
job = cron.new(command = python_dir + " " + working_dir + 'velux-integra-control/shutter_sunrise.py')
job.dom.on(sunrise_time.strftime('%d'))
job.month.on(sunrise_time.strftime('%m'))
job.hour.on(sunrise_time.strftime('%H'))
job.minute.on(sunrise_time.strftime('%M'))
cron.remove_all(command = working_dir + 'velux-integra-control/sunset_automation.py')
cron.write()
