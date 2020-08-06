# 对外部文件的目录操作

'''
1.write:该方法像文件中写入字符串，不设置当前位置，默认为文件第一行开头起写入，相同字符写入时不会重复
2.open:该方法，打开一个文件
3.read:读取打开文件里面的内容
4.close:关闭打开的文件
5.rename:修改当前传入文件的名称
6.mkdir：创建新的文件目录
7.chdir：切换操作的文件目录
8.rmdir：删除指定的文件目录
9.getcwd：查看当前所在的目录
10.os包提供的是操作文件目录的方法
'''
import os

file1 = open("D:/demo/code/python/pythen_demo/test1234.text", "r+", encoding="utf-8")
file1.write("你好，世界！")
re = file1.read()
print(re)
file1.close()

os.rename("D:/demo/code/python/pythen_demo/test123.text", "D:/demo/code/python/pythen_demo/test1234.text")
os.mkdir("D:/demo/code/python/pythen_demo/text")
os.chdir("D:/demo/code/python/pythen_demo/text")
os.rmdir("D:/demo/code/python/pythen_demo/text")
print(os.getcwd())
