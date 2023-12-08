from sqlalchemy.orm import Session
from app.db_modules.demo_authors import authors_list
from sqlalchemy import select
from app.db_modules.create_db import db


from app.models import (
    Author,
    Articles,
)

def add_article_by_author_login(author_login, article_heading, article_body):
    
    author = Author(
        login=author_login,
        password='123',
        email='fake.email()',
        lastname='ИВАААААААААН',
        name='ИВАААААААААН',
        surname='ИВАААААААААН',
        postal_address='ИВАААААААААН',
        articles=[Articles(article_heading=article_heading,article_body=article_body),]
        )
    session = db.session
    session.add(author)
    session.commit()
    print('Добавили статью')
    
     

    

def fill_db_fakes_info():
    session = db.session
    print('Заполняем базу 25 авторами и статьями')
    session.add_all(authors_list)
    session.commit()
    print('*' * 100)


def get_all_articles_by_author_login_v1(author_login):

    session = db.session

    stmt = select(Author).where(Author.login==author_login)

    print(f"Все статьи для автора с логином {author_login}")

    all_articles_by_login_author = []
    
    for author in session.scalars(stmt):
        for article in author.articles:
            all_articles_by_login_author.append(article.article_heading, article.article_body)
    
    return all_articles_by_login_author

def get_all_articles():

    session = db.session
    stmt = select(Articles)

    all_articles = []
    
    for article in session.scalars(stmt):
        all_articles.append((article.id, article.article_heading, article.article_body[:60]))
    
    return all_articles

def get_all_articles_by_author_login_v2(author_login):

    session = db.session

    stmt = session.query(Author).filter(Author.login==author_login).all()

    print(f"Все статьи для автора с логином {author_login}")
    
    for author in stmt:
        for article in author.articles:
            print(f'Заголовок статьи: "{article.article_heading}"')
            print(f'Тело статьи: "{article.article_body}"')


        print(article)

def get_article_by_id(article_id):

    session = db.session

    stmt = session.query(Articles).get(article_id)
    return stmt

    


if __name__ == '__main__':
    fill_db_fakes_info()