#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

def warpper(func):
    # @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@warpper
def index():
    print('函数内容')



print(index.__name__)