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
