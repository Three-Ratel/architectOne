#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
离线脚本
"""
from deploy import create_app, db
from deploy import models

app = create_app()

with app.app_context():
    # obj = models.UserInfo(username='wupeiqi',password='123',nickname='武沛齐')
    #    db.session.add_all([
    #        models.Project(ti)
    #    ])
    # #   db.session.add()
    #    db.session.commit()
    #    db.session.remove()
    # ################## 数据初始化 ####################
    """
    1. 创建两个用户
    2. 创建一个项目
    3. 创建两个服务器
    4. 项目和服务器创建关系
    """
    user1 = models.UserInfo(username='wupeiqi', password='123', nickname='武沛齐')
    user2 = models.UserInfo(username='hhw', password='123', nickname='黄宏伟')

    pro1 = models.Project(title='公司官网', name='web1', repository='https://github.com/WuPeiqi/dbhot.git')
    pro1.hosts = [mode ls.Host(hostname='c1.com', port=80), models.Host(hostname='c2.com', port=80)]

    db.session.add_all([
        user1,
        user2,
        pro1
    ])
    db.session.commit()
    db.session.remove()
