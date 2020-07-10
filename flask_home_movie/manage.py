from flask import Flask, render_template, blueprints
from flask_script import Manager

app = Flask(__name__)
manage = Manager(app=app)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    manage.run()

