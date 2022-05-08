import getpass
from crontab import CronTab

cron = CronTab(user=getpass.getuser())

cron.remove_all(command='/home/pi/velux/shutter_sunrise.py')
cron.remove_all(command='/home/pi/velux/shutter_sunset.py')
cron.write()
