from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.engines import db
from app.models import User

from flask_login import login_user, logout_user, login_required
auth = Blueprint('auth', __name__, url_prefix='')
param_location = ('json', )


@auth.route('/login/user', methods=['POST', 'GET'])   # 用户登录请求处理
def login():
    if request.method == 'POST':

        # 这是获取前端传过来的数据
        email = request.form['email']
        password = request.form['password']

        # 对前端传过来的数据进行数据库中查找
        user = db.session.query(User).filter_by(email=email).first()


        # 根据是否查找到用户进行不同的处理
        if user:

            # 查找到用户进行密码判断是否对
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('aj.index'))
            else:
                flash("密码错误，再试一次")
                return render_template('login.html')
        else:

            # 查不到返回错误提示
            flash("没有此用户，检查输入")
            return render_template('login.html')
    return render_template('login.html')


@auth.route('/logout', methods=['POST', 'GET'])    # 用户登出请求处理
@login_required
def logout():
    logout_user()

    # 登出后重定向到用户登陆页面
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['POST', 'GET'])     # 用户注册请求处理
def register():
    if request.method == 'POST':
        # 这是获取前端传过来的数据
        name = request.form['name']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']

        # 对前端传过来的数据进行数据库中查找看是否己经注册过
        user = db.session.query(User).filter_by(email=email).first()

        if user:
            flash(" 此邮箱已被注册")
            return render_template('register.html')

        if password1 != password2:
            flash("两次输入密码不一致")
            return render_template('register.html')

        # 对新注册的用户信息写入数据库
        user = User()
        user.name = name
        user.email = email
        user.password = password1
        user.role_id = 2
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('register.html')