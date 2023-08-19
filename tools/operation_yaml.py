# 作者: 张波
# 日期: 2023/7/30 21:22
# 工具: PyCharm
# Python版本: 3.10
# 清空yml
import json

import yaml

from config.config import *
from log.GetLogger import GetLog
from tools.case_template import case_template

log = GetLog.get_logger()


def clear_yml(file_name='extract.yml'):
    log.info("正在调用接口关联变量yml文件清除方法...")
    file_name = base_path + os.sep + "testdata" + os.sep + file_name
    with open(file_name, 'w', encoding='utf-8') as f:
        f.truncate()


# 写入yml
def write_yml_key(data, file_name='extract.yml'):
    log.info("正在调用用例写入yml文件方法...")
    file_name = base_path + os.sep + "testdata" + os.sep + file_name
    with open(file_name, 'a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取yml_key
def read_yml_key(file_name='extract.yml'):
    log.info("正在调用接口关联读取方法...")
    file_name = base_path + os.sep + "testdata" + os.sep + file_name
    with open(file_name, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


# 读取yml用例
def read_yml_file(file_name='test_user_audit.yml'):
    log.info("正在调用接口关联读取方法...")
    file_name = base_path + os.sep + "testdata" + os.sep + file_name
    with open(file_name, 'r', encoding='utf-8') as f:
        raw_dict = yaml.load(f, Loader=yaml.FullLoader)
        return case_template(raw_dict)

if __name__ == '__main__':
    read_yml_key()
