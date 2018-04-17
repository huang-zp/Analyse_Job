from sqlalchemy import Column
from sqlalchemy import Integer, ForeignKey
from .base import Base, BaseColumns
from .role import Role
from .user import User

class RolesUser(Base, BaseColumns):
    __tablename__ = 'roles_users'
    user_id = Column(Integer(), ForeignKey('users.id'))
    role_id = Column(Integer(), ForeignKey('roles.id'))