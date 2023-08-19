# 作者: 张波
# 日期: 2023/8/8 8:03
# 工具: PyCharm
# Python版本: 3.10
import json
import re

import random

import jsonpath
import yaml
from tools.operation_yaml import write_yml_key
from log.GetLogger import GetLog
from tools.random_generate import *

log = GetLog.get_logger()


def extract_key(response, case):
    if case.get("extract"):
        log.info("需要提取关联值存储到extract.yml文件")
        extract = yaml.safe_load(case.get("extract"))
        for key, value in extract.items():
            if 'random' in value:
                # 提取random函数参数的正则表达式模式
                data = {key: jsonpath.jsonpath(response.json(),
                                               random_generate(pattern=r'random\((\d+),(\d+)\)', data=value))[0]}
                # 写入临时文件保存
                write_yml_key(data, "extract.yml")
                log.info("关联数据".format(data))
            else:
                data = {key: jsonpath.jsonpath(response.json(), value)[0]}
                # 写入临时文件保存
                write_yml_key(data, "extract.yml")
                log.info("关联数据".format(data))
