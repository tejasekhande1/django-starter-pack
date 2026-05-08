migrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

startapp:
	docker compose exec web python manage.py startapp $(name)

build:
	docker compose up --build

run:
	docker compose up

stop:
	docker compose down