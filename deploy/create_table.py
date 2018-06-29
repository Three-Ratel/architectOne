#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploy import create_app,db
from deploy import models
app=create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
