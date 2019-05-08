from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from datetime import datetime, timedelta

now_time = datetime.now()
begin_time = now_time + timedelta(days=-7)

aj = Blueprint('aj', __name__, url_prefix='')
param_location = ('json', )


@aj.route('/')   # 这个是主页请求处理， 有些数据是模拟的
def index():
    data = [22222, 12503, 17177, 19658, 17031, 19931, 17133, 4175] # 模拟的数据

    # 城市职位数量的查询计算
    city_names = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门']

    for i, city_name in enumerate(city_names):
        if city_name:
            break
        values = db.session.query(func.count()).filter(Job.city == city_name).group_by(Job.time_sort).limit(7).all()
        for j, value in enumerate(values):
            values[j] = int(value[0])
        city_names[i] = [city_name, values]

    # 各职位的趋势变动计算
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法']

    for i, job_name in enumerate(job_names):
        if job_name:
            break
        job_type=db.session.query(Job.positionName, func.count(), func.avg(Job.avg_salary)).filter_by(job_type=job_name)\
            .group_by(Job.positionName).order_by(func.count().desc()).limit(10).all()
        job_names[i] = {job_name : job_type,}

    return render_template('index.html', data=data)
