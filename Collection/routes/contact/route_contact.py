from flask import redirect, render_template, Blueprint, request, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

# check email field if it is available


main = Blueprint('contact', __name__, template_folder='templates' )


class ContactForm(FlaskForm):
    name = StringField('Hello, what is your name?', [DataRequired(message='不能为空'), Length(3, 10, message='3-10个字符')])
    email = StringField('What is your email?', [DataRequired(message='不能为空'), Length(3,50, message='太长或太短'), Email(message='不是邮箱')])
    content = TextAreaField('Words you want to say', [DataRequired(message='不能为空'), Length(3, 500, message='需在500字以内' )] )



@main.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        pass

    return render_template('contact.html', form = form)