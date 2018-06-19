 #自己定义一个异常
class MyError(Exception):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
def get_pwd():
    pwd = input('请输入密码:')
    if len(pwd)<6:
        raise MyError('密码小于6位不符合要求!!!',12,'女')
try:
    get_pwd()
except Exception as re:
    print('遇到异常，内容是%s'% re.age)
