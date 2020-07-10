from time import sleep
import encodings
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task(name='tasks')
def add(a, b):
    print('准备开始')
    print(a + b)
    sleep(5)
    return a + b