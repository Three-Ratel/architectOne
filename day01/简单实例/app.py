#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, session
import functools

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.secret_key = 'zq'


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        user_info = session.get('user_info')
        if not user_info:
            return redirect('/login')
        return func(*args, **kwargs)

    return inner


@app.route('/index', methods=['GET', 'POST'], endpoint='n2')
@auth
def index():
    # user_info = session.get('user_info')
    # if not user_info:
    #     return redirect('/login')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'], endpoint='n1')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            return redirect('/index')
    return render_template('login.html', msg='用户名密码错误', errcode=123)
    return render_template('login.html', **{'msg': '用户名或密码错误'})


# @app.route('/logout', methods=['GET' ])
# def logout():
#     x=session.pop('user_info')
#     return redirect('/login')


if __name__ == '__main__':
    app.run()
