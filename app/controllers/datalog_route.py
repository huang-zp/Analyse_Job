from flask import Blueprint, render_template
from app.engines import db
from app.models import CrawlLog
from flask_login import login_required, logout_user
from app.models import User

datalog = Blueprint('datalog', __name__, url_prefix='')
param_location = ('json', )


@datalog.route('/datalog')    # 数据日志模块请求处理
@login_required
def log():

    datalogs = db.session.query(CrawlLog).limit(100).all()

    return render_template('data_log.html', datalogs=datalogs)
