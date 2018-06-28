#!/usr/bin/python
# -*- coding:utf-8 -*-

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123QWEasd@172.21.120.53:3306/m1day07?charset=utf8"
    SQLALCHEMY_POOL_SIZE =5
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass