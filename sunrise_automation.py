import os
import getpass
from crontab import CronTab
import shutter_control
import sun_event

working_dir = os.getenv('VELUX_CONTROL_PATH')
cron = CronTab(user=getpass.getuser())

shutter_control.shutter_open()
sunset_time = sun_event.get_next_sunset()
job = cron.new(command = "python3 " + working_dir + 'velux-integra-control/sunset_automation.py')
job.dom.on(sunset_time.strftime('%d'))
job.month.on(sunset_time.strftime('%m'))
job.hour.on(sunset_time.strftime('%H'))
job.minute.on(sunset_time.strftime('%M'))
cron.remove_all(command = working_dir + 'velux-integra-control/sunrise_automation.py')
cron.write()
