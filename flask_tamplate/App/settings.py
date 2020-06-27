def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'develop'

    return '{}:{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)
    pass

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'asdasdasdasdj123123123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}