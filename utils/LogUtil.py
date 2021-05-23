import logging
import os.path

from config import Conf
import datetime
from config.Conf import ConfigYalm
# 定义日志映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# 封装log工具类
# 创建类
class Logger:
    # 定义函数
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level


# 编写输出控制台文件
        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 设置logger级别
        self.logger.setLevel(log_l[self.log_level])
        # 判断handlers是否存在
        if not self.logger.handlers:
            #输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter()
            fh_stream.setFormatter(formatter)
            #写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            #添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 初始化参数数据
# 日志文件名，日志文件级别
# 日志文件名称=log目录+当前时间+扩展名
log_path = Conf.get_log_path()
current_time = datetime.datetime.now().strftime('%Y-%m-%d')
log_extension = ConfigYalm().get_conf_log_extension()
log_file = os.path.join(log_path, current_time+log_extension)
log_level = ConfigYalm().get_conf_log()


def my_log(log_name=__file__):
    return Logger(log_file=log_file, log_name=log_name, log_level=log_level).logger


if __name__ == '__main__':
    my_log().debug("this is debug")









