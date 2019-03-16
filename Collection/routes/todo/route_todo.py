from flask import Blueprint, render_template, request, json
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from models import db, Todo
from datetime import datetime
import time

todo_main = Blueprint('todo_main', __name__, template_folder='templates' )

class TodoForm(FlaskForm):
    body =StringField('', validators=[DataRequired(), Length(0, 60, message='too long')],
                       render_kw={'placeholder': 'todo', "class": 'form-control shadow-sm my-input' })
    hidden = StringField('', render_kw ={ 'type':'hidden','display': None})


@todo_main.route('/todo', methods=['GET'])
def index():
    todo = Todo.query.all()
    return render_template('todo_index.html', todos = todo)

@todo_main.route('/api/todo/add', methods=['POST'])
def add():
    body= request.get_json()
    current_time = datetime.utcnow()
    todo = Todo(body= body['body'],
                ct = current_time,
                done = 0
                )
    db.session.add(todo)
    db.session.commit()
    return 'saved'

@todo_main.route('/api/todo/mark', methods=['POST'])
def mark():
    received = request.get_json()
    body = received['content'].strip()
    todo = Todo.query.filter_by(body= body).first()
    if received['action'] == 'add_check':
        todo.done = 1
        db.session.commit()
    if received['action'] == 'remove_check':
        todo.done = 0
        db.session.commit()
    return 'updated'


@todo_main.route('/api/todo/delete', methods=['POST'])
def delete():
    received = request.get_json()
    body = received['content'].strip()
    todo = Todo.query.filter_by(body= body).first()
    if received['action'] == 'remove_todo':
        db.session.delete(todo)
        db.session.commit()
    else:
        abort(404)
    return 'updated'



