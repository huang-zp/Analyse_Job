import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# 日志格式配置
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] - [%(levelname)-8s] - [%(name)-8s] - [%(message)s] - [%(module)s] - [%(lineno)d]',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '[%(blue)s%(asctime)s%(reset)s] - [%(log_color)s%(levelname)-8s%(reset)s] - '
                      '[%(purple)s%(name)-8s%(reset)s] - [%(cyan)s%(message)s%(reset)s]',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'log_colors': {
                'DEBUG': 'white',
                'INFO': 'bold_green',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_red',
                'CRITICAL': 'red,bg_white'
            }
        }
    },
    'handlers': {
        'task': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': '{}/logs/task/task.log'.format(APP_PATH),
            'formatter': 'standard'
        },
        'console': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'colored'
        },
        'api': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': '{}/logs/api/api.log'.format(APP_PATH),
            'formatter': 'standard'
        },
        'lagou': {
            'level': 'WARNING',
            'filters': None,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': '{}/logs/lagou/lagou.log'.format(APP_PATH),
            'formatter': 'standard'
        },
        'zhilian': {
            'level': 'WARNING',
            'filters': None,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': '{}/logs/zhilian/zhilian.log'.format(APP_PATH),
            'formatter': 'standard'
        },
        'crawl': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'filename': '{}/logs/crawl.log'.format(APP_PATH),
            'formatter': 'standard'
        }
    },
    'loggers': {
        'task': {
            'handlers': ['task', 'console'],
            'propagate': False
        },
        'api': {
            'handlers': ['api', 'console'],
            'propagate': False
        },
        'task_lagou': {
            'handlers': ['lagou', 'console'],
            'propagate': False
        },
        'task_zhilian': {
            'handlers': ['zhilian', 'console'],
            'propagate': False
        },
        'crawl': {
            'handlers': ['crawl', 'console'],
            'propagate': False
        }
    }
}
