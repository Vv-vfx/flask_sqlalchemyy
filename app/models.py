from typing import (
    List,
    Optional,
)
from sqlalchemy import (
    ForeignKey,
    String,
    BigInteger,
    Identity

)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship, backref,
)

from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    RoleMixin,
    login_required,
)

from app.db_modules.create_db import db


# class Base(DeclarativeBase):
#     pass

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    role_name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(String(100))


class Author(db.Model, UserMixin):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    login: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    author_roles: Mapped["Role"] = relationship(secondary="roles_users",
                                                backref=backref('authors_with_roles', lazy='dynamic'))
    lastname: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
    postal_address: Mapped[str] = mapped_column(String(200))
    articles: Mapped[List["Articles"] | None] = relationship(back_populates="author", cascade="all, delete-orphan")

    # def __repr__(self) -> str:
    #     return f"Author(id={self.id!r}, login={self.login!r}, password={self.password!r}, email={self.email!r}, \
    #             lastname={self.lastname!r}, name={self.name!r}, surname={self.surname!r}, \
    #             postal_address={self.postal_address!r}, author_article={self.author_article!r})"


class Articles(db.Model):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    article_heading: Mapped[str]
    article_body: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="articles")

    # def __repr__(self) -> str:
    #     return f'Article(id={self.id!r}, article_heading={self.article_heading!r}, \
    #     article_body={self.article_body!r}, author_id={self.author_id!r}, author={self.author!r})'


def create_table():
    print('Создаём таблицы')
    db.create_all()
