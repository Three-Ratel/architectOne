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
    result = db.session.query(models.UserInfo).all()
    print(result)
    db.session.remove()
