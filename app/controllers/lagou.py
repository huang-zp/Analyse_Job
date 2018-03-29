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


@lagou.route('/')
def index():
    data = [22222, 12503, 17177, 19658, 17031, 19931, 17133, 4175]
    job_counts = db.session.query(func.count(Job.id)).first()[0]
    return render_template('index.html', job_counts=job_counts, data=data)


@lagou.route('/trend/job/count')
def job_count():
    job_name = [['Java','C++','PHP'],['数据挖掘','搜索算法','精准推荐'],['C','C#','全栈工程师'],['.NET','Hadoop','Python'],['Delphi','VB','Perl'],['Ruby','Node.js','Go'],['ASP','Shell','后端开发其它'],['HTML5','Android','iOS'],['WP','移动开发其它','web前端'],['Flash','html5','JavaScript']]
    return render_template('job_count_trend.html', job_name=job_name)


@lagou.route('/trend/job/salary')
def job_salary():
    return render_template('job_count_trend.html')


@lagou.route('/trend/area/count')
def area_count():
    return render_template('job_count_trend.html')


@lagou.route('/trend/area/salary')
def area_salary():
    return render_template('job_count_trend.html')


@lagou.route('/data/lagou')
def data_lagou():
    return render_template('data_lagou.html')


@lagou.route('/job/type')
def job_type():
    return render_template('job_type.html')

