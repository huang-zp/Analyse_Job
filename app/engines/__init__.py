import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app.config import load_config

SQLITE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/resources/' + 'sqlite.db'

SQLITE_URL = 'sqlite:///' + SQLITE_PATH


# 封装sqlalchemy引擎实例， 分离出flask上下文
class DBEngine:

    def __init__(self):
        self.engine = create_engine(load_config().SQLALCHEMY_DATABASE_URI, convert_unicode=True,
                                    encoding='utf-8', pool_size=64, max_overflow=0,
                                    pool_recycle=30, pool_timeout=10)
        self.session = self.create_scoped_session()

    def create_scoped_session(self):
        session_maker = sessionmaker(bind=self.engine)
        return scoped_session(session_maker)


# 就可以根据db进行操作数据库
db = DBEngine()
