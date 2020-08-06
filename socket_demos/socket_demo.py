import socket

class SocketServer:
    def sockerService(self):
        # 创建socket对象
        soc = socket.socket()
        # 获取当前主机名称
        host = socket.gethostname()
        # 定义当前服务端口号
        port = 12306
        # 将主机，端口绑定到当前服务
        soc.bind((host, port))

        # 监听客户端连接
        soc.listen(3)
        while True:
            # 建立客户端连接
            cli, add = soc.accept()
            print( '连接地址：', add)
            cli.send("欢迎访问菜鸟教程！".encode("utf-8"))
            cli.close()  # 关闭连接

    def socketClient(self):
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12306  # 设置端口号
        # 建立一个客户端连接，连接到当前主机及端口
        s.connect((host, port))
        str = s.recv(1024)
        print(str.decode("utf-8"))
        s.close()