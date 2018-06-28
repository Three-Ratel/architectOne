#!/usr/bin/python
# -*- coding:utf-8 -*-
from deploy import create_app

app = create_app()

if __name__ == '__main__':
    app.run()