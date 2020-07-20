# coding:utf-8


# 基类
import os


class Config:
    """配置文件基类"""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 文件上传目录
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')
    UPLOAD_PHOTO_DIR = os.path.join(STATIC_DIR, 'upload/photo')

    # session配置

    # jwt数字签名
    SIGN = 'xadf@341.A'

    @staticmethod
    def get_db_uri(db_info):
        engine = db_info.get('ENGINE') or 'sqlite'
        driver = db_info.get('DRIVER') or 'sqlite'
        user = db_info.get('USER') or ''
        password = db_info.get('PASSWORD') or ''
        host = db_info.get('HOST') or 'localhost'
        port = db_info.get('PORT') or ''
        name = db_info.get('NAME') or ''
        return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)


# 开发环境
class DevelopConfig(Config):
    """ 开发环境配置 """

    DEBUG = True

    # mysql数据库参数
    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'Zcg@123456',# root
        'NAME': 'cms',
        'HOST': '127.0.0.1',# 114.215.84.163
        'PORT': '3306'
    }

    # 拼接sql路径
    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


# 测试环境
class TestConfig(Config):
    """ 测试环境配置类 """

    DEBUG = True

    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123',
        'NAME': 's1',
        'HOST': 'localhost',
        'PORT': '3306'
    }

    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


# 生产环境
class ProductConfig(Config):
    """ 生产环境配置 """

    DEBUG = False

    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123',
        'NAME': 's1',
        'HOST': 'localhost',
        'PORT': '3306'
    }

    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


# 导出变量
envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'product': ProductConfig,
}
