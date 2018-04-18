from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from flask_login import login_required
from datetime import datetime, timedelta
from app.cache import cache

calc_time = datetime.now() + timedelta(days=-7)
year = calc_time.year
month = calc_time.month-1
day = calc_time.day

trend = Blueprint('trend', __name__, url_prefix='')
param_location = ('json', )


@trend.route('/trend/job/count')    # 职位数量趋势请求
@cache.cached(timeout=43200)
@login_required
def job_count():
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','全栈工程师','.NET','Hadoop','Delphi','VB','Perl','Ruby','Node.js','Go','ASP','Shell','后端开发其它','HTML5','Android','iOS','WP','移动开发其它','web前端','Flash','html5','JavaScript']

    for i, job_name in enumerate(job_names):

        values = db.session.query(func.count()).filter(Job.job_type==job_name).order_by(Job.time_sort.desc()).group_by(Job.time_sort).limit(7).all()
        for j, value in enumerate(values):
            values[j] = value[0]

        job_names[i] = [job_name, values]
    return render_template('job_count_trend.html', job_names=job_names, year=year, month=month, day=day)


@trend.route('/trend/job/salary')   # 职位薪资趋势请求
@cache.cached(timeout=43200)
@login_required
def job_salary():
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','全栈工程师','.NET','Hadoop','Delphi','VB','Perl','Ruby','Node.js','Go','ASP','Shell','后端开发其它','HTML5','Android','iOS','WP','移动开发其它','web前端','Flash','html5','JavaScript']

    for i, job_name in enumerate(job_names):

        values = db.session.query(func.avg(Job.avg_salary)).filter(Job.job_type==job_name).order_by(Job.time_sort.desc()).group_by(Job.time_sort).limit(7).all()
        for j, value in enumerate(values):
            if value[0] is None:
                values[j] = 0
                continue
            values[j] = int(value[0])
        job_names[i] = [job_name, values]

    return render_template('job_salary_trend.html', job_names=job_names, year=year, month=month, day=day)


@trend.route('/trend/area/count')        # 地区职位数量请求
@cache.cached(timeout=43200)
@login_required
def area_count():
    city_names = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津','重庆','郑州','青岛','合肥','福州','济南','大连','珠海','无锡','佛山','东莞','宁波','常州','沈阳','石家庄','昆明','南昌','南宁','哈尔滨','海口','中山','惠州','贵阳','长春','太原','嘉兴','泰安','昆山','烟台','兰州','泉州']

    for i, city_name in enumerate(city_names):

        values = db.session.query(func.count()).filter(Job.city==city_name).order_by(Job.time_sort.desc()).group_by(Job.time_sort).limit(7).all()
        for j, value in enumerate(values):
            values[j] = int(value[0])
        city_names[i] = [city_name, values]

    return render_template('city_count_trend.html', city_names=city_names, year=year, month=month, day=day)


@trend.route('/trend/area/salary')  # 地区职位薪资请求
@cache.cached(timeout=43200)
@login_required
def area_salary():
    city_names = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津','重庆','郑州','青岛','合肥','福州','济南','大连','珠海','无锡','佛山','东莞','宁波','常州','沈阳','石家庄','昆明','南昌','南宁','哈尔滨','海口','中山','惠州','贵阳','长春','太原','嘉兴','泰安','昆山','烟台','兰州','泉州']

    for i, city_name in enumerate(city_names):

        values = db.session.query(func.avg(Job.avg_salary)).filter(Job.city==city_name).order_by(Job.time_sort.desc()).group_by(Job.time_sort).limit(7).all()
        for j, value in enumerate(values):
            if value[0] is None:
                values[j] = 0
                continue
            values[j] = int(value[0])
        city_names[i] = [city_name, values]

    return render_template('city_salary_trend.html', city_names=city_names, year=year, month=month, day=day)