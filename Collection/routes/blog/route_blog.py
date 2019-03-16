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
from flask_login import login_required, login_user, current_user
from datetime import datetime
import hashlib
import json
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from models import Blog, User, db

main= Blueprint('blog', __name__, template_folder='templates')





@main.route('/')
@login_required
def index():
    username = current_user.username
    page = request.args.get('page',1 ,type=int)
    articles = Blog.query.filter().order_by(Blog.ut.desc()).paginate(page, 8, False)
    pages = articles.pages
    utc_now = datetime.utcnow()
    return render_template('index.html', username=  username,
                                                 articles = articles,
                                                 utc_now = utc_now,
                                                 pages = pages,

                                                                  )


@main.route('/new', methods=['POST', 'GET'])
@login_required
def new_article():
    if request.method == 'POST':
        current_time = datetime.utcnow()
        username = current_user.username
        title = request.form.get('title')
        body = request.form.get('body')
        topic = request.form.get('topic')
        article = Blog(title= title,
                                body=body,
                                ct=current_time,
                                ut = current_time,
                                topic= topic,
                                writer = username
                    )
        db.session.add(article)
        db.session.commit()
        return redirect('/')
    return render_template('new-post.html')

@main.route('/detail/<id>')
def detail(id):
    article = Blog.query.filter_by(id=id).first()
    return render_template('detail.html', article= article)

@main.route('/article/update', methods=['POST', 'GET'])
def update():
    current_time = datetime.utcnow()
    arg = request.args.get('id')
    article = Blog.query.filter_by(id=int(arg)).first()
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.body = request.form.get('body')
        article.topic = request.form.get('topic')
        article.ut = current_time
        from initial import db
        db.session.commit()
        return redirect('/')
    return render_template('update.html', article=article)

@main.route('/article/delete')
def delete():
    arg = request.args.get('id')
    article = Blog.query.filter_by(id=int(arg)).first()
    db.session.delete(article)
    db.session.commit()
    return redirect('/')

@main.route('/topic/<topic>')
def get_topicAll(topic):
    blog = Blog.query.filter_by(topic=topic).all()
    all_blog = {}
    for x in blog:
       all_blog[x.id] = x.title
    all = json.dumps(all_blog, ensure_ascii=False)
    return all








