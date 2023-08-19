# 作者: 张波
# 日期: 2023/8/7 20:20
# 工具: PyCharm
# Python版本: 3.10
import json

import yaml
from string import Template


def case_template(raw_dict):
    # 定义一个列表存放用例
    case_list = list()
    case_name = list()
    # 读取yaml文件中的用例
    for yaml_case in raw_dict:
        # 获取用例内容
        values = yaml_case["test"]
        # 判断该用例是否需要参数化
        if "parametrize" in values.keys():
            param_name = values["parametrize"][0]
            # 新建一个字典
            param = dict()
            del values["parametrize"][0]
            # 用例参数化
            for parm in values["parametrize"]:
                for i in range(0, len(parm)):
                    param[param_name[i]] = parm[i]
                # 替换参数并将case重新实例化为字典
                case = yaml.safe_load(Template(json.dumps(values, ensure_ascii=False)).safe_substitute(param))
                del case["parametrize"]
                # 如果extract为空则不需要提取，删除extract
                if "extract" in case.keys() and case["extract"] == 'None':
                    del case["extract"]
                case_list.append(case)
                case_name.append(case["name"])
        else:
            case_list.append(values)
            case_name.append(values["name"])
    return case_list
