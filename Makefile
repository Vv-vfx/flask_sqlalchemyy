
# Запустить приложение в режиме production
start-prod:
	docker compose up --build prod-backend

# Запустить приложение в режиме dev
start-dev:
	echo "Запускаем приложение c сервером gunicorn"
	docker compose up --build dev-backend

# Запустить приложение c сервером gunicorn
start-gunicorn:
	echo "Запускаем приложение c сервером gunicorn"
	docker compose up --build gunicorn-backend

# Остановить и удалить все контейнеры в Docker
docker-clear:
	echo "Останавливаем и удаляем все контейнеры в Docker"
	docker stop $(shell docker ps -aq)
	docker rm $(shell docker ps -aq)