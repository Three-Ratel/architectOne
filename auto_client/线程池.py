#!/usr/bin/python
# -*- coding:utf-8 -*-

from concurrent.futures  import ThreadPoolExecutor
import time

#创建了一个线程池  , 最多2个线程

def task(host=1):
    '''
    采集资产
    :return:
    '''
    time.sleep(2)
    print(host)

pool = ThreadPoolExecutor(20)

for i in range(1,101):
    hostname="c%s.com"%(i)
    #去线程池中申请一个线程去执行
    pool.submit(task,hostname)