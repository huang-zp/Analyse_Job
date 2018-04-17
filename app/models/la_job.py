import os
from sqlalchemy import Column, DateTime, Integer, Text, ARRAY
from sqlalchemy import String, JSON
from .base import Base, BaseColumns
from datetime import datetime
from app.utill.format import format_time


class Job(Base, BaseColumns):
    __tablename__ = "jobs"

    companyId = Column(String(50), server_default='')  # 公司ID
    score = Column(String(50), server_default='')  # 公司评分
    positionId = Column(String(50), server_default='')  # 职位ID
    positionName = Column(String(120), server_default='', index=True)  # 职位名称
    createTime = Column(String(50), server_default='')  # 职位创建时间
    positionAdvantage = Column(Text, server_default='')  # 职位优势
    salary = Column(String(50), server_default='', index=True)  # 薪水
    approve = Column(String(50), server_default='')  # 这个我也不知道
    workYear = Column(String(50), server_default='')  # 工作年限
    education = Column(String(50), server_default='')  # 教育学历
    city = Column(String(50), server_default='', index=True)  # 城市
    companyLogo = Column(String(120), server_default='')  # 公司Logo
    jobNature = Column(String(50), server_default='')  # 工作性质（全职，兼职）
    industryField = Column(String(50), server_default='')  # 公司类型
    companyShortName = Column(String(120), server_default='')  # 公司短昵称
    financeStage = Column(String(50), server_default='')  # 公司融资情况
    companyLabelList = Column(String(120), server_default='')  # 公司标签
    publisherId = Column(String(50), server_default='')  # （我也不知道。。）
    district = Column(String(50), server_default='')   # 公司所在城市的区域（比如 宛城区）
    companySize = Column(String(50), server_default='')  # 公司大小 （比如 50人）
    positionLables = Column(String(120), server_default='')  # 职位标签
    industryLables = Column(String(120), server_default='')
    businessZones = Column(String(120), server_default='')
    formatCreateTime = Column(String(50), server_default='')  # 格式化时间
    longitude = Column(String(50), server_default='')
    latitude = Column(String(50), server_default='')
    companyFullName = Column(String(120), server_default='')  # 公司全名
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

    job_type = Column(String(50), server_default='')  # 工作类型（比如 Python）
    time_sort = Column(String(50), default=format_time)  # 格式化时间（比如 2018-04-17）
    avg_salary = Column(Integer(), index=True)   # 平均薪水

    job_type_id = Column(Integer(), index= True)   # 工作类型id （比如 1代表python）
    city_id = Column(Integer(), index=True)  # 工作城市ID （比如 1代表北京）



