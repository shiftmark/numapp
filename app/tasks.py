from celery import Celery
from time import sleep
import os

cel = Celery('tasks',
             broker='amqp://guest@broker:5672',
             backend='redis://backend:6379'
             )

@cel.task
def add(x, y):
    sleep(3)
    return x + y
