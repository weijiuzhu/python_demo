from mysql_demo.mysql_connection import MySQLConnection

if __name__ == '__main__':
    db = MySQLConnection()
    sql = "SELECT * FROM credit_assist_result where CONS_NO = '%s'" % ('0410953330')
    data = db.queryPyMySQLData(sql)
    print(data)
