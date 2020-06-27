# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 13:59
# @Software: PyCharm
# @File    : views.py
# @Version : 3.7
# @Author  : Jeffrey
from flask import Blueprint, render_template, request, Response, redirect, url_for, session

blue = Blueprint('first_blue', __name__)

@blue.route('/home/')
def home():
    username = session.get('user')

    return render_template('home.html', username=username)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        print(username)
        session['user'] = username
        resp = Response(response='%s登陆成功' % username)
        # 存入cookie
        # resp.set_cookie('user', username)
        return resp


@blue.route('/logout/')
def logout():
    resp = redirect(url_for('first_blue.home'))
    resp.delete_cookie('user')
    return resp

@blue.route('/hello/')
@blue.route('/hi/')
def hello():
    return render_template('hello.html')

@blue.route('/temp/')
def temp():
    return render_template('index.html')

@blue.route('/feedback')
def feedback():
    return render_template('feedback.html')