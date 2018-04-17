
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from .base import Base, BaseColumns
from flask_security import UserMixin
from sqlalchemy.orm import relationship, backref


class User(Base, BaseColumns, UserMixin):
    __tablename__ = "users"

    name = Column(String(50), server_default='')  # 用户名

    email = Column(String(100), server_default='')   # 用户邮箱

    role_id = Column(Integer(), server_default='0')   # 用户角色ID

    active = Column(Integer, server_default='0')   # 用户是否激活
    password = Column(String(100), server_default='')   # 用户密码

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.name






