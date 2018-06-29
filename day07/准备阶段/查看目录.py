#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

for li in os.listdir('E:\code\m1\day07\准备阶段'):
    # print(li)
    pass
for base,folder,files in os.walk('E:\code\m1\day07\准备阶段'):
    for item in files:
        file_path=os.path.join(base,item)
        print(file_path)