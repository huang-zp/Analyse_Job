from app.engines import db
from app.models import Job


jobs = db.session.query(Job).order_by(Job.id).all()

for job in jobs:
    print(job.salary)
    salary = job.salary.lower()
    if '-' in salary:
        if '以上' in salary:
            salary = salary.replace('以上', '')
        salary_list = salary.split('-')
        result = (int(salary_list[0].replace('k', '')) + int(salary_list[1].replace('k', '')))*500
        result = int(result)
    elif '以上' in salary:
        salary_list = salary.split('k')
        result = salary_list[0].replace('k', '')
    else:
        result=0

    print(result)
    job.avg_salary = result
    db.session.add(job)

db.session.commit()
