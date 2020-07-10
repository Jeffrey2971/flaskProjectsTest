import random
import time


# 无参
def total_time(fun):
    def f():
        old_time = time.time()
        fun()
        new_time = time.time()
        total = new_time - old_time
        print(total)

    return f


# 有参
def total_time_params(fun):
    def f(*args, **kwargs):
        old_time = time.time()
        fun(*args, **kwargs)
        new_time = time.time()
        total = new_time - old_time
        print(total)

    return f


@total_time
def add():
    time.sleep(3)
    return 3


@total_time_params
def sub(a, b):
    print('略略略')
    time.sleep(2)
    print('asdasdasd')
    return a - b


def check_permission(permission):
    def love_learn(fun):
        def f(*args, **kwargs):
            if permission > 90:
                fun(*args, **kwargs)
            else:
                print('休息')

        return f

    return love_learn


@check_permission(89)
def learn():
    print('i love learn')


if __name__ == '__main__':
    # sub(8, 5)
    learn()
