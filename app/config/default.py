# coding: utf-8
import os


# 这是配置
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    # PERMANENT_SESSION_LIFETIME = 7 * 3600 * 24
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"

    # 这是项目的根目录路径
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    # 这是数据库的连接URL
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@47.104.212.219/analyse_job"
    # CELERY_BROKER = "redis://127.0.0.1/2"

    # 这是redis的缓存前缀字段
    REDIS_PREFIX = "analyse_job"

    # session conf
    # 这是redis的配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = "redis://127.0.0.1/0"
    SESSION_COOKIE_NAME = "aj"
    # login required

    # 平台的名字
    APP = "analyse_job"
