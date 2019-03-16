import os
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateTable
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from flask_bootstrap import Bootstrap
from flask import Flask, redirect, url_for, flash, render_template, Blueprint
from wtforms.validators import DataRequired, Length, EqualTo, Email
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import login_required, login_user
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from models import Blog, User, db

main = Blueprint('user', __name__, template_folder='templates')




class RegisterForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), Length(0, 60, message='too long')], render_kw={'placeholder': '请输入您的名字', "class": 'form-control', "aria-describedby":"emailHelp" \
               })
    email = StringField('', validators=[DataRequired(), Email(),], render_kw={"placeholder": "请输入邮箱", "class": 'form-control', \
            })
    password= PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "请输入密码", "class": 'form-control'})
    confirm_password = StringField('',  validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "请输入密码", "class": 'form-control',"type": 'password'})
    submit= SubmitField('提交', render_kw={"class": "btn btn-primary"})
    fa_addon = {
        'email': 'fa-envelope-o',
        'name': 'fa-user-o',
        'password': 'fas-acorn-o"',
        'confirm_password': 'fa-envelope-o'
    }







@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # db.drop_all()
        # db.create_all()
        current_time = datetime.utcnow()
        password = form.password.data
        salt_pwd = User.salted_password(password)
        user = User(username= form.name.data,
                    email= form.email.data,
                    hashed_password = salt_pwd,
                    ct = current_time,

        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', form=form)






@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        login_pwd = User.salted_password(request.form.get('password'))
        a= User.query.filter_by(email=email).first()
        if a is None:
            return render_template('login.html', message = '邮箱未注册')
        else:
            if login_pwd == a.hashed_password:
                login_user(a, remember= True)
                return redirect('/')
            else:
                return render_template('login.html', message ='密码不正确')

    return render_template('login.html', message = '')







