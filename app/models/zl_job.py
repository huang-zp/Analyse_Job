import os
from sqlalchemy import Column, DateTime, Integer, Text, ARRAY
from sqlalchemy import String, JSON
from .base import Base, BaseColumns


class ZlJob(Base, BaseColumns):
    __tablename__ = "zljobs"

    positionName = Column(String(120), server_default='')
    companyFullName = Column(String(120), server_default='')
    companyLabelList = Column(String(120), server_default='')

    salary = Column(String(50), server_default='')
    city = Column(String(50), server_default='')
    createTime = Column(String(50), server_default='')
    jobNature = Column(String(50), server_default='')
    workYear = Column(String(50), server_default='')
    education = Column(String(50), server_default='')

    positionCount = Column(String(50), server_default='')

    firstType = Column(String(50), server_default='')

    job_type = Column(String(50), server_default='')

    url = Column(Text, server_default='')



