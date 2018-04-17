import os
from sqlalchemy import Column, DateTime, Integer, Text, ARRAY
from sqlalchemy import String, JSON
from .base import Base, BaseColumns


class Message(Base, BaseColumns):
    __tablename__ = "messages"

    message = Column(Text, server_default='')  # 留言信息

    pass_code = Column(Integer(), server_default='0')  # 留言是否审核通过 （1 通过  0 拦截）



