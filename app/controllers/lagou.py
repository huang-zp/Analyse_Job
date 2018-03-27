from flask import Blueprint, jsonify, render_template
from webargs.flaskparser import use_args
from app.engines import db
from app.models import Job
from app.businesses.lg_biz import LGBiz
from app.schemas.lagou import query_lagou_schema
from sqlalchemy import func


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


@lagou.route('/lagou/index')
def index():
    data = [22222, 12503, 17177, 19658, 17031, 19931, 17133, 14175]
    job_counts = db.session.query(func.count(Job.id)).first()[0]
    return render_template('index.html', job_counts=job_counts, data=data)





