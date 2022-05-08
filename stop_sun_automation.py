import getpass
from crontab import CronTab

working_dir = "/home/pi/"
cron = CronTab(user=getpass.getuser())

cron.remove_all(command = working_dir + 'velux-integra-control/sunrise_automation.py')
cron.remove_all(command = working_dir + 'velux-integra-control/sunset_automation.py')
cron.write()
