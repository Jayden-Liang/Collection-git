import os
from flask import Flask
from flask import abort
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
from flask_login import login_required, login_user, current_user
from datetime import datetime
import hashlib
import urllib.parse
import json
import random
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from models import Blog, User, db, Topic

main= Blueprint('control', __name__, template_folder='templates')

class AddTopicForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), Length(0, 60, message='too long')],)
    submit = SubmitField('添加topic')

class removeTopicForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), Length(0, 60, message='too long')],)
    submit = SubmitField('删除topic')

@main.route('/admin')
@login_required
def index():
    form = AddTopicForm()
    removeForm = removeTopicForm()
    topics = Topic.query.all()
    return render_template('admin.html', topics =topics, form= form, removeForm = removeForm)


@main.route('/admin/addTopic', methods=['POST'])
@login_required
def addTopic():
    form = AddTopicForm()
    if form.validate_on_submit():
        topic = form.name.data
        newTopic = Topic(body=topic)
        db.session.add(newTopic)
        db.session.commit()
        return redirect('/')


@main.route('/admin/removeTopic', methods=['POST'])
@login_required
def removeTopic():
    removeForm = removeTopicForm()
    if removeForm.validate_on_submit():
        topic = removeForm.name.data
        newTopic = Topic.query.filter_by(body=topic).first()
        db.session.delete(newTopic)
        db.session.commit()
        return redirect('/')






