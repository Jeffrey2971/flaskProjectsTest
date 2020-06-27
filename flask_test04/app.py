from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    class Person(object):
        name = u'飞飞'
        age = 9999999999

    p = Person()

    context = {
        'username': u'红泽飞',
        'gender': '男',
        'age': 9999999999,
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
