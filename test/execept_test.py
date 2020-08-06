# python异常
'''
try:
    放置可能出现异常的代码块
except BaseException:    BaseException：所有异常的父类，该参数可省写
    出现异常时执行的方法
else:
    未出现异常时执行该方法，如上面出现异常，该块里面的内容不执行
'''
try:
    trr = 1/0
except:
    print("分母不能为0")
else:
    print("这边是继续执行完的数据")
finally:
    print("无论异常是否发生，都执行该代码块")