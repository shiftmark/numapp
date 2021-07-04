# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# ENV PYTHONUNBUFFERED=1

# RUN python -m venv /usr/local/venv
# COPY requirements.txt .
# RUN . /usr/local/venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt

# COPY ./app /app

# #RUN pip install -r requirements.txt

# WORKDIR /app

# CMD . /usr/local/.venv/bin/activate
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PYTHONUNBUFFERED=1

COPY ./app /app
ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt