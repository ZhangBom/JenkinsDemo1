# 作者: 张波
# 日期: 2023/7/26 17:06
# 工具: PyCharm
# Python版本: 3.10
import jsonpath

from log.GetLogger import GetLog
from tools.common_assert_mysql import *

log = GetLog.get_logger()


def common_assert(response, validate):
    log.info("正在调用断言公共方法...")
    # 获取响应数据
    result =True
    for i in validate:
        # 如果是eq 验证是否相等
        if "eq" in i.keys():
            yaml_result = i.get("eq")[0]
            actual_result = jsonpath.jsonpath(response.json(), yaml_result)
            expect_result = i.get("eq")[1]
            if type(actual_result[0]) == int:
                expect_result = int(expect_result)
            log.info("实际结果：" + str(actual_result[0]))
            log.info("期望结果：" + str(expect_result))
            assert actual_result[0] == expect_result
        # 如果是include 验证是否包含
        if "include" in i.keys():
            yaml_result = i.get("include")[0]
            actual_result = jsonpath.jsonpath(response.json(), yaml_result)
            expect_result = i.get("include")[1]
            if type(actual_result[0]) == int:
                expect_result = int(expect_result)
            log.info("实际结果：" + str(actual_result[0]))
            log.info("期望结果：" + str(expect_result))
            assert expect_result in actual_result[0]
        if "eq_data" in i.keys():
            actual_result = i.get("eq_data")[0]
            # actual_result = jsonpath.jsonpath(response.json(), yaml_result)
            expect_result = restore_data(method="select_data", sql=i.get("eq_data")[1])
            if type(actual_result) == int:
                expect_result = int(expect_result)
            log.info("实际结果：" + str(actual_result))
            log.info("期望结果：" + str(expect_result))
            assert expect_result == actual_result
        if "select_data" in i.keys():
            yaml_result = i.get("select_data")[0]
            actual_result = jsonpath.jsonpath(response.json(), yaml_result)[0]
            expect_result = restore_data(method="select_data", sql=i.get("select_data")[1])
            if type(actual_result) == int:
                expect_result = int(expect_result)
            log.info("实际结果：" + str(actual_result))
            log.info("期望结果：" + str(expect_result))
            assert expect_result == actual_result

