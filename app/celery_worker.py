from celery import Celery
from celery.utils.log import get_task_logger
from get_value_from_db import get_time
from time import sleep

cel = Celery(
    'worker',
    broker='amqp://guest@broker:5672',
    backend='redis://backend:6379',
)

# Logger for displaying messages in terminal
cel_log = get_task_logger(__name__)

@cel.task()
def sleep_for(item_id):
    duration = get_time(item_id)
    sleep(duration)
    cel_log.info('Worker done.')
    return {'Slept for': f'{duration} seconds'}
