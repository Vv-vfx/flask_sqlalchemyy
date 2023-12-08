from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddArticleForm(FlaskForm):
    author_login = StringField('author_login', validators=[DataRequired()])
    article_heading = StringField('article_heading', validators=[DataRequired()])
    article_body = StringField('article_body', validators=[DataRequired()])

