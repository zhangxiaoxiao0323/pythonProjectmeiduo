import os
from utils.YamlUtil import YamlReader


# 获取当前目录
current = os.path.abspath(__file__)
# 获取当前项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(current))
# 定义config目录路径
_confgi_path = BASE_DIR+os.sep+"config"
# 定义conf.yml的绝对路径
_confgi_file = _confgi_path+os.sep+"conf.yml"
# 定义logs文件的路径
_log_path = BASE_DIR+os.sep+"logs"


def get_config_path():
    return _confgi_path


def get_config_file():
    return _confgi_file


def get_log_path():
    return _log_path
# 读取配置文件


class ConfigYalm:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    def get_conf_url(self):
        return self.config[0]["BASE"]["test"]["url"]

    def get_conf_log(self):
        return self.config[0]["BASE"]["log_level"]

    def get_conf_log_extension(self):
        return self.config[0]["BASE"]["log_extension"]


if __name__ == '__main__':
    conf_read = ConfigYalm()
    print(conf_read.get_conf_url())
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())
    print(_log_path)
