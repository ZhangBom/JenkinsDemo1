# 作者: 张波
# 日期: 2023/8/8 9:29
# 工具: PyCharm
# Python版本: 3.10
import yaml

from tools.SendRequest import *
from tools.common_assert import common_assert
from tools.extract_key import extract_key
from tools.operation_yaml import read_yml_key
from string import Template

def run_case(case):
    log.info("用例开始执行...")
    # 替换测试用例中的关联值
    case = yaml.safe_load(Template(json.dumps(case, ensure_ascii=False)).safe_substitute(read_yml_key()))
    try:
        # 调用接口执行方法
        response = send_request(**case["request"])
        # 断言
        common_assert(response, case["validate"])
        if "extract" in case.keys():
            extract_key(response, case)
        # 执行结果写入excel
        log.info("用例执行通过")
    except Exception as e:
        err = "错误:" + format(e)
        log.info("用例执行未通过:" + err)
        raise
