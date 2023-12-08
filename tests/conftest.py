import pytest
from app.db_modules.create_db import create_DB, drop_DB


@pytest.fixture(scope="session", autouse=True)
def test_db():
    print('Этот блок будет выполнен перед запуском тестов')
    create_DB()
    yield
    print('Этот блок будет выполнен после окончания работы тестов')
    # drop_DB()
