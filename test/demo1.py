# 数据打印到控制台
print("你好！世界")
print("hello World")

# Numbers（数字）
# 整数
a = 1
# 浮点数
b = 1.0
c = 1.1
print(a, b, c)
# String（字符串）
# 表示字符串
str = "String"
# 截取字符串  str[起始位置，结束位置，步长]
print(str[0:-4])
# 表示字符串，不同的写法
char = 'String123'
print(char)
# List（列表）
list1 = [1, 2, 3, 's', 't', 'r', "in", "ing", True]

print(list1[0:8:2])

# Tuple（元组）
tuple1 = (1, 3, 5, '7', '9', True, list1)
print(tuple1[-1][0:5])
# Dictionary（字典）
dic = {}
dic[1] = "test"
dic['ss'] = 123456
dic["tt"] = tuple1
print(dic)

print(2**32)

#算数运算符
a = 21
b = 10
c = 0
c = a + b
print("1 - c 的值为：", c)
c = a - b
print("2 - c 的值为：", c)
c = a * b
print("3 - c 的值为：", c)
c = a / b
print("4 - c 的值为：", c)
c = a % b
print("5 - c 的值为：", c)
# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)
a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)
