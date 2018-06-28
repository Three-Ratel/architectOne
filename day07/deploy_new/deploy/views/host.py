#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import  Blueprint

host = Blueprint('host',__name__)

@host.route('/index')
def index():
    return "Index"