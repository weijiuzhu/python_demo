import time
import calendar

from pip._vendor.distlib.compat import raw_input

print(time.time())
print(time.time_ns())
print(time.timezone)

print("获取当前时间：" , time.localtime(time.time()))
print("格式化时间：" + time.asctime(time.localtime(time.time())))

print("时间格式化：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


print(calendar.month(2020, 11))

# 使用lambda创建匿名函数并调用
sum = lambda a, b: a +b;
print(sum(1, 3))

str = raw_input("请输入：")
print(str)
str1 = input("请输入：")
print(str1)

file1 = open("operator.py", "r+", encoding='utf-8')
print(file1.name)
print(file1.closed)
print(file1.mode)
file1.read()
file1.close()