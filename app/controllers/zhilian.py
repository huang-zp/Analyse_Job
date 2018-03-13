from flask import Blueprint, jsonify
from webargs.flaskparser import use_args

from app.businesses.zl_biz import ZLBiz
from app.schemas.zhilian import query_zhilian_schema

zhilian = Blueprint('zhilian', __name__, url_prefix='')
param_location = ('json', )


@zhilian.route('/zhilian/list', methods=['POST'])
@use_args(query_zhilian_schema)
def query_zhilian(payload):
    zl_biz = ZLBiz()
    query_data = zl_biz.query(**payload)
    return jsonify(code=200, data=query_data)


@zhilian.route('/zhilian/<int:zl_id>')
def get_info_details(zl_id):
    zl_biz = ZLBiz()
    data = zl_biz.query_details(zl_id)
    return jsonify(code=200, data=data)





