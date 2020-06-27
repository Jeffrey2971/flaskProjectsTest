# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 1:33
# @Software: PyCharm
# @File    : views_2.py
# @Version : 3.7
# @Author  : Jeffrey
from flask import Blueprint

blue = Blueprint('second_blue', __name__)

@blue.route('/abc/')
def index():

    return 'abc'