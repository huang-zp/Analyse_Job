from flask import Blueprint, jsonify
from webargs.flaskparser import use_args

from app.businesses.lg_biz import LGBiz
from app.schemas.lagou import query_lagou_schema

lagou = Blueprint('lagou', __name__, url_prefix='')
param_location = ('json', )


@lagou.route('/lagou/list', methods=['POST'])
@use_args(query_lagou_schema)
def query_lagou(payload):
    lg_biz = LGBiz()
    query_data = lg_biz.query(**payload)
    return jsonify(code=200, data=query_data)


@lagou.route('/lagou/<int:lg_id>')
def get_info_details(lg_id):
    lg_biz = LGBiz()
    data = lg_biz.query_details(lg_id)
    return jsonify(code=200, data=data)





