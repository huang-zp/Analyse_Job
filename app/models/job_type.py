
from sqlalchemy import Column
from sqlalchemy import String
from .base import Base, BaseColumns


class JobType(Base, BaseColumns):
    __tablename__ = "jobtypes"

    name = Column(String(50), server_default='')  # 职位类别





