#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from deploy.views.account import account
from deploy.views.host import host
from deploy.views.project import project


from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(account)
    app.register_blueprint(host)
    app.register_blueprint(project)
    db.init_app(app)
    return app