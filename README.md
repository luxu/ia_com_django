# PROJECT DJANGO WITH IA

### Tools used in this repository:
- uv: Python packaging in Rust [https://docs.astral.sh/uv/#highlights](https://docs.astral.sh/uv/#highlights)
- groq: Model supplier [https://groq.com/](https://groq.com/)

## Create virtualenv
cd ia_com_django
````bash
uv venv .venv
````
## Access VM
````bash
source venv/bin/activate
````
## Generate requirements.txt use uv
````bash
uv sync --no-dev
````
````bash
uv pip freeze > requirements.txt
````
