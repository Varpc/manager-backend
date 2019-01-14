import os

# basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 得到项目根目录的绝对路径

db_prefix = 'mysql+pymysql://root:12345@localhost/manager?charset=utf8'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')  # 先从环境变量中获取密钥，获取不到为secret key

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象的修改


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = db_prefix


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = db_prefix


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
