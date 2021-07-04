# numapp
API endpoint to execute long-running tasks using a queue.

Requirements:
1. docker: https://docs.docker.com/get-docker/
2. docker-compose: https://docs.docker.com/compose/install/

Setup:
1. Download the repository
2. In the directory root, create a .env file with the postgres details:
   DB_PASS=<choose password>
   DB=<choose database name>

Run the app:
1. From the directory root, run "docker-compose up -d"

Docker will download the required images (postgres, rabbitmq, redis, fastApi).

API Usage (via http://localhost/docs or Postman):
1. GET: http://localhost/result/<result id>
2. POST: http://localhost/item

