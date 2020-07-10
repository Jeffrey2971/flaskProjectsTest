from time import sleep

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(a, b):
    print('准备开始')
    print(a + b)
    sleep(5)
    return a + b


if __name__ == '__main__':
    print('略略略')

    add.delay(4, 5)

    print('执行结束')
