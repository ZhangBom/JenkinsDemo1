# 作者: 张波
# 日期: 2023/8/8 9:29
# 工具: PyCharm
# Python版本: 3.10
import jsonpath
import yaml
import time
from tools.SendRequest import *
from tools.common_assert import common_assert
from tools.extract_key import extract_key
from tools.operation_yaml import read_yml_key
from tools.common_assert_mysql import *
from string import Template
import jinja2


def run_case(case):
    log.info("用例开始执行...")
    # 替换测试用例中的关联值
    # print(case)
    # 单独替换request请求中的数据，避免后置处理中包含嵌套或提取关联数据异常
    case = yaml.safe_load(Template(json.dumps(case, ensure_ascii=False)).safe_substitute(read_yml_key()))
    try:
        # 调用接口执行方法
        response = send_request(**case["request"])
        # 数据提取
        if "extract" in case.keys():
            extract_key(response, case)
        # 再次替换测试用例中的关联值做数据库校验
        case = yaml.safe_load(Template(json.dumps(case, ensure_ascii=False)).safe_substitute(read_yml_key()))
        # 结果断言
        if "validate" in case.keys():
            common_assert(response, case["validate"])
        # 数据回滚
        if "restore" in case.keys():
            for item in case["restore"]:
                restore_data(method=item, sql=case["restore"][item])
                # restore_data(method=item, sql=value)
        # 执行结果写入excel
        log.info("用例执行完成")
    except Exception as e:
        err = "错误:" + format(e)
        log.info("用例执行未通过:" + err)
        raise
