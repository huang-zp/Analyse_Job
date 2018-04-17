import os
from sqlalchemy import Column, DateTime, Integer, Text, ARRAY
from sqlalchemy import String, JSON
from .base import Base, BaseColumns
from datetime import datetime
from app.utill.format import format_time


class Job(Base, BaseColumns):
    __tablename__ = "jobs"

    companyId = Column(String(50), server_default='')
    score = Column(String(50), server_default='')
    positionId = Column(String(50), server_default='')
    positionName = Column(String(120), server_default='', index=True)
    createTime = Column(String(50), server_default='')
    positionAdvantage = Column(Text, server_default='')
    salary = Column(String(50), server_default='', index=True)
    approve = Column(String(50), server_default='')
    workYear = Column(String(50), server_default='')
    education = Column(String(50), server_default='')
    city = Column(String(50), server_default='', index=True)
    companyLogo = Column(String(120), server_default='')
    jobNature = Column(String(50), server_default='')
    industryField = Column(String(50), server_default='')
    companyShortName = Column(String(120), server_default='')
    financeStage = Column(String(50), server_default='')
    companyLabelList = Column(String(120), server_default='')
    publisherId = Column(String(50), server_default='')
    district = Column(String(50), server_default='')
    companySize = Column(String(50), server_default='')
    positionLables = Column(String(120), server_default='')
    industryLables = Column(String(120), server_default='')
    businessZones = Column(String(120), server_default='')
    formatCreateTime = Column(String(50), server_default='')
    longitude = Column(String(50), server_default='')
    latitude = Column(String(50), server_default='')
    companyFullName = Column(String(120), server_default='')
    adWord = Column(String(50), server_default='')
    hitags = Column(String(120), server_default='')
    resumeProcessRate = Column(String(50), server_default='')
    resumeProcessDay = Column(String(50), server_default='')
    imState = Column(String(50), server_default='')
    lastLogin = Column(String(50), server_default='')
    explain = Column(String(50), server_default='')
    plus = Column(String(50), server_default='')
    pcShow = Column(String(50), server_default='')
    appShow = Column(String(50), server_default='')
    deliver = Column(String(50), server_default='')
    gradeDescription = Column(String(50), server_default='')
    promotionScoreExplain = Column(String(50), server_default='')
    firstType = Column(String(50), server_default='')
    secondType = Column(String(50), server_default='')
    isSchoolJob = Column(String(50), server_default='')
    subwayline = Column(String(50), server_default='')
    stationname = Column(String(50), server_default='')
    linestaion = Column(Text, server_default='')

    job_type = Column(String(50), server_default='')
    time_sort = Column(String(50), default=format_time)
    avg_salary = Column(Integer(), index=True)

    job_type_id = Column(Integer(), index= True)
    city_id = Column(Integer(), index=True)



