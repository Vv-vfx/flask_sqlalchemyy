import os

config_data = dict(os.environ)

POSTGRES_DB = config_data.get('POSTGRES_DB','blog_base')
POSTGRES_USER = config_data.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = config_data.get('POSTGRES_PASSWORD', '12345')
SECRET_KEY = config_data.get('SECRET_KEY', 'ksdfljfmsdlfsywergywuerg')
SECURITY_PASSWORD_SALT = config_data.get('SECURITY_PASSWORD_SALT', 'QWERTY')
POSTGRES_PORT = config_data.get('POSTGRES_PORT', '5432')

# for docker
DSN = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@pg:{POSTGRES_PORT}/{POSTGRES_DB}"

# for local
# DSN = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"

DB_ECHO = True
