import pymysql
from utils.LogUtil import my_log


class Mysql:
    def __init__(self,host, user, password, database, charset='utf-8', port=3306):
        self.log = my_log()
        # 链接database
        self.conn = pymysql.connect(
            host='192.168.3.126',
            user='',
            password='',
            database='',
            charset='utf-8',
            port=8080
        )
        # 获取执行sql的光标对象
        self.curses = self.conn.cursor()
# 创建查询，执行方法

    # 单个查询
    def fetchone(self, sql):
        self.curses.execute(sql)
        return self.curses.fetchone()

    # 多个查询
    def fetchall(self, sql):
        self.curses.execute(sql)
        return self.curses.fetchall()

    def exec(self, sql):
        try:
            if self.conn and self.curses:
                self.curses.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True
    # 关闭对象

    def __del__(self):
        if self.curses is not None:
            self.curses.close()

        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    mysql = Mysql(
        '192.168.3.220',
        'test',
        'meiduo',
        '123456',
        charset='utf-8',
        port=8080
    )
    res = mysql.fetchall("select  * form md_org")
    res_exec = mysql.exec("update ....")
    print(res)
