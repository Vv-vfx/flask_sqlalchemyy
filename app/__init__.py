from flask_login import LoginManager

from app.config.config import SECRET_KEY, SECURITY_PASSWORD_SALT, DSN
from app.db_modules.create_db import db
from flask import Flask, request, redirect, url_for, flash
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SECURITY_PASSWORD_SALT"] = SECURITY_PASSWORD_SALT

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Чтобы перейти на эту страницу, авторизуйтесь'
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        # Получаем конечный маршрут
        endpoint = request.endpoint
        # Настраиваем своё сообщение на основе endpoint
        if endpoint == 'main.profile':
            message = "Чтобы получить доступ к странице Профиля, авторизуйтесь"
        elif endpoint == 'main.db_info':
            message = "Чтобы получить доступ к странице Данные из БД, авторизуйтесь"
        else:
            message = "Чтобы получить доступ к этой странице, авторизуйтесь"

        flash(message, 'info')
        return redirect(url_for('auth.login'))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, cli_group='main')

    Migrate(app, db)

    return app
