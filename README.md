# Ecommerce Backend

Standardized FastAPI backend repository for the multi-vendor marketplace.

## Tech Stack
- **Python**: 3.11+
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Configuration**: Pydantic Settings (`.env`)
- **Testing & Linting**: Pytest, HTTPX, Ruff

## Project Structure
```text
ecommerce_backend/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
├── database/
│   └── ecommerce.sql
├── src/
│   └── ecommerce_backend/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── config.py
│       └── api/
│           ├── __init__.py
│           └── v1/
│               ├── __init__.py
│               ├── router.py
│               └── endpoints/
│                   ├── __init__.py
│                   └── health.py
└── tests/
    ├── __init__.py
    └── test_health.py
```

## Local Setup

1. **Create and activate a virtual environment**
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```

## Run the Application

```bash
uvicorn ecommerce_backend.main:app --reload
```

- **Root**: `http://127.0.0.1:8000/`
- **Health Check**: `http://127.0.0.1:8000/api/v1/health`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Run Tests & Lint

```bash
pytest
ruff check .
```