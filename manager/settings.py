import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 得到项目根目录的绝对路径

image_dir_suffix = '/static/image/'  # 存储图片的文件夹路径后缀
image_dir = os.path.abspath(os.path.dirname(__file__)) + image_dir_suffix
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

db_uri = 'mysql+pymysql://root:12345@localhost/manager?charset=utf8'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')  # 先从环境变量中获取密钥，获取不到为secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象的修改

    IMAGE_DIR = image_dir
    IMAGE_DIR_SUFFIX = image_dir_suffix  # 相对路径下存储图片的文件夹
    IMAGE_UIR_PREFIX = '/image/'  # 图片请求时的前缀，即存储图片的文件夹在静态资源文件夹中的位置
    DEFAULT_HEAD_IMAGE_URI = '/image/1.jpg'
    DEFAULT_HOME_IMAGE_URI = '/image/default-home.png'


class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')
    SQLALCHEMY_DATABASE_URI = db_uri


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = db_uri


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
