
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from .base import Base, BaseColumns
from flask_security import UserMixin
from sqlalchemy.orm import relationship, backref


class User(Base, BaseColumns, UserMixin):
    __tablename__ = "users"

    name = Column(String(50), server_default='')

    email = Column(String(100), server_default='')

    role_id = Column(Integer(), server_default='0')

    active = Column(Integer, server_default='0')
    password = Column(String(100), server_default='')

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






