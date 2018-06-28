#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import  Blueprint

account = Blueprint('account',__name__)

@account.route('/login')
def login():
    return "Login"