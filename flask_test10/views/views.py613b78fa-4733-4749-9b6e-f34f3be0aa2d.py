# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 0:37
# @Software: PyCharm
# @File    : views.py.py
# @Version : 3.7
# @Author  : Jeffrey

from flask import Flask, Blueprint, request, url_for, render_template, redirect, flash

app = Flask(__name__)

blue = Blueprint('first_blue', __name__)

@blue.route('/')
def main():
    return render_template('index.html')

@blue.route('/feedback')
def feedback():

    hobby = ['eat', 'SLEEP', 'dRiNK', '<h2>driver</h2>', 'study', 'SLEEP']
    make_safe = '<h2>坚持，就是胜利！</h2>'

    return render_template('feedback.html', hobby=hobby, make_safe=make_safe)

@blue.route('/hello_bootstrap/')
def hello_bootstrap():
    return render_template('hello_bootstrap.html')

@blue.route('/userlogin/', methods=['POST', 'GET'])
def user_login():
    if request.method == 'GET':
        return render_template('user_login.html')
    elif request.method == 'POST':
        flash('用户名或密码不正确')
        return redirect(url_for('first_blue.user_login'))
