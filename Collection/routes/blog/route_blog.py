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

main= Blueprint('blog', __name__, template_folder='templates')



class DeletBlogForm(FlaskForm):
    submit = SubmitField('Delete')

def get_random_phrase():
    word_list = []
    today_list= []
    with open('utils/words.txt', 'r') as f:
        for line in f.readlines():
            word_list.append(line.strip('\n'))
    for x in range(3):
        today_list.append(word_list[random.randint(0, len(word_list)-1)])
    return word_list

def get_random_study():
    last_id = Blog.query.filter().order_by(Blog.id.desc()).first().id  # 通过找到最后一个的id，用random.randint随机出每日推荐
    while True:
        random_today = Blog.query.filter_by(id=random.randint(1, last_id + 1)).first()
        if random_today is not None:
            break
    return random_today

@main.route('/')
def index():
    topics = Topic.query.all()
    # if current_user.is_authenticated:
    #     username = current_user.username
    # word_list = get_random_phrase()
    random_today = get_random_study()

    return render_template('index.html', blog = random_today, topics =topics,)


@main.route('/new', methods=['POST', 'GET'])
@login_required
def new_article():
    topics = Topic.query.all()
    if request.method == 'POST':
        current_time = datetime.utcnow()
        username = current_user.username
        title = request.form.get('title')
        body = request.form.get('body')
        topic = request.form.get('topic')
        print(topic, body, title)
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
    return render_template('new-post.html', topics= topics)


@main.route('/topic')
def topic():
    topics = Topic.query.all()
    topic = str(request.args.get('sort_by', ''))
    page = int(request.args.get('page','没找到'))
    if topic == 'All':
        print('yes')
        articles = Blog.query.filter().order_by(Blog.ut.desc()).paginate(page, 8, False)
    else:
        articles = Blog.query.filter(Blog.topic == topic).order_by(Blog.ut.desc()).paginate(page, 8, False)

    pages = articles.pages
    # articles = Blog.query.filter_by(topic=topic)
    return render_template('topic.html', articles= articles,
                                            topic = topic,
                                            topics = topics,
                                             pages = pages,
                        )



@main.route('/detail', methods=['POST','GET'])
def detail():
    topics = Topic.query.all()
    form = DeletBlogForm()
    title = urllib.parse.unquote(request.args.get('title', ''))
    article = Blog.query.filter_by(id=title).first()
    return render_template('blog_detail.html', article= article, form=form, topics = topics,)

@main.route('/article/update', methods=['POST', 'GET'])
@login_required
def update():
    if current_user.username != 'Jayden-Liang':
        abort(404)
    topics = Topic.query.all()
    current_time = datetime.utcnow()
    arg = request.args.get('article_id')
    article = Blog.query.filter_by(id=int(arg)).first()
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.body = request.form.get('body')
        article.topic = request.form.get('topic')
        article.ut = current_time
        db.session.commit()
        return redirect('/')
    return render_template('update.html', article=article, topics= topics)


@main.route('/article/delete', methods = ['POST'])
@login_required
def delete():
    if current_user.username != 'Jayden-Liang':
        abort(404)
    form = DeletBlogForm()
    arg = request.args.get('delete_id')
    if arg is None:
        abort(404)
    if form.validate_on_submit():
        article = Blog.query.get(int(arg))
        if article is None:
            abort(404)
        db.session.delete(article)
        db.session.commit()
        return redirect('/')





# @main.route('/topic/<topic>')
# def get_topicAll(topic):
#     blog = Blog.query.filter_by(topic=topic).all()
#     all_blog = {}
#     for x in blog:
#        all_blog[x.id] = x.title
#     all = json.dumps(all_blog, ensure_ascii=False)
#     return all








