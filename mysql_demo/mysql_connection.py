import MySQLdb
import pymysql

class MySQLConnection:
    # 数据库连接地址
    host = "rm-8vbs625tz967xx08x8o.mysql.zhangbei.rds.aliyuncs.com"
    # 用户名
    username = "wjz"
    # 密码
    password = "Weijiuzhu123!!"
    # 连接端口号
    port = 3306
    # 要连接的数据库
    dataBase = "business"

    def queryMySQLdbData(self, sql):
        try:
            connectPool = MySQLdb.connect(host=self.host, port=self.port,
                                 user=self.username, passwd=self.password, db=self.dataBase, charset="utf8")
            cursor = connectPool.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except:
            print("获取数据库连接失败")
        finally:
            connectPool.close()

    def queryPyMySQLData(self, sql):
        try:
            connectPool = pymysql.connect(host=self.host, port=self.port,
                                 user=self.username, passwd=self.password, db=self.dataBase)
            cursor = connectPool.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except:
            print("获取数据库连失败")
        finally:
            connectPool.close()
