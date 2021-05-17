# 导包
import yaml
from utils.YamlUtil import YamlReader
# 定义yaml文件路径

# 获取文件流对象
# with open('./data.yml', 'r', encoding='utf-8')as f:
# 通过safe_load 读取文件流
# r = yaml.safe_load(f)
# print('读取到的数据：', r)
# print('读取到的数据的数据类型：', type(r))

# with open('./data1.yml', 'r', encoding='utf-8') as f:
# r = yaml.safe_load_all(f)
# for i in r:
# print(i)
res1 = YamlReader('./data.yml').data()
res = YamlReader('./data1.yml').data_all()
print(res1)
print(res)

