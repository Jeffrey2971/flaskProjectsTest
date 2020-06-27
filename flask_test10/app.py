from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
from views.views import blue


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.register_blueprint(blueprint=blue)
manage = Manager(app=app)

Bootstrap(app=app)

if __name__ == '__main__':
    manage.run()


