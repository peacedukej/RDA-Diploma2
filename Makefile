.PHONY: build up down migrate

build:
	docker-compose build
up:
	docker-compose up
down:
	docker-compose down

migrate: build up