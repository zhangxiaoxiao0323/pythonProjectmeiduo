import utils.MysqlUtil
from config.Conf import ConfigYalm
from utils.MysqlUtil import Mysql

# 定义init_db
def init_db(db_alias):
    # 初始化数据库信息，通过配置
    db_info = ConfigYalm().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    database = db_info["db_database"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    # 初始化数据库连接
    conn = Mysql(host, user, password, database, charset, port)
    print(conn)
    return conn


if __name__ == '__main__':
    init_db('db_1')


