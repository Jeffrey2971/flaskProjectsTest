def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    DB = dbinfo.get('DB') or 'develop'

    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, DB)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'Jeffrey222233s'
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
        'DB': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'DB': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'DB': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class ProductConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'DB': 'Python1806FlaskProject'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}