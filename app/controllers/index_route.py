from flask import Blueprint, render_template
from app.engines import db
from app.models import Job
from sqlalchemy import func
from datetime import datetime, timedelta

now_time = datetime.now()
begin_time = now_time + timedelta(days=-7)

aj = Blueprint('aj', __name__, url_prefix='')
param_location = ('json', )


@aj.route('/')
def index():
    data = [22222, 12503, 17177, 19658, 17031, 19931, 17133, 4175]

    return render_template('index.html', data=data)