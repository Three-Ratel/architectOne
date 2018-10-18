#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
import time


def agent():
    '''
    获取当前服务器的资产信息并提交给api
    :return:
    '''
    # 1.获取资产信息:硬盘 网卡 内存(操作系统判断)
    disk = subprocess.getoutput('ls')
    info = {'hostname': 'c1', 'memory': disk}
    url = "http://127.0.0.1:8000/api/asset/"
    # 2.错误处理 堆栈错误

    # 3.唯一标记问题
    # OpenStack下存在虚拟机和宿主机sn重名   (1.需要: 系统+调用OpenStackapi 2.主机名唯一标志)
    r1 = requests.post(
        url=url,
        # 方式一
        data=json.dumps(info).encode('utf-8'),

        # 方式二 不能有中文,json默认不是utf8编码
        # json=info,

        # 附:
        # data={'hostname':'c1','memory':'5G'} #此格式post和body都可以接收到数据
    )
    print(r1.text)


def task(host):
    # 循环主机列表,对每一台主机调用saltstack.paramiko.ssh等远程执行命令
    info = {'hostname': host, 'disk': '1111'}


    url = "http://127.0.0.1:8000/api/asset/"
    r1 = requests.post(
        url=url,
        data=json.dumps(info).encode('utf-8'),
    )
    print(r1.text)


def ssh():
    # 1.获取未采集服务器列表
    r1 = requests.get("http://127.0.0.1:8000/api/asset/")
    print(r1.text, type(r1.text), r1.content, type(r1.content), r1.json(), type(r1.json()))
    host_list = r1.json()
    print(host_list)

    #提交到线程池
    pool=ThreadPoolExecutor(10)
    for host in host_list:
        pool.submit(task,host)

ssh()
