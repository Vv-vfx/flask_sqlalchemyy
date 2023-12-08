from app.models import (
    Author,
    Articles,
    Role,
)

from faker import Faker

from app.db_modules.create_db import db

Faker.seed(11)
fake = Faker('ru_RU')

authors_list = []

role_admin = Role(role_name='admin', description='Администратор')
role_user = Role(role_name='user', description='Просто пользователь')

for _ in range(25):
    full_name = fake.name().split()

    author = Author(login=fake.user_name(), password=fake.password(length=20), email=fake.unique.email(),
                    lastname=full_name[0], name=full_name[1], surname=full_name[2], postal_address=fake.address(),
                    articles=[
                        Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=1000)),
                        Articles(article_heading=fake.text(max_nb_chars=20),
                                 article_body=fake.text(max_nb_chars=1000))],
                    author_roles=role_user)

    authors_list.append(author)

maxim = Author(login='maxxx', password=fake.password(length=20), email=fake.unique.email(), lastname=full_name[0],
               name=full_name[1], surname=full_name[2], postal_address=fake.address(),
               articles=[
                   Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=1000)),
                   Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=1000)),
                   Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=1000))],
               author_roles=role_admin)

johnnn = Author(
    login='johnnn', password=fake.password(length=20), email=fake.unique.email(), lastname=full_name[0],
    name=full_name[1],
    surname=full_name[2], postal_address=fake.address(),
    articles=[
        Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=300)),
        Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=300)),
        Articles(article_heading=fake.text(max_nb_chars=20), article_body=fake.text(max_nb_chars=300))],
    author_roles=role_admin)

authors_list.extend([maxim, johnnn])

if __name__ == '__main__':
    print(authors_list)
