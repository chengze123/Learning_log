login_staus = False
status_dict = {
    'username': None,
    'status': False,
}


def auth(f):
    """
    你的装饰器完成，访问被装饰函数之前写一个三次登录认证功能
    登陆成功，让其访问被装饰的函数，登陆没有成功，不让访问
    :param f:
    :return:
    """

    def inner(*args, **kwargs):
        """访问函数之前的操作、功能"""
        if status_dict['status']:
            ret = f(*args, **kwargs)
            """访问函数之后的操作、功能"""
            return ret
        else:
            login()
    return inner


def login(*args, **kwargs):
    username = input('请输入用户名').strip()
    password = input('请输入密码').strip()
    if username == 'daisy' and password == '123':
        print('登录成功')
        status_dict['username'] = username
        status_dict['status'] = True
        #ret = f(*args, **kwargs)
        #return ret
    else:
        print('登录失败')


def register():
    pass


@auth
def article():
    print('欢迎访问文章页面')
article()
@auth
def comment():
    print('欢迎访问评论页面')
comment()
@auth
def dairy():
    print('欢迎访问日记页面')
dairy()