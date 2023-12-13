from flask import current_app, flash
from flask_login import login_required, current_user, logout_user

from app.db_modules.create_db import create_DB, drop_DB
from app.db_modules.query_db import (fill_db_fakes_info,
                                     get_db_info,
                                     )
from app.db_modules.query_db import (get_all_articles,
                                     get_article_by_id,
                                     add_article_by_username,
                                     )
from flask import redirect, render_template, url_for, Blueprint
from app.forms import AddArticleForm, SendQuestion

main = Blueprint('main', __name__)


@main.route("/", endpoint='index')
def index_page():
    articles = get_all_articles()
    return render_template("index.html", articles=articles)


@main.route("/favicon.ico")
def favicon():
    return url_for('static', filename='favicon.ico')


@main.route('/profile/', endpoint='profile')
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route("/article/<int:article_id>")
def article_by_id(article_id):
    article = get_article_by_id(article_id)
    return render_template("article.html", article=article)


@main.route("/article/add/", endpoint='article_add', methods=['GET', 'POST'])
@login_required
def add_one_article():
    form = AddArticleForm()
    if form.validate_on_submit():
        article_heading = form.article_heading.data
        article_body = form.article_body.data
        user = current_user
        add_article_by_username(user, article_heading, article_body)
        flash(f'Спасибо, {user.username}, за добавленную статью на тему {article_heading}', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_article.html', form=form)


@main.route("/send_question", endpoint='send_question', methods=['GET', 'POST'])
@login_required
def send_question():
    print('Зашел в send_question')
    form = SendQuestion()

    if form.validate_on_submit():
        print('Зашел в if form.validate_on_submit():')
        username = current_user.username

        flash(f'Спасибо, {username} Ваш вопрос отправлен', 'success')
        return redirect(url_for(endpoint='main.index'))

    return render_template('send_question.html', form=form)


@main.route("/db_info", endpoint='db_info')
@login_required
def db_info():
    authors = get_db_info()
    return render_template("db_info.html", authors=authors)


@main.cli.command("create-new-db")
def create_new_db():
    with current_app.app_context():
        create_DB()


@main.cli.command("fill-db-fakes")
def fill_db_fakes():
    with current_app.app_context():
        fill_db_fakes_info()


@main.cli.command("drop-db")
def drop_db():
    with current_app.app_context():
        drop_DB()
