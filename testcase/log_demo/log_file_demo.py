import logging


logger = logging.getLogger('log_file_demo')
logger.setLevel(logging.INFO)
fh_stream = logging.StreamHandler()
# 写入文件
fh_file = logging.FileHandler('./test.log')
# 设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.DEBUG)
# 定义输出格式
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
# 添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
# 运行输出
logger.info('this is info')
logger.debug('this is debug')
logger.warning('this is warning')
