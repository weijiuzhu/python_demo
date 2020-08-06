import MySQLdb
import pymysql
'''
对数据库操作   MySQLdb.connect  pymysql.connect，获取数据连接信息
db.cursor()  获取游标
cursor.execute(sql)：执行SQL语句
cursor.fetchall()：获取数据库操作的返回值
对与SQL语句：
在书写SQL语句的时候，WHERE条件语句面  CONS_NO = '%s'" %('0410953330')  按照这种方式， %s ：是为占位符

在对数据库操作执行完成后，要关闭数据库连接
'''


def mySQLdbDemo():
    db = MySQLdb.connect(host = "rm-8vbs625tz967xx08x8o.mysql.zhangbei.rds.aliyuncs.com", port = 3306,
                         user = "wjz", passwd = "Weijiuzhu123!!", db = "business", charset='utf8')
    print(db)
    cursor = db.cursor()
    sql = "SELECT * FROM credit_assist_result where CONS_NO = '%s'" %('0410953330')
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data:
        print(d)
    db.close()

def pyMySQLDemo():
    db = pymysql.connect(host = "rm-8vbs625tz967xx08x8o.mysql.zhangbei.rds.aliyuncs.com", port = 3306,
                         user = "wjz", passwd = "Weijiuzhu123!!", db = "portal", charset="utf8")
    cursor = db.cursor()

    sql = "SELECT count(*) FROM credit_assist_result "
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)


if __name__ == '__main__':
    mySQLdbDemo()