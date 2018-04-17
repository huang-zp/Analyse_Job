from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from datetime import datetime, timedelta

now_time = datetime.now()
begin_time = now_time + timedelta(days=7)

aj = Blueprint('aj', __name__, url_prefix='')
param_location = ('json', )


@aj.route('/')
def index():

    return render_template('index.html', data=data)