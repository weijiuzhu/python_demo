'''
创建一个类，class为类的标识参数
def __init__(self, name, age) 为类的构造函数，self:表示当前对象，后面的参数为裁员变量
'''
class UserEntity:
    __add = "天涯海角"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("对象被销毁")

    def printUser(self):
        print(self.__class__)
        print("姓名：", self.name, ",年龄：", self.age)