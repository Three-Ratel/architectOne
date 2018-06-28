#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint,render_template,request
from deploy import db
from deploy import models


project = Blueprint('project',__name__)

@project.route('/project/list')
def project_list():
    pro_list = db.session.query(models.Project).all()

    # for row in pro_list:
    #     print(row.id,row.title,row.hosts)

        # 使用sqlalchemy连表操作
        # hosts = db.session.query(models.Project2Host.host_id,models.Host.hostname).join(models.Host,models.Project2Host.host_id==models.Host.id,isouter=True).filter(models.Project2Host.project_id==row.id).all()
        # print(row.id,row.title,hosts)

    return render_template('project_list.html',pro_list=pro_list)


from wtforms.fields import simple
from wtforms.fields import core
from wtforms import validators
from wtforms import form

class ProjectAddForm(form.Form):
    name = simple.StringField(
        label=u'名称',
        validators=[validators.DataRequired(message=u'名称不能为空')],
        render_kw={'class':'form-control','placeholder':u'项目名称'}
    )
    title = simple.StringField(
        label=u'描述',
            validators=[validators.DataRequired(message=u'描述不能为空')],
        render_kw={'class': 'form-control', 'placeholder': u'项目描述'}
    )

    repository = simple.StringField(
            label=u'地址',
            validators=[validators.DataRequired(message=u'地址不能为空')],
            render_kw={'class': 'form-control', 'placeholder': u'项目地址'}
    )
    hosts = core.SelectMultipleField(
            label=u'主机',
            choices=(),
            coerce=int,
            render_kw={'class': 'form-control'}
    )

    def __init__(self,*args,**kwargs):
        super(ProjectAddForm,self).__init__(*args,**kwargs)

        self.hosts.choices = db.session.query(models.Host.id,models.Host.hostname).all()


@project.route('/project/add',methods=['GET','POST'])
def project_add():
    if request.method == 'GET':
        form = ProjectAddForm()
        return render_template('project_add.html',form=form)
    print(request.form)
    form = ProjectAddForm(formdata=request.form)
    if form.validate():
        print('验证成功',form.data)
        # {'x2': u'asdf', 'x3': u'asdf', 'x1': u'asdf', 'x4': [1, 2]})
        """
        1.创建项目 models.Project
        2.创建关系
        """
        # models.Project(name='test',title="test",repository='test')
        # obj = models.Project(**{"name":'test','title':"test",'repository':'test'})
        # 方式一：
        """
        data_dict = form.data
        host_id_list = data_dict.pop('hosts')
        obj = models.Project(**data_dict)
        db.session.add(obj)
        db.session.commit()

        p2h_list = []
        for host_id in host_id_list:
            p2h_list.append(models.Project2Host(host_id=host_id,project_id=obj.id))
        db.session.add_all(p2h_list)
        db.session.commit()
        """
        # 方式二：
        data_dict = form.data
        host_id_list = data_dict.pop('hosts')

        host_object_list = db.session.query(models.Host).filter(models.Host.id.in_(host_id_list)).all()
        obj = models.Project(**data_dict)
        obj.hosts = host_object_list

        db.session.add(obj)
        db.session.commit()
        db.session.remove()
    return render_template('project_add.html', form=form)

