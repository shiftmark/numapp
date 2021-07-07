# Build for listener/worker - include requirements.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PYTHONUNBUFFERED=1

#___________venv_________________#
#ENV VIRTUAL_ENV=/opt/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#________________________________#

COPY ./app /app
ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
