
from sqlalchemy import Column
from sqlalchemy import String
from .base import Base, BaseColumns


class CrawlLog(Base, BaseColumns):
    __tablename__ = "crawllogs"

    source = Column(String(50), server_default='')   # 数据来源
    job_type = Column(String(50), server_default='')  # 职位类型
    spend_time = Column(String(50), server_default='')  # 爬取花费时间
    request_count = Column(String(50), server_default='')  # 请求次数
    job_count = Column(String(50), server_default='')  # 抓取工作数量




