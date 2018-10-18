#!/usr/bin/python
# -*- coding:utf-8 -*-
import traceback

def f1():
    int('asdf')
    return 123

def run():
    try:
        ret=f1()
        print(ret)
    except Exception as e:
        msg=traceback.format_exc()
        print('错误的堆栈信息')


run()
