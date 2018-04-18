# coding: UTF-8
import os


# 配置导入函数

def load_config():
    """Load config."""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config