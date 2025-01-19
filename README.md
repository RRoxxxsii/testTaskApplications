# Application Service - Test Task

-----

## Run Locally

Clone the project:

```bash
  git clone
```

Copy `.envExample` to `.env`:

```bash
cp .envExample .env
```

Run with docker-compose:
```bash
docker compose up --build
```

-----

## Available endpoints:

**POST /v1/applications/**

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/applications/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_name": "user",
  "description": "Hello WORLD!"
}'
```
```
{
  "id": 207,
  "user_name": "string",
  "description": "string",
  "created_at": "2025-01-19T13:33:57.628018Z"
}
```
``STATUS 201``

**GET /v1/applications/**

```bash
curl -X 'GET' \
  'http://0.0.0.0:8000/v1/applications/?page=1&size=10&filter_user_name=lol' \
  -H 'accept: application/json'
```
```
[
  {
    "id": 1,
    "user_name": "lol",
    "description": "string",
    "created_at": "2025-01-19T05:24:54.762996Z"
  }
]
```
```STATUS 200```

----
## Main dependencies

**PYTHON 3.12.7**

### Infrastructure

* PostgreSQL
* Docker
* Kafka

### Python libs

* FastAPI
* Pydantic
* Alembic
* asyncpg
* SQLAlchemy
* pytest
* pytest_asyncio
