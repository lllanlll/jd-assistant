# -*- coding:utf-8 -*-
import time
from datetime import datetime
from timer import Timer
from log import logger

buy_time = "2021-03-25 19:57:00.000"
t = Timer(buy_time=buy_time)

buy_time = datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S.%f")
sleep_interval = 0.01

def start(self):
    logger.info('正在等待到达设定时间:%s' % self.buy_time)
    now_time = datetime.now
    while True:
        if now_time() >= self.buy_time:
            logger.info('时间到达，开始执行……')
            break
        else:
            time.sleep(self.sleep_interval)

t.start()
