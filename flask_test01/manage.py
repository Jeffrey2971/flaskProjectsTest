from flask import Flask, render_template, url_for
from flask_script import Manager
import uuid
app = Flask(__name__)

manager = Manager(app=app)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/hello/')
def hello():
    return 'Hello'


@app.route('/say/')
def say():
    result = 1 / 0
    return 'Say'


@app.route('/templates')
def temp():
    ren = render_template('hello.html')

    print(ren)
    print(type(ren))
    return ren


@app.route('/student/<uuid:id>/')
def student(id):
    print(type(id))
    print(id)
    return '参数'

@app.route('/getuuid/')
def get_uuid():
    return str(uuid.uuid4())


@app.route('/any/<any(a, b, c):an>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def any(an):
    print(an)
    print(type(an))
    return 'Any'


@app.route('/reverse/')
def reverse():

    result = url_for('get_uuid')
    print(result)
    print(url_for('any', an='b'))
    return 'There is reverse'


if __name__ == '__main__':
    manager.run()
