# numapp
API endpoint to execute long-running tasks using a queue.

Requirements:
1. docker: https://docs.docker.com/get-docker/
2. docker-compose: https://docs.docker.com/compose/install/

Setup:
1. Download the repository
2. In the folder root, create a ".env" file with the postgres details:
   DB_PASS=<choose password>
   DB=<choose database name>
Note: The username has the default value - "postgres". If you want to connect to database from outside of container, uncomment the line indicated in docker-compose.yml file, before running the command mentioned below.

Run the app:
1. From the directory root, run "docker-compose up -d"

Docker will download the required images (Postgres, Rabbitmq, Redis, FastApi).

API calls, via http://localhost/docs or Postman:
1. POST: http://localhost/item
   The valid "item_id"s for POST are "a" and "b", which return 5 and 12 respectively
2. GET: http://localhost/result/<result id>
   The result id is returned by POST
