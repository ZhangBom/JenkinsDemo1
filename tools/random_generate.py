# 作者: 张波
# 日期: 2023/8/19 17:08
# 工具: PyCharm
# Python版本: 3.10
import re
import random

# def replace_random(match):
#     return str(random.randint(match.group(1), match.group(2)))

data = "{'userid1': '$.data.contentList[random(1,50)].userId[random(1,20)]','userid1_status': '$.data.contentList[random(1,50)].userId'}"

pattern = r'random\((\d+),(\d+)\)'  # 正则表达式模式

random_values = {}  # 用于存储已生成的随机数值

def replace_random(match):
    lower = int(match.group(1))
    upper = int(match.group(2))
    key = (lower, upper)
    if key not in random_values:
        random_values[key] = random.randint(lower, upper)
    return str(random_values[key])

result = re.sub(pattern, replace_random, data)

print(result)
