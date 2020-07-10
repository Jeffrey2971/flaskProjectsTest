import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or os.environ.get('ENGINE')
    DRIVER = dbinfo.get('DRIVER') or os.environ.get('pymysql')
    USER = dbinfo.get('USER') or os.environ.get('USER')
    PASSWORD = dbinfo.get('PASSWORD') or os.environ.get('PASSWORD')
    HOST = dbinfo.get('HOST') or os.environ.get('HOST')
    PORT = dbinfo.get('PORT') or os.environ.get('PORT')
    DB = dbinfo.get('DB') or 'develop'

    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, DB)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_CONFIG
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 25
    MAIL_USERNAME = os.environ.get('mail_username')
    MAIL_PASSWORD = os.environ.get('mail_password')
    MAIL_DEFAULT_SENDER = os.environ.get('mail_username')


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE': os.environ.get('ENGINE'),
        'DRIVER': os.environ.get('DRIVER'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'DB': os.environ.get('DB'),
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'ENGINE': os.environ.get('ENGINE'),
        'DRIVER': os.environ.get('DRIVER'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'DB': os.environ.get('DB'),
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        'ENGINE': os.environ.get('ENGINE'),
        'DRIVER': os.environ.get('DRIVER'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'DB': os.environ.get('DB'),
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        'ENGINE': os.environ.get('ENGINE'),
        'DRIVER': os.environ.get('DRIVER'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'DB': os.environ.get('DB'),
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}

ADMINS = ('Jeffrey', 'Mable')

FILE_PATH_PREFIX = "/static/uploads/icons"

UPLOADES_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')
print(UPLOADES_DIR)
