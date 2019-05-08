from flask import Blueprint, render_template, request, redirect, url_for
from app.engines import db
from app.models import Job
from flask_login import login_required
from app.utill.filter import gfw
from flask import flash

recommend = Blueprint('recommend', __name__, url_prefix='')
param_location = ('json', )


@recommend.route('/recommend') #填写理想职位页面
@login_required
def recommend_index():

    return render_template('recommend.html')


@recommend.route('/recommend/job', methods=['POST', 'GET']) # 职位推荐页面
@login_required
def recommend_job():
    if request.method == 'POST':
        # 获取填写的理想职位信息
        job = request.form['job']
        salary = request.form['salary']
        city = request.form['city']

        # 判断信息是否输全
        if not job or not salary or not city:
            flash("请输全信息")
            return render_template('recommend.html')
        try:
            # 查找匹配的职位，同时将福利比较好的前三十个职位提取出来
            jobs = db.session.query(Job).filter(Job.job_type == job).filter(Job.avg_salary == salary).filter(Job.city == city).filter(Job.positionAdvantage != '').filter(Job.companyLabelList != '').limit(30).all()
        except Exception as e:
            flash("请好好输信息")
            return render_template('recommend.html')

        # 将前三十个职位提取出来返回前端展示
        return render_template('recommend_job.html', jobs=jobs)
    return render_template('recommend.html')
