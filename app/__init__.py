from app.config.config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from app.db_modules.create_db import db
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)

# это надо обязательно, чтобы app знал о роутах
# и если импортировать раньше, то будет рекурсивный импорт
# при команде flask create-db
from app import routes 

app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY

db.init_app(app)


migrate = Migrate(app, db)

