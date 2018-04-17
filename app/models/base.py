# coding: utf-8
from sqlalchemy import Column, DateTime, BigInteger, func, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class BaseColumns:
    id = Column(BigInteger(), primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    create_time = Column(TIMESTAMP, server_default=func.now(), index=True)  # 记录创建时间
    update_time = Column(TIMESTAMP, server_default=func.now(), index=True)  # 记录更新时间

