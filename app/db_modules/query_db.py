from werkzeug.security import generate_password_hash

from app.db_modules.demo_authors import authors_list
from sqlalchemy import select
from app.db_modules.create_db import db

from app.models import (
    User,
    Articles,
    Role,
)


def add_article_by_username(user, article_heading, article_body):
    article = Articles(
        article_heading=article_heading,
        article_body=article_body,
        user_id=user.id
    )
    session = db.session
    session.add(article)
    session.commit()
    print('Добавили статью')


def fill_db_fakes_info():
    session = db.session
    print('Заполняем базу 25 авторами и статьями')
    session.add_all(authors_list)
    session.commit()
    print('*' * 100)


def check_author_in_db(email):
    return User.query.filter_by(email=email).first()


def add_author_to_db(username, email, password):
    role_user = Role(role_name='user', description='Просто пользователь')

    author = User(
        username=username,
        password=generate_password_hash(password, method='scrypt'),
        email=email,
        author_roles=role_user
    )
    session = db.session
    session.add(author)
    session.commit()



def get_all_articles_by_author_login_v1(username):
    session = db.session

    stmt = select(User).where(User.username == username)

    print(f"Все статьи для автора с логином {username}")

    all_articles_by_login_author = []

    for author in session.scalars(stmt):
        for article in author.articles:
            all_articles_by_login_author.append((article.article_heading, article.article_body))

    return all_articles_by_login_author


def get_all_articles():
    session = db.session
    # stmt = select(Articles)
    stmt = session.query(Articles).all()

    all_articles = []

    # for article in session.scalars(stmt):
    for article in stmt:
        all_articles.append((article.id, article.article_heading, article.article_body[:60]))

    return all_articles


def get_article_by_id(article_id):
    session = db.session

    stmt = session.query(Articles).get(article_id)
    return stmt


def get_db_info():
    session = db.session

    stmt = session.query(User).all()
    # print(stmt)

    return stmt


if __name__ == '__main__':
    fill_db_fakes_info()
