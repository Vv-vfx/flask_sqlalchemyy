from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from app.db_modules.query_db import check_author_in_db, add_author_to_db
from app.forms import SignUp, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
        # Проверяем, есть ли пользователь в БД
        user = check_author_in_db(email)
        if not user or not check_password_hash(user.password, password):
            flash('Пожалуйста проверьте свой логин/пароль')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.profile', username=user.username))

    return render_template('login.html', form=form)


@auth.route('/signup', endpoint='signup', methods=['GET', 'POST'])
def signup_post():
    form = SignUp()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Проверяем, есть ли пользователь в БД
        user = check_author_in_db(email)

        if user is not None:
            flash(f'Email {email} уже зарегистрирован в системе, пожалуйста укажите другой', 'error')
            return redirect(url_for(endpoint='auth.signup'))

        # Создаем нового пользователя
        add_author_to_db(username, email, password)
        flash(f'Успешная регистрация под ником {username}', 'success')
        logout_user()
        user = check_author_in_db(email)
        login_user(user, remember=True)
        return redirect(url_for(endpoint='main.index'))

    return render_template('signup.html', form=form)
