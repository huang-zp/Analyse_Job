from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from flask_login import login_required
from app.cache import cache

data = Blueprint('data', __name__, url_prefix='')
param_location = ('json', )


@data.route('/data/lagou')    # 数据管理模块中拉勾数据请求处理
@cache.cached(timeout=43200)
@login_required
def data_lagou():

    # 将数据库中的拉勾职位数据查找出来100个
    jobs = db.session.query(Job).limit(100).all()

    # 查找python高薪工作3个
    python_jobs = db.session.query(Job).filter_by(job_type = 'Python').order_by(Job.avg_salary.desc()).limit(3).all()
    # 以下同理
    java_jobs = db.session.query(Job).filter_by(job_type = 'Java').order_by(Job.avg_salary.desc()).limit(3).all()
    c_plus_jobs = db.session.query(Job).filter_by(job_type = 'C++').order_by(Job.avg_salary.desc()).limit(3).all()
    c_jobs = db.session.query(Job).filter(str(Job.positionName).find('++') == -1).filter_by(job_type = 'C').order_by(Job.avg_salary.desc()).limit(3).all()
    php_jobs = db.session.query(Job).filter_by(job_type = 'PHP').order_by(Job.avg_salary.desc()).limit(3).all()
    c_sharp_jobs = db.session.query(Job).filter_by(job_type='C#').order_by(Job.avg_salary.desc()).limit(3).all()

    return render_template('data_lagou.html', jobs=jobs, python_jobs=python_jobs,java_jobs=java_jobs,
                           c_plus_jobs=c_plus_jobs,c_jobs=c_jobs,php_jobs=php_jobs,c_sharp_jobs=c_sharp_jobs)


@data.route('/data/zhilian')    # 数据管理模块中智联数据请求处理
@cache.cached(timeout=43200)
@login_required
def data_zhilian():

    # 同上个函数
    jobs = db.session.query(Job).order_by(Job.id.desc()).limit(100).all()

    datacrawl_jobs = db.session.query(Job).filter_by(job_type = '数据挖掘').order_by(Job.avg_salary.desc()).limit(3).all()

    search_jobs = db.session.query(Job).filter_by(job_type = '搜索算法').order_by(Job.avg_salary.desc()).limit(3).all()
    recommend_jobs = db.session.query(Job).filter_by(job_type = '精准推荐').order_by(Job.avg_salary.desc()).limit(3).all()
    backend_jobs = db.session.query(Job).filter_by(job_type = '后端开发其它').order_by(Job.avg_salary.desc()).limit(3).all()
    weball_jobs = db.session.query(Job).filter_by(job_type = '全栈工程师').order_by(Job.avg_salary.desc()).limit(3).all()
    webfront_jobs = db.session.query(Job).filter_by(job_type='web前端').order_by(Job.avg_salary.desc()).limit(3).all()

    return render_template('data_zhilian.html', jobs=jobs, datacrawl_jobs=datacrawl_jobs,search_jobs=search_jobs,
                           recommend_jobs=recommend_jobs,backend_jobs=backend_jobs,weball_jobs=weball_jobs,webfront_jobs=webfront_jobs)
