from datetime import datetime
from webargs import fields

from app.exceptions import ParamError
from app.engines import db
from app.models import ZlJob
from app.schemas import length_validator, OneOf

query_lagou_schema = {
    'start': fields.Int(missing=0),
    'length': fields.Int(missing=15, validate=length_validator),
    'order': fields.Nested({
        'field': fields.Str(missing='crawl_time'),
        'direction': fields.Str(missing='desc', validate=OneOf(['asc', 'desc']))
    }, missing={}),
    'filter': fields.Nested({
        'positionName': fields.Str(),
    }, missing={})
}
