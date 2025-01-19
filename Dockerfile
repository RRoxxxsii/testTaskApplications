FROM python:3.12.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install poetry==1.8.2
RUN poetry config virtualenvs.create false

WORKDIR /proj/

COPY . /proj/

RUN poetry install --no-dev

CMD alembic upgrade head && python -m src
