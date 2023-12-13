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

from flask_login import UserMixin

from app.db_modules.create_db import db


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))


class Role(db.Model):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    role_name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"Role(role_name={self.role_name!r})"

    def __str__(self) -> str:
        return f"{self.role_name}"


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]
    email: Mapped[str] = mapped_column(String(100), unique=True)
    author_roles: Mapped["Role"] = relationship(secondary="roles_users",
                                                backref=backref('users_with_roles', lazy='dynamic'))
    lastname: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    surname: Mapped[Optional[str]]
    postal_address: Mapped[Optional[str]] = mapped_column(String(200))
    articles: Mapped[Optional[List["Articles"]]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, username={self.username!r}, password={self.password!r}, email={self.email!r}, \
                author_roles={self.author_roles!r}, lastname={self.lastname!r}, name={self.name!r}, \
                surname={self.surname!r}, postal_address={self.postal_address!r}, articles={self.articles!r})"


class Articles(db.Model):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    article_heading: Mapped[str]
    article_body: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="articles")

    def __repr__(self) -> str:
        return f'Article(id={self.id!r}, article_heading={self.article_heading!r}, \
        article_body={self.article_body!r}, user_id={self.user_id!r}, user={self.user!r})'


def create_table():
    print('Создаём таблицы')
    db.create_all()
