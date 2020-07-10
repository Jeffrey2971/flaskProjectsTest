import random
from time import sleep, time


def calc_time(fun):
    def wrapper(*args, **kwargs):
        before = time()
        fun(*args, **kwargs)
        after = time()
        print("游戏时间", after - before)

    return wrapper


@calc_time
def play(game):
    print("你正在打游戏%s" % game)
    sleep(3)
    print("游戏结束")

def can_play(can):
    def can_play_wrapper(fun):
        def wrapper(*args, **kwargs):
            if random.randrange(10) > can:
                fun(*args, **kwargs)
            else:
                print('do homework')
        return wrapper
    return can_play_wrapper

@can_play(10)
def play_game():
    print("开心的玩游戏")

if __name__ == '__main__':
    play_game()
