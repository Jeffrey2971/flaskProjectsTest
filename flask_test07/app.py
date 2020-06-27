from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    comments = [
        {
            'user': u'知了课堂',
            'content': 'xxxx'
        },
        {
            'user': u'mable',
            'content': 'xxxxx'
        }
    ]
    return render_template('index.html', comments=comments)


if __name__ == '__main__':
    app.run()
