# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 15:37
# @Software: PyCharm
# @File    : manage.py.py
# @Version : 3.7
# @Author  : Jeffrey

# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 0:35
# @Software: PyCharm
# @File    : manage.py
# @Version : 3.7
# @Author  : Jeffrey

from flask import Flask
from flask_script import Manager
from App.views import blue
from App.views_2 import blue as blue_2
app = Flask(__name__)
app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue_2)
manager = Manager(app=app)

if __name__ == '__main__':
    # app.run()
    manager.run()