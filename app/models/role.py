
from sqlalchemy import Column
from sqlalchemy import String
from .base import Base, BaseColumns
from flask_security import RoleMixin


class Role(Base, BaseColumns, RoleMixin):
    __tablename__ = "roles"

    name = Column(String(50), server_default='')
    description = Column(String(100), server_default='')








