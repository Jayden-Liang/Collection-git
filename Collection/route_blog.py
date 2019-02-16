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

main= Blueprint('blog', __name__)





@main.route('/')
@login_required
def index():
    from models import Blog
    from models import User
    from initial import db
    username = current_user.username
    articles = Blog.query.all()
    from initial import moment
    utc_now = datetime.utcnow()
    print('/', utc_now)
    return render_template('main/index.html', username=  username,
                                                 articles = articles,
                                                 utc_now = utc_now
                                                                  )


@main.route('/new', methods=['POST', 'GET'])
@login_required
def new_article():
    if request.method == 'POST':
        from models import Blog
        from models import User
        from initial import db
        current_time = datetime.utcnow()
        print(request.form)
        username = current_user.username
        title = request.form.get('title')
        body = request.form.get('body')
        topic = request.form.get('topic')
        article = Blog(title= title,
                                body=body,
                                ct=current_time,
                                topic= topic,
                                writer = username
                    )
        db.session.add(article)
        db.session.commit()
        print('创建文章成功')
        return redirect('/')
    return render_template('main/new-post.html')

@main.route('/detail/<id>')
def detail(id):
    from models import Blog
    article = Blog.query.filter_by(id=id).first()
    print(article)
    return render_template('main/detail.html', article= article)

@main.route('/article/update', methods=['POST', 'GET'])
def update():
    from models import Blog
    arg = request.args.get('id')
    article = Blog.query.filter_by(id=int(arg)).first()
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.body = request.form.get('body')
        article.topic = request.form.get('topic')
        from initial import db
        db.session.commit()
        return redirect('/')
    return render_template('main/update.html', article=article)

@main.route('/article/delete')
def delete():
    from initial import db
    from models import Blog
    arg = request.args.get('id')
    article = Blog.query.filter_by(id=int(arg)).first()
    db.session.delete(article)
    db.session.commit()
    return redirect('/')

@main.route('/topic/<topic>')
def get_topicAll(topic):
    from initial import db
    from models import Blog
    blog = Blog.query.filter_by(topic=topic).all()
    all_blog = {}
    for x in blog:
       all_blog[x.id] = x.title
    print(all_blog)
    all = json.dumps(all_blog, ensure_ascii=False)
    print(type(all))
    return all








