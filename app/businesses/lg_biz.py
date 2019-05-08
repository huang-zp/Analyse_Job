from sqlalchemy import and_, or_

from app.businesses.base_biz import BaseBiz
from app.exceptions import ResourceNotFound, ParamError
from app.models import Job


# 这是拉勾数据的增删查改类 继承基础的增删查改类
class LGBiz(BaseBiz):

    @property
    def cls(self):
        return Job

    @property
    def fields(self):
        return []

    def query(self, **kwargs):
        query = self.ses.query(self.cls)
        return self.base_query(query, **kwargs)

    def _build_query_filter(self, query, condition, strict=False):
        for attr in ['domain', 'source']:
            if condition.get(attr):
                query = query.filter(getattr(self.cls, attr).like('%' + condition[attr] + '%'))
        return query

    # 这是查找单个职位详细信息的函数
    def query_details(self, domain_id):
        domain = self.ses.query(Job).filter_by(id=domain_id).first()
        if not domain:
            return None
        details = domain.as_dict()
        return details

    def _build_query_order(self, query, order):
        order_field, order_dir = order.get('field', 'crawl_time'), order.get('direction', 'desc')
        if order_field not in self.fields:
            order_field = 'crawl_time'
        obj_attr = getattr(self.cls, order_field)
        return query.order_by(getattr(obj_attr, order_dir)()).order_by(self.cls.crawl_time.desc())
