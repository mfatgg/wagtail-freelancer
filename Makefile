BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
WHITE ?= \033[1;37m
COFF ?= \033[0m

.PHONY: all help shell shell-dev build build-dev runserver runserver-dev collectstatic collectstatic-dev makemigrations makemigrations-dev migrate migrate-dev load-user-data load-website-data load-many-posts superuser superuser-dev shutdown shutdown-dev shutdown-volumes shutdown-volumes-dev logs logs-dev logs-interactive logs-interactive-dev coverage-django lint lint-fix test-project test-website test-users docker

all: help

help:
	@echo -e "\n$(WHITE)Available commands:$(COFF)"
	@echo -e "$(CYAN)make build-dev$(COFF)        - Builds development images"
	@echo -e "$(CYAN)make collectstatic-dev$(COFF)  - Runs the Django's collectstatic command in development"
	@echo -e "$(CYAN)make load-oscar-data$(COFF)   - Loads initial data from Django Oscar app's fixtures"
	@echo -e "$(CYAN)make load-user-data$(COFF)   - Loads initial data from Django user accounts app's fixtures"
	@echo -e "$(CYAN)make logs-dev$(COFF)        - Shows the logs for the django development app"
	@echo -e "$(CYAN)make makemigrations-dev$(COFF) - Runs django's makemigrations command in the development container"
	@echo -e "$(CYAN)make migrate-dev$(COFF)      - Runs django's migrate command in the development container"
	@echo -e "$(GREEN)make runserver-dev$(COFF)    - Runs the django development app, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make setup-dev$(COFF)      - (Re-)Setup all data in the development container"
	@echo -e "$(RED)make shutdown-dev$(COFF)    - Stops the django development app"
	@echo -e "$(RED)make shutdown-volumes-dev$(COFF) - Shuts down the running services and deletes volumes in development"


build-dev:
	@echo -e "$(CYAN)Building website images for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml build

collectstatic-dev:
	@echo -e "$(CYAN)Running django collectstatic in develoment:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py collectstatic $(cmd)

deploy-media-dev:
	@echo -e "$(CYAN)Deploy media data from local dir:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web cp -r media/* /mediafiles/

dump-user-data:
	@echo -e "$(CYAN)Dumping original data to Django fixtures:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python manage.py dumpdata --indent 2 auth.user freelancer wagtailcore wagtailimages > wagtail_freelancer/freelancer/fixtures/freelancer.json

load-oscar-data:
	@echo -e "$(CYAN)Populating initial data from Django fixtures:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py load_oscar_data

load-user-data:
	@echo -e "$(CYAN)Populating initial data from Django fixtures:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py loaddata wagtail_freelancer/freelancer/fixtures/freelancer.json

logs-dev:
	@echo -e "$(CYAN)Checking logs:$(COFF)"
	@docker-compose -f docker-compose-dev.yml logs

makemigrations-dev:
	@echo -e "$(CYAN)Running django makemigrations for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py makemigrations $(cmd)

migrate-dev:
	@echo -e "$(CYAN)Running django migrations in development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py migrate $(cmd)

reset-db-dev:
	@echo -e "$(CYAN)Reset database for development:$(COFF)"
	@rm -f db.sqlite3

runserver-dev:
	@echo -e "$(GREEN)Starting Docker container with the app in development.$(COFF)"
	@docker-compose -f docker-compose-dev.yml up -d
	@echo -e "$(CYAN)App ready and listening at http://127.0.0.1:8000.$(COFF)"

setup-dev: shutdown-volumes-dev reset-db-dev migrate-dev collectstatic-dev deploy-media-dev load-user-data load-oscar-data runserver-dev

shutdown-dev:
	@echo -e "$(RED)Stopping Docker container with the app in development.$(COFF)"
	@docker-compose -f docker-compose-dev.yml down

shutdown-volumes-dev:
	@echo -e "$(CYAN)Stopping services and deleting volumes:$(COFF)"
	@docker-compose -f docker-compose-dev.yml down --volumes
