# coding: utf-8
import os


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    # PERMANENT_SESSION_LIFETIME = 7 * 3600 * 24
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@127.0.0.1:5432/analyse_job"
    # CELERY_BROKER = "redis://127.0.0.1/2"
    REDIS_PREFIX = "analyse_job"

    # session conf
    SESSION_TYPE = "redis"
    SESSION_REDIS = "redis://127.0.0.1/0"
    SESSION_COOKIE_NAME = "aj"
    # login required
    APP = "analyse_job"
