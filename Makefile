up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

createsuperuser:
	docker-compose exec backend python manage.py createsuperuser

migrate:
	docker-compose exec backend python manage.py migrate

collectstatic:
	docker-compose exec backend python manage.py collectstatic --noinput

logs:
	docker-compose logs -f

test:
	docker-compose exec backend python manage.py test

clean:
	docker system prune -f

.PHONY: up down build createsuperuser migrate collectstatic logs test clean
