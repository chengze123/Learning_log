import time


# timer装饰器写在最前面
def timmer(f):  # (function index地址)
    def inner():  # inner:(function inner地址)
        start_time = time.time()
        f()  # index()(function index地址)
        end_time = time.time()
        print(f'测试本函数的执行效率(end_time-start_time)')

    return inner  # 注意返回函数名  （function inner地址）


@timmer  # index=timmer(index)
def index():
    """有很多代码"""
    time.sleep(2)
    print("欢迎登陆")


# index()
@timmer
def dairy():
    """有很多代码"""
    time.sleep(3)
    print("忘记烦恼")
dairy()
