# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 22:55
# @Software: PyCharm
# @File    : views.py
# @Version : 3.7
# @Author  : Jeffrey
from flask import Blueprint, render_template
import random
from App.models import db, Person

blue = Blueprint('first_blue', __name__)

@blue.route('/')
def index():
    return 'Hello Flask'

@blue.route('/create_db/')
def create_db():

    db.create_all()

    return 'Create Success'


@blue.route('/addperson/')
def add_person():
    p = Person()
    p.p_name = '洪泽飞%d' % (random.randrange(100))

    # 将数据添加到本次数据库的链接会话中
    db.session.add(p)
    # 提交会话
    db.session.commit()

    return 'Person Create Success '

@blue.route('/getpersion/')
def get_person_():
    persons = Person.query.all()


    # for person in persons:
    #     print(person.p_name)

    return render_template('PersonList.html', persons=persons)