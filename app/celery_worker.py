import celery
from get_value_from_db import get_time
from time import sleep

cel = celery.Celery(
    'cel',
    broker='amqp://guest@broker:5672',
    backend='redis://backend:6379',
)

# Logger for displaying messages
cel_log = celery.utils.log.get_task_logger(__name__)

@cel.task()
def queue_item(item_id):
    tm = get_time(item_id)
    sleep(tm)
    cel_log.info('Celery done.')
    return {'Done': f'in {tm} seconds'}

             