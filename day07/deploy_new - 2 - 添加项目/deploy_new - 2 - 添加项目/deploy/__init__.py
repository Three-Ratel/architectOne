#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models import *
from deploy.views.account import account
from deploy.views.host import host
from deploy.views.project import project

def create_app():
    app = Flask(__name__,static_url_path='/xxxxx')
    app.config.from_object('settings.DevelopmentConfig')


    app.register_blueprint(account)
    app.register_blueprint(host)
    app.register_blueprint(project)

    db.init_app(app)

    return app


