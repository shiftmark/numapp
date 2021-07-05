# Build for listener/worker - include requirements.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PYTHONUNBUFFERED=1

COPY ./app /app
ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
