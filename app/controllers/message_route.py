from flask import Blueprint, render_template, request, redirect, url_for
from app.engines import db
from app.models import Message
from flask_login import login_required
from app.utill.filter import gfw

message = Blueprint('message', __name__, url_prefix='')
param_location = ('json', )


@message.route('/message/pass')  # 处理留言通过请求
@login_required
def message_pass():
    # 将通过的留言进行查询操作
    messages = db.session.query(Message).filter_by(pass_code=1).order_by(Message.id.desc()).limit(30).all()

    # 将通过的留言返回前端进行展示
    return render_template('message_pass.html', messages=messages)


@message.route('/message/stop')   # 处理留言拦截请求
@login_required
def message_stop():
    messages = db.session.query(Message).filter_by(pass_code=0).order_by(Message.id.desc()).limit(30).all()

    return render_template('message_stop.html', messages=messages)


@message.route('/message/deal', methods=['POST', 'GET'])    # 处理留言请求, 然后根据是否敏感取去转给通过或者拦截请求
@login_required
def message_deal():
    if request.method == 'POST':
        message = request.form['message']

        # 这个就是敏感词过滤，能通过的话pass_code是1，不能是0
        if gfw.filter(message):
            new_message = Message()
            new_message.message = message
            new_message.pass_code = 0
            db.session.add(new_message)
        else:
            new_message = Message()
            new_message.message = message
            new_message.pass_code = 1
            db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('aj.index'))


@message.route('/message/delete/pass/<int:message_id>', methods=['GET'])     # 通过信息的删除请求
@login_required
def message_delete_pass(message_id):

    # 根据留言id查找出来需要删除的留言进行删除
    db.session.query(Message).filter_by(id=message_id).delete()
    db.session.commit()
    return redirect(url_for('message.message_pass'))


@message.route('/message/delete/stop/<int:message_id>', methods=['GET'])      # 拦截信息的删除请求
@login_required
def message_delete_stop(message_id):
    # 根据留言id查找出来需要删除的留言进行删除
    db.session.query(Message).filter_by(id=message_id).delete()
    db.session.commit()
    return redirect(url_for('message.message_stop'))
