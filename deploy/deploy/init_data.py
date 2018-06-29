#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploy import create_app, db
from deploy import models

app = create_app()

with app.app_context():
    # obj=models.UserInfo(username='wuxp',password='123',nickname='xp')
    # db.session.add(obj)
    # db.session.commit()

    # 批量增加
    # db.session.add_all(
    # [
    #     models.UserInfo(username='wuxp',password='123',nickname='xp'),
    #     models.UserInfo(username='hw', password='123', nickname='hw'),
    # ]
    # )
    # db.session.commit()
    # db.session.remove()

    # result = db.session.query(models.UserInfo).all()
    # print(result)
    # db.session.remove()

    # 添加用户和主机
    # db.session.add_all(
    #     [
    #         models.UserInfo(username='wuxp', password='123', nickname='xp'),
    #         models.UserInfo(username='hw', password='123', nickname='hw'),
    #         models.Host(hostname='c1.com', port=80),
    #         models.Host(hostname='c2.com', port=80),
    #         models.Project(title='公司官网', name='web1', repository='https://github.com/WuPeiqi/dbhot.git'),
    #         models.Project(title='公司后台', name='web2', repository='https://github.com/WuPeiqi/dbhot.git')
    #     ]
    # )
    # db.session.commit()
    # db.session.remove()
    # 多对多关系
    # db.session.add_all([
    #     models.Project2Host(project_id=1,host_id=1),
    #     models.Project2Host(project_id=1, host_id=2),
    #     models.Project2Host(project_id=2, host_id=1),
    #     models.Project2Host(project_id=2, host_id=2),
    # ])
    # db.session.commit()
    # db.session.remove()

    # 创建2个服务器 一个项目  创建关联关系
    # obj1 = models.Host(hostname='c3.com', port=80)
    # obj2 = models.Host(hostname='c4.com', port=80)
    # obj3 = models.Project(title='运维平台', name='devops')
    # db.session.add(obj1, )
    # db.session.add(obj2, )
    # db.session.add(obj3, )
    # db.session.commit()
    # db.session.add_all([
    #     models.Project2Host(host_id=obj1.id, project_id=obj3.id),
    #     models.Project2Host(host_id=obj2.id, project_id=obj3.id)
    # ])
    # db.session.commit()
    #简便写法
    # obj3 = models.Project(title='运维平台2', name='devops2',repository='asdfgh')
    # obj3.hosts=[models.Host(hostname='c33.com', port=80),models.Host(hostname='c44.com', port=80)]
    # db.session.add(obj3)
    # db.session.commit()
    # db.session.remove()

    #
    user1=models.UserInfo(username='wupeiqi',password='123',nickname='武')
    user2=models.UserInfo(username='wuxp',password='123',nickname='兴普')
    pro1=models.Project(title='公司官网',name='web1',repository='https://github.com/WuPeiqi/dbhot.git')
    pro1.hosts=[models.Host(hostname='c33.com', port=80),models.Host(hostname='c44.com', port=80)]
    db.session.add_all([
        user1,user2,pro1,
    ])
    db.session.commit()
    db.session.remove()
    # pass