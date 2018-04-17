from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.engines import db
from app.models import User

from flask_login import login_user, logout_user, login_required
auth = Blueprint('auth', __name__, url_prefix='')
param_location = ('json', )


@auth.route('/login/user', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db.session.query(User).filter_by(email=email).first()

        if user:
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('aj.index'))
            else:
                flash("密码错误，再试一次")
                return render_template('login.html')
        else:
            flash("没有此用户，检查输入")
            return render_template('login.html')
    return render_template('login.html')


@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user = db.session.query(User).filter_by(email=email).first()

        if user:
            flash(" 此邮箱已被注册")
            return render_template('register.html')

        if password1 != password2:
            flash("两次输入密码不一致")
            return render_template('register.html')

        user = User()
        user.name = name
        user.email = email
        user.password = password1
        user.role_id = 2
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('register.html')