from sqlalchemy import func

from app.exceptions import DBError, ParamError
from app.engines import db

# 这是数据业务层
# 这个类业务层的基础类，封装基础的增删查改
class BaseBiz:

    @property
    def fields(self):
        return []

    @property
    def cls(self):
        return None

    # 这是查找的基础函数
    def find(self, **kwargs):
        return self.ses.query(self.cls).filter_by(**kwargs).first()

    def __init__(self):
        self.ses = db.session

    # 如果查找数据有数量限制就使用这个函数
    @staticmethod
    def query_count(query):
        count_q = query.statement.with_only_columns([func.count()]).order_by(None)
        count = query.session.execute(count_q).scalar()
        return count

    # 这个按照分页查找数据
    @staticmethod
    def _query_with_pagination(query, start=0, length=15):
        if start == -1:
            return query.all()
        if start < 0 or length < 0:
            raise ParamError('无效参数')
        data = query.slice(start, start + length).all()
        return data

    # 将查找的数据json化返回
    def _build_json_data(self, data, filter_count, total_count, ssac=False, **kwargs):
        json_data = {'records': [self.trans2dict(obj, ssac=ssac) for obj in data],
                     'total_count': total_count,
                     'filter_count': filter_count}
        return json_data

    def _build_query_filter(self, query, condition, strict=False):
        return query

    def trans2dict(self, obj, **kwargs):
        return obj.as_dict()

    # 这是更进一层的查找函数
    def base_query(self, query, **kwargs):
        total_count = self.query_count(query)
        query = self._build_query_filter(query, kwargs.get('filter', {}), strict=kwargs.get('strict'))
        query = self._build_query_order(query, kwargs.get('order', {}))
        filter_count = self.query_count(query)
        data = self._query_with_pagination(query, kwargs.get('start', 0), kwargs.get('length', 15))
        json_data = self._build_json_data(data, filter_count, total_count, **kwargs)
        return json_data

    # 这个根据条件对查找的数据排序的函数
    def _build_query_order(self, query, order):
        order_field, order_dir = order.get('field', 'posted_time'), order.get('direction', 'desc')
        if order_field not in self.fields:
            order_field = 'posted_time'
        obj_attr = getattr(self.cls, order_field)
        return query.order_by(getattr(obj_attr, order_dir)()).order_by(self.cls.posted_time.desc())

    # 这是为了安全提交数据，如果有异常发生则进行回滚
    def safe_commit(self):
        try:
            self.ses.commit()
        except Exception as e:
            self.ses.rollback()
            raise DBError(e)
        return True
