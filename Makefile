start:
	docker compose up -d --build

up:
	docker compose up -d

stop:
	docker compose stop

down:
	docker compose down

build:
	docker compose build

log:
	docker compose logs nevelichki-streamlit --follow --tail 100

restart: stop up

pipenv_lock:
	docker compose run --rm nevelichki-streamlit bash -c "pip install pipenv && PIPENV_TIMEOUT=9999 PIPENV_INSTALL_TIMEOUT=9999 PIPENV_VENV_IN_PROJECT=1 pipenv lock"
