from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.config.config import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_PORT

)

db = SQLAlchemy()


def create_DB():
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user=POSTGRES_USER, password=POSTGRES_PASSWORD, port=POSTGRES_PORT)
    print("Подключились к postgres")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL запрос на завершение всех соединений с базой
    terminate_query = f"""
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = '{POSTGRES_DB}'
    AND pid <> pg_backend_pid();
    """
    # Выполняем запрос
    cursor.execute(terminate_query)
    # удаляем базу, если база существует
    cursor.execute(f'DROP DATABASE IF EXISTS {POSTGRES_DB}')
    # создаем базу
    cursor.execute(f'create database {POSTGRES_DB}')
    print("Создали базу")
    # Закрываем соединение
    cursor.close()
    connection.close()


def drop_DB():
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user=POSTGRES_USER, password=POSTGRES_PASSWORD, port=POSTGRES_PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Удаляем базу данных
    cursor.execute(f'drop database {POSTGRES_DB}')
    print("Удалили базу")
    # Закрываем соединение
    cursor.close()
    connection.close()
