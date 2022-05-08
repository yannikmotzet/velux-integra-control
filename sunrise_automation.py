import shutter_control
import sun_event
import getpass
from crontab import CronTab

working_dir = "/home/pi/"
python_dir = "/usr/bin/python3"

cron = CronTab(user=getpass.getuser())

shutter_control.shutter_open()
sunset_time = sun_event.get_next_sunset()
job = cron.new(command = python_dir + " " + working_dir + 'velux-integra-control/shutter_sunset.py')
job.dom.on(sunset_time.strftime('%d'))
job.month.on(sunset_time.strftime('%m'))
job.hour.on(sunset_time.strftime('%H'))
job.minute.on(sunset_time.strftime('%M'))
cron.remove_all(command=working_dir + 'velux-integra-control/sunrise_automation.py')
cron.write()
