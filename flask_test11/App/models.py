# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 22:55
# @Software: PyCharm
# @File    : models.py
# @Version : 3.7
# @Author  : Jeffrey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_models(app):
    db.init_app(app=app)


class Person(db.Model):
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(16))
