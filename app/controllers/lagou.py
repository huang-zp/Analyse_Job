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
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','全栈工程师','.NET','Hadoop','Delphi','VB','Perl','Ruby','Node.js','Go','ASP','Shell','后端开发其它','HTML5','Android','iOS','WP','移动开发其它','web前端','Flash','html5','JavaScript']
    return render_template('job_count_trend.html', job_names=job_names)


@lagou.route('/trend/job/salary')
def job_salary():
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','全栈工程师','.NET','Hadoop','Delphi','VB','Perl','Ruby','Node.js','Go','ASP','Shell','后端开发其它','HTML5','Android','iOS','WP','移动开发其它','web前端','Flash','html5','JavaScript']
    return render_template('job_salary_trend.html', job_names=job_names)


@lagou.route('/trend/area/count')
def area_count():
    city_names = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津','重庆','郑州','青岛','合肥','福州','济南','大连','珠海','无锡','佛山','东莞','宁波','常州','沈阳','石家庄','昆明','南昌','南宁','哈尔滨','海口','中山','惠州','贵阳','长春','太原','嘉兴','泰安','昆山','烟台','兰州','泉州']
    return render_template('city_count_trend.html', city_names=city_names)


@lagou.route('/trend/area/salary')
def area_salary():
    city_names = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津','重庆','郑州','青岛','合肥','福州','济南','大连','珠海','无锡','佛山','东莞','宁波','常州','沈阳','石家庄','昆明','南昌','南宁','哈尔滨','海口','中山','惠州','贵阳','长春','太原','嘉兴','泰安','昆山','烟台','兰州','泉州']
    return render_template('city_salary_trend.html', city_names=city_names)


@lagou.route('/data/lagou')
def data_lagou():
    jobs = db.session.query(Job).limit(100).all()
    python_jobs = db.session.query(Job).filter_by(job_type = 'Python').order_by(Job.avg_salary.desc()).limit(3).all()
    java_jobs = db.session.query(Job).filter_by(job_type = 'Java').order_by(Job.avg_salary.desc()).limit(3).all()
    c_plus_jobs = db.session.query(Job).filter_by(job_type = 'C++').order_by(Job.avg_salary.desc()).limit(3).all()
    c_jobs = db.session.query(Job).filter(str(Job.positionName).find('++') == -1).filter_by(job_type = 'C').order_by(Job.avg_salary.desc()).limit(3).all()
    php_jobs = db.session.query(Job).filter_by(job_type = 'PHP').order_by(Job.avg_salary.desc()).limit(3).all()
    c_sharp_jobs = db.session.query(Job).filter_by(job_type='C#').order_by(Job.avg_salary.desc()).limit(3).all()

    return render_template('data_lagou.html', jobs=jobs, python_jobs=python_jobs,java_jobs=java_jobs,
                           c_plus_jobs=c_plus_jobs,c_jobs=c_jobs,php_jobs=php_jobs,c_sharp_jobs=c_sharp_jobs)


@lagou.route('/job/type')
def job_type():
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','.NET','Hadoop','Delphi','Ruby','Node.js','Go','ASP','后端开发其它','HTML5','Android','iOS','移动开发其它','web前端','Flash','JavaScript']

    for i, job_name in enumerate(job_names):
        job_type=db.session.query(Job.positionName, func.count(), func.avg(Job.avg_salary)).filter_by(job_type=job_name)\
            .group_by(Job.positionName).order_by(func.count().desc()).limit(10).all()
        job_names[i] = {job_name : job_type,}

    return render_template('job_type.html',job_names=job_names)


@lagou.route('/ave/salary')
def ave_salary():
    return render_template('ave_salary.html')


@lagou.route('/welfare/level')
def welfare_level():
    return render_template('welfare_level.html')


@lagou.route('/geo/area')
def geo_area():
    return render_template('geo_area.html')

