# numapp
API endpoint to execute long-running tasks using a queue.

## Requirements:
1. docker: https://docs.docker.com/get-docker/
2. docker-compose: https://docs.docker.com/compose/install/

## Setup:
1. Download the repository
2. In the folder root, create a ".env" file with the Postgres details:


DB_PASS=<i>choose a password</i><br>
DB=<i>choose a database name</i><br>

The username has the default value - "postgres". If you want to connect to database from outside of container, uncomment the line indicated in docker-compose.yml file, before running the command mentioned below.

## Running the app:
1. From the directory root, run "docker-compose up -d"<br>
Docker will download the required images (Postgres, Rabbitmq, Redis, FastApi).

## API calls:
via http://localhost/docs or Postman:
1. POST: http://localhost/item<br>
   The valid "item_id"s for POST are "a", "b", "c", "d", which return 5, 12, 24, 48 respectively<br>
2. GET: http://localhost/result/<i>result id</i><br>
   The result id is returned by POST
