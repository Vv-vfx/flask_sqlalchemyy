### Пример создания и заполнения БД postgresql локально 

#### Если проект в самом начале:
```
flask db init
```

Создать базу:
```
flask create-new-db
```
Удалить базу:
```
flask drop-db
```
Подготовить миграции:
```
flask db migrate
```
Обновление базы по миграциям:
```
flask db upgrade
```
Заполняем базу фейковыми данными:
```
flask fill-db-fakes
```
Запускаем приложение:
```
flask run
```