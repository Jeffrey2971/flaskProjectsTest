import os


def find():
    file = open('test.txt', mode='r')
    for i in file:
        if i == "80":
            os.system('taskkill /f /im QQ.exe')
        else:
            print("没找到80")
    file.close()


if __name__ == '__main__':
    find()
