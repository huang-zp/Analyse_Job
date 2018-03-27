
from sqlalchemy import Column
from sqlalchemy import String
from .base import Base, BaseColumns


class CrawlLog(Base, BaseColumns):
    __tablename__ = "crawllogs"

    source = Column(String(50), server_default='')
    job_type = Column(String(50), server_default='')
    spend_time = Column(String(50), server_default='')
    job_count = Column(String(50), server_default='')
    workYear = Column(String(50), server_default='')




