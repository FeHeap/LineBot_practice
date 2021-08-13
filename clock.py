# -*- coding = utf-8 -*-
# @Time: 2021/8/14 上午 12:02
# @Software: PyCharm

from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
def scheduled_job():
    print('========== APScheduler CRON ==========')
    print('This job runs every mon-fri */30 min.')
    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON ==========')

    url = "https://fe-00-proto-type.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)

sched.start()