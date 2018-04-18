from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from flask_login import login_required
from app.cache import cache


jobtype = Blueprint('jobtype', __name__, url_prefix='')
param_location = ('json', )


@jobtype.route('/job/type')   # 工作类型数据处理
@cache.cached(timeout=43200)
@login_required
def job_type():
    job_names = ['Python','Java','C++','PHP','数据挖掘','搜索算法','精准推荐','C','C#','.NET','Hadoop','Delphi','Ruby',
                 'Node.js','Go','ASP','后端开发其它','HTML5','Android','iOS','移动开发其它','web前端','Flash','JavaScript']

    for i, job_name in enumerate(job_names):
        job_type=db.session.query(Job.positionName, func.count(), func.avg(Job.avg_salary)).filter_by(job_type=job_name)\
            .group_by(Job.positionName).order_by(func.count().desc()).limit(10).all()
        job_names[i] = {job_name : job_type,}

    return render_template('job_type.html',job_names=job_names)