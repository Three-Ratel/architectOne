#!/usr/bin/python
# -*- coding:utf-8 -*-

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@192.168.11.22:3306/m1day07?charset=utf8"
    SQLALCHEMY_POOL_SIZE =5
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass