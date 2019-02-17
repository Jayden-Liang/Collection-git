import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateTable
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask import  Flask, redirect, url_for, flash, render_template, Blueprint
from flask_wtf.csrf import CSRFProtect
from route_user import main as route_user
from route_blog import main as route_blog
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment





app = Flask(__name__)

bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)
db= SQLAlchemy(app)
migrate = Migrate(app, db)
moment= Moment(app)
login_manager= LoginManager(app)
login_manager.login_view='user.login'
login_manager.session_protection= 'strong'


app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('settings.py', silent=True)
app.secret_key= b'fdhakhfkjaghj873o8qyhhg'


app.register_blueprint(route_blog)
app.register_blueprint(route_user)





@login_manager.user_loader
def load_user(id):
    from models import User
    print('i just checked, load_user')
    return User.query.get(int(id))





