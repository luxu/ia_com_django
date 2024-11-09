# PROJECT DJANGO WITH IA

### Tools used in this repository:
- uv: Python packaging in Rust [https://docs.astral.sh/uv/#highlights](https://docs.astral.sh/uv/#highlights)
- groq: Model supplier [https://groq.com/](https://groq.com/)

## Install Dependencies
cd ia_com_django
````bash
uv sync --frozen
````

## Create virtualenv
````bash
uv venv .venv
````

## Access VM
````bash
source venv/bin/activate
````

## Generate requirements.txt use uv
````bash
uv export --format requirements-txt > requirements.txt
````

## Update lib
````bash
uv lock --upgrade
````

## Run commands with uv
````bash
uv run django-admin startproject <project-name> .
uv run manage.py runserver
````

## Run commands with uv
````bash

````
After all the dependencies are specified in `pyproject.toml` 
you can run `uv sync` to make sure everything is installed in your environment.

## Adding dev dependencies
````bash
uv add --dev pytest pytest-django
````

## Not to install dev dependencies in production
````bash
uv sync --no-dev --locked
````
