
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import User
from app.engines import db

user_operate = Blueprint('user_operate', __name__, url_prefix='')
param_location = ('json', )


@user_operate.route('/user/list') # 用户列表
@login_required
def user_list():

    # 查找所有的用户
    users = db.session.query(User).all()
    return render_template('user_list.html', users=users)


@user_operate.route('/user/delete/<int:user_id>')  # 删除用户
def user_delete(user_id):

    # 根据要删除的用户id进行数据库查找，查到删除
    user = db.session.query(User).filter(User.id == user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_operate.user_list'))


@user_operate.route('/user/change/<int:user_id>', methods=['POST', 'GET'])  # 修改用户
def user_change(user_id):

    # 在数据库中根据id查找出来要修改的用户id
    user = db.session.query(User).filter(User.id == user_id).first()

    if request.method == 'POST':
        # 获取前端表单修改的信息
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        # 如果传来的信息中角色字段含有管理两字，则使该用户为管理员。不含有则使普通用户
        if '管理' in role:
            role = 1
        else:
            role = 2
        password = request.form['password']
        if name == '' or email == '' or role == '' or password == '':
            flash(" 检查某些字段是否为空")
            return redirect(url_for('user_operate.user_change', user_id=user.id))

        # 将数据库中该用户的苏剧进行修改
        user.name = name
        user.email = email
        user.role_id = int(role)
        user.password = password

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_operate.user_list'))
    return render_template('user_change.html', user=user)


@user_operate.route('/user/add', methods=['POST', 'GET'])  # 增加用户，几乎和修改同理
def user_add():
    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']
        role = request.form['role']
        # if '管理' in role:
        #     role = 1
        # else:
        #     role = 2
        password = request.form['password']
        if name == '' or email == '' or role == '' or password == '':
            flash(" 检查某些字段是否为空")
            return redirect(url_for('user_operate.user_change'))

        user = User()
        user.name = name
        user.email = email
        user.role_id = int(role)
        user.password = password

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_operate.user_list'))

    return render_template('user_add.html')
