import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
def get_db_uri(dbinfo):
    # 获取值，如不存在则默认值
    BACKEND = dbinfo.get('BACKEND') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    DB = dbinfo.get('DB') or 'db'

    return "{}+{}://{}:{}@{}:{}/{}".format(BACKEND, DRIVER, USER, PASSWORD, HOST, PORT, DB)
class Config:
    SECRET_KEY = 'ASDJKASHDJAKSJKXMNCNVBMXCBNSERH12392134'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# 不同环境有不同环境的配置
class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'DB': 'Python1803FlaskProject'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'Aa664490254',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DB': 'Python1803FlaskProjectTesting'
    }

    SQLACHEMY_DATABASE_URI = get_db_uri(DATABASE)

# 演示环境，和线上完全一致
class StagingConfig(Config):

    DEBUG = True
    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'Aa664490254',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DB': 'Python1803FlaskProjectStaging'
    }

    SQLACHEMY_DATABASE_URI = get_db_uri(DATABASE)

class ProductConfig(Config):

    DEBUG = True
    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'Aa664490254',
        'HOST': 'localhost',
        'PORT': '3306',
        'DB': 'Python1803FlaskProjectProduct'
    }
    SQLACHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig
}