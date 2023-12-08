from dotenv import dotenv_values

config = dict(dotenv_values(dotenv_path=".env.shared"))

# print(config)
# exit()
TEST_DB_NAME = config['TEST_DB_NAME']
DB_USER = config['DB_USER']
BD_PASSWORD = config['BD_PASSWORD']
SECRET_KEY = config['SECRET_KEY']

DSN = f"postgresql+psycopg2://{DB_USER}:{BD_PASSWORD}@localhost:5432/{TEST_DB_NAME}"
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{BD_PASSWORD}@localhost/{TEST_DB_NAME}"
DB_ECHO = True

