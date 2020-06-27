# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 0:35
# @Software: PyCharm
# @File    : views.py
# @Version : 3.7
# @Author  : Jeffrey


from flask import Blueprint, url_for, request, render_template, make_response, Response, redirect, abort, jsonify
from jinja2 import Template

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return 'Hello_world'


@blue.route('/hello/')
def hello():
    return 'Hi'


@blue.route('/hello/<int:a>/')
def add(a):
    print(a)
    return 'add'


@blue.route('/reverse/')
def reverse():
    print(url_for('second_blue.index'))
    return '反向解析'

@blue.route('/request/', methods=['GET', 'POST'])
def get_request():
    # print(request)
    # print(type(request))
    # print(request.path)
    # print(request.url)
    # print(request.method)
    # print(request.data)
    # print(request.range)
    # print(request.values)
    print(request.args)
    # print(request.args.get('asdasdasd', 'not found'))
    print(request.args.getlist('name'))
    # print(request.host)
    # print(request.form)
    # print(request.json)
    # print(request.remote_addr)
    # print(request.user_agent)
    # print(request.files)
    # print(request.cookies)
    return '这有一个request', 200


@blue.route('/PersonInfo/')
def person_info():
    temp = render_template('PersonInfo.html')
    print(temp)
    return 'temp', 200

@blue.route('/PersonInfo/1/')
def person_info_1():
    temp = Template('<h2>这是一个模板{{user}}</h2>')
    print(temp)
    result = temp.render(user='Jeffrey')
    print(result)
    print(type(result))
    return '这有一个模板', 401




@blue.route('/makeresponse/')
def make():

    result = make_response('<h2>再睡觉就叫警察把你带走</h2>', 401)
    print(result)
    print(type(result))
    return result

@blue.route('/response/')
def resp():
    resp = Response(response='<h2>再睡觉就叫警察把你带走</h2>', status=405)
    return resp


@blue.route('/redirect/')
def redir():
    resp = redirect(url_for('first_blue.resp'))
    print(type(resp))
    return resp

@blue.route('/hehe/')
def hehe():
    abort(404)


@blue.route('/json/')
def json():
    # data = {'name': 'value'}
    # return jsonify(data)
    result = jsonify(name='Jeffrey', age=999999999999999999, hobby='learn')
    print(type(result))
    return result


