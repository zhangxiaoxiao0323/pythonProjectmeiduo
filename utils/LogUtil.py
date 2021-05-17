import logging
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
    def __int__(self, log_file, log_name, log_level):
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







