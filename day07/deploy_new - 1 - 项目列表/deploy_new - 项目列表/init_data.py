#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
离线脚本
"""
from deploy import create_app,db
from deploy import models
app = create_app()

with app.app_context():
    # 1. 增加
    # obj = models.UserInfo(username='wupeiqi',password='123',nickname='武沛齐')
    # db.session.add(obj)
    # db.session.commit()
    # 2. 批量增加
    # db.session.add_all([
    #     models.UserInfo(username='wupeiqi', password='123', nickname='武沛齐'),
    #     models.UserInfo(username='hhw', password='123', nickname='黄宏伟'),
    # ])
    # db.session.commit()
    # db.session.remove()

    # result = db.session.query(models.UserInfo).all()
    # db.session.remove()

    # 3. 添加用户和主机
    # db.session.add_all([
    #     # models.UserInfo(username='wupeiqi', password='123', nickname='武沛齐'),
    #     # models.UserInfo(username='hhw', password='123', nickname='黄宏伟'),
    #     models.Host(hostname='c1.com',port=80),
    #     models.Host(hostname='c2.com',port=80),
    #     models.Project(title='公司官网',name='web1',repository='https://github.com/WuPeiqi/dbhot.git'),
    #     models.Project(title='公司后台',name='web2',repository='https://github.com/WuPeiqi/dbhot.git')
    # ])
    # db.session.commit()
    # db.session.remove()

    # db.session.add_all([
    #     models.Project2Host(project_id=1,host_id=1),
    #     models.Project2Host(project_id=1,host_id=2),
    #     models.Project2Host(project_id=2,host_id=2),
    #     models.Project2Host(project_id=2,host_id=1),
    # ])
    # db.session.commit()
    # db.session.remove()
    # 任务：创建两个服务器，创建一个项目，项目和服务器创建关系。
    # 复杂方式
    # obj1 = models.Host(hostname='c4.com',port=80)
    # obj2 = models.Host(hostname='c5.com',port=80)
    # obj3 = models.Project(title='运维平台',name='devops',repository='asdfasdf')
    # db.session.add(obj1)
    # db.session.add(obj2)
    # db.session.add(obj3)
    # db.session.commit()
    #
    # db.session.add_all([
    #     models.Project2Host(host_id=obj1.id,project_id=obj3.id),
    #     models.Project2Host(host_id=obj2.id,project_id=obj3.id),
    # ])
    # db.session.commit()
    # 简单访问

    """
    1. 添加项目
    2. 添加两个主机
    3. 项目和主机的关系表中添加一个两个
    """
    # obj1 = models.Project(title='运维平台',name='devops111',repository='asdfasdf')
    # obj1.hosts = [models.Host(hostname='c10.com',port=80),models.Host(hostname='c11.com',port=80)]
    # db.session.add(obj1)
    # db.session.commit()
    # db.session.remove()

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
    pro1.hosts = [models.Host(hostname='c1.com',port=80),models.Host(hostname='c2.com',port=80)]

    db.session.add_all([
        user1,
        user2,
        pro1
    ])
    db.session.commit()
    db.session.remove()




