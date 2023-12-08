
from app.db_modules.create_db import create_DB, drop_DB
from app.models import create_table
from app.db_modules.query_db import fill_db_fakes_info
from app.db_modules.query_db import (
    get_all_articles,
    get_article_by_id,
    add_article_by_author_login,
)
from flask import redirect, render_template, request
from app.forms import AddArticleForm
from app import app


@app.route("/")
def index_page():
    print("REQUEST")
    print(request.cookies)

    articles = get_all_articles()
    # articles = [1,2,3,4,5]
    return render_template("index.html", articles=articles)

@app.route("/article/<int:article_id>")
def article_by_id(article_id):
    article = get_article_by_id(article_id)
    print(article)
    return render_template("article.html", article=article)

@app.route("/article/add/", endpoint='article_add', methods=['GET', 'POST'])
def add_one_article():
    form = AddArticleForm()
    if form.validate_on_submit():
        author_login = form.author_login.data
        article_heading = form.article_heading.data
        article_body = form.article_body.data
        add_article_by_author_login(author_login, article_heading, article_body)
        return redirect('/')
    return render_template('add_article.html', form=form)
    


@app.route("/contacts")
def contacts_page():
    print(1111)
    return render_template("contacts.html")


@app.cli.command("create-new-db")
def create_new_db():
    with app.app_context():
        create_DB()

@app.cli.command("fill-db-fakes")
def fill_db_fakes():
    with app.app_context():
        fill_db_fakes_info()

@app.cli.command("drop-db")
def drop_db():
    with app.app_context():
        drop_DB()

# if __name__ == '__main__':
#     # start_db()
#     app.run(debug=True)