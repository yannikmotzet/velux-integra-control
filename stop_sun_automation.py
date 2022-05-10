import os
import sys
import getpass
from crontab import CronTab

repo_dir = os.path.dirname(os.path.realpath(__file__))
cron = CronTab(user=getpass.getuser())

cron.remove_all(command = repo_dir + '/sunrise_automation.py')
cron.remove_all(command = repo_dir + '/sunset_automation.py')
cron.write()
