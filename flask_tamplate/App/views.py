from flask import Blueprint

blue = Blueprint('first_blue', __name__)


def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello Flask'
