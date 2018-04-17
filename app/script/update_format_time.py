from app.engines import db
from app.models import Job

jobs = db.session.query(Job).all()


for job in jobs:
    job.time_sort = job.createTime[:10]
    db.session.add(job)

db.session.commit()