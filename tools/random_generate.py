# 作者: 张波
# 日期: 2023/8/19 17:08
# 工具: PyCharm
# Python版本: 3.10
import re
import random


def random_generate(pattern, data):
    """
    :param pattern: 需要匹配的正则表达式
    :param data: 需要匹配替换的字符串数据
    :return: 替换后返回字符串数据
    """
    return re.sub(pattern, replace_random, data)


random_values = {}  # 用于存储已生成的随机数值


def replace_random(match):
    """
    :param match: 匹配到的字符串数据
    :return: 生成的随机数字符数据
    """
    lower = int(match.group(1))
    upper = int(match.group(2))
    # 构建random(lower,upper)数据
    key = (lower, upper)
    # 判断该数据是否已经存在为多次使用
    if key not in random_values:
        # 没有构建过，生成随机数
        random_values[key] = random.randint(lower, upper)
    return str(random_values[key])
