
from sqlalchemy import Column
from sqlalchemy import String
from .base import Base, BaseColumns


class City(Base, BaseColumns):
    __tablename__ = "cities"

    name = Column(String(50), server_default='')





