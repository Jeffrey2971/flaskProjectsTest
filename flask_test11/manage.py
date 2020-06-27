from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from App import models
from App.models import init_models
from App.views import blue

app = Flask(__name__)


# 数据库链接地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Aa664490254@localhosl:3306/test'

# 实例化对象
manage = Manager(app=app)

# db = SQLAlchemy(app=app)

# 注册蓝图
app.register_blueprint(blueprint=blue)

models.init_models(app)
if __name__ == '__main__':
    manage.run()
