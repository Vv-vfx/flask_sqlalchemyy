from flask_wtf import FlaskForm
from wtforms import (PasswordField,
                     BooleanField,
                     EmailField,
                     TextAreaField,
                     SubmitField,
                     StringField)
from wtforms.validators import DataRequired, Email


class AddArticleForm(FlaskForm):
    article_heading = StringField('Заголовок статьи', validators=[DataRequired()])
    article_body = TextAreaField('Тело статьи', validators=[DataRequired()])


class SendQuestion(FlaskForm):
    question = TextAreaField('Вопрос')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')


class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()])
