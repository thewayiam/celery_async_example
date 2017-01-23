import time
from celery import Celery

app = Celery('tasks', broker='pyamqp://', backend='redis://localhost')

@app.task
def add(x, y):
    return x + y

@app.task
def multiple(x, y):
    return x * y

@app.task
def total_sum(numbers):
    return sum(numbers)
