#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
# from deploy import db
# from deploy  import models


project=Blueprint('project',__name__)


@project.route('/project/list')
def project_list():
    # pro_list=db.session.query(models.Project).all()
    # return render_template('project_list.html',pro_list)
  return render_template('project_list.html',)