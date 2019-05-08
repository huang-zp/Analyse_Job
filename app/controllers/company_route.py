from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from flask_login import login_required
from app.cache import cache


company = Blueprint('company', __name__, url_prefix='')
param_location = ('json', )


@company.route('/company/welfare')   # 公司福利请求处理（这个没有用）
@cache.cached(timeout=43200)
@login_required
def company_welfare():
    return render_template('company_welfare.html')


@company.route('/company/area')    # 公司区域信息请求处理
@cache.cached(timeout=43200)
@login_required
def company_area():

    # 查找每个城市的职位数量，按职位数量排序，取前四十个
    citys = db.session.query(func.count(), Job.city).group_by(Job.city).order_by(func.count().desc()).limit(40).all()

    # 职位数量最高的十个城市
    dense_citys = citys[:10]

    # 职位数量最低的是个城市
    sparse_citys = citys[30:]

    # 将计算好的值返回前端进行展示
    return render_template('company_area.html', citys=citys, dense_citys=dense_citys, sparse_citys=sparse_citys)


@company.route('/company/salary')    # 公司薪水信息请求处理
@cache.cached(timeout=43200)
@login_required
def company_salary():
    # 查找薪水低于5000的数量
    range_5 = db.session.query(Job).filter(Job.avg_salary < 5000).count()

    # 查找薪水高于5000低于7000的数量
    range_5_7 = db.session.query(Job).filter(Job.avg_salary > 5000).filter(Job.avg_salary < 7000).count()
    # 以下同理
    range_7_9 = db.session.query(Job).filter(Job.avg_salary > 7000).filter(Job.avg_salary < 9000).count()
    range_9_11 = db.session.query(Job).filter(Job.avg_salary > 9000).filter(Job.avg_salary < 11000).count()
    range_11_13 = db.session.query(Job).filter(Job.avg_salary > 11000).filter(Job.avg_salary < 13000).count()
    range_13_15 = db.session.query(Job).filter(Job.avg_salary > 13000).filter(Job.avg_salary < 15000).count()
    range_15_17 = db.session.query(Job).filter(Job.avg_salary > 15000).filter(Job.avg_salary < 17000).count()
    range_17_19 = db.session.query(Job).filter(Job.avg_salary > 17000).filter(Job.avg_salary < 19000).count()
    range_19_21 = db.session.query(Job).filter(Job.avg_salary > 19000).filter(Job.avg_salary < 21000).count()
    range_21_23 = db.session.query(Job).filter(Job.avg_salary > 21000).filter(Job.avg_salary < 23000).count()
    range_23_25 = db.session.query(Job).filter(Job.avg_salary > 23000).filter(Job.avg_salary < 25000).count()
    range_25 = db.session.query(Job).filter(Job.avg_salary > 25000).count()
    salarys = [range_5, range_5_7, range_7_9, range_9_11, range_11_13, range_13_15, range_15_17, range_17_19,
               range_19_21, range_21_23, range_23_25, range_25]

    # 查找高薪的公司十个
    high_companys = db.session.query(Job).order_by(Job.avg_salary.desc()).filter(Job.avg_salary > 1).limit(10).all()
    # 底薪的十个
    lower_companys = db.session.query(Job).order_by(Job.avg_salary).filter(Job.avg_salary > 1000).limit(10).all()

    # 将计算好的值返回前端进行展示
    return render_template('company_salary.html', salarys=salarys, high_companys=high_companys, lower_companys=lower_companys)