from flask import Blueprint, render_template, request, redirect, url_for
from app.engines import db
from app.models import Job
from flask_login import login_required
from app.utill.filter import gfw
from flask import flash

recommend = Blueprint('recommend', __name__, url_prefix='')
param_location = ('json', )


@recommend.route('/recommend')
@login_required
def recommend_index():

    return render_template('recommend.html')


@recommend.route('/recommend/job', methods=['POST', 'GET'])
@login_required
def recommend_job():
    print(1)
    if request.method == 'POST':
        print(2)
        job = request.form['job']
        print(3)
        print(job)
        salary = request.form['salary']
        print(4)
        city = request.form['city']
        print(job, salary, city)
        if not job or not salary or not city:

            flash("请输全信息")
            return render_template('recommend.html')
        try:
            jobs = db.session.query(Job).filter(Job.job_type == job).filter(Job.avg_salary == salary).filter(Job.city == city).filter(Job.positionAdvantage != '').filter(Job.companyLabelList != '').limit(30).all()
        except Exception as e:
            flash("请好好输信息")
            return render_template('recommend.html')
        return render_template('recommend_job.html', jobs=jobs)
    return render_template('recommend.html')