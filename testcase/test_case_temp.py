# 日期: 2023/7/26 8:02
# 工具: PyCharm
# Python版本: 3.10
import pytest
import allure
from tools.SendRequest import *
from log.GetLogger import GetLog
from tools.operation_yaml import read_yml_file, clear_yml

from tools.run_case import run_case

log = GetLog.get_logger()


@pytest.fixture(scope="session", autouse=True)
def wd():
    print("执行")
    clear_yml()


class TestLogin:
    # 测试方法
    @pytest.mark.parametrize('case', read_yml_file("test_login_demo1.yml"))
    def test_login(self, case):
        log.info("开始执行用例" + case["name"])
        allure.dynamic.feature(case["feature"])
        allure.dynamic.title(case["name"])
        run_case(case)

    @pytest.mark.parametrize('case', read_yml_file("test_userinfo.yml"))
    def test_userinfo(self, case):
        log.info("开始执行用例"+case["name"])
        allure.dynamic.feature(case["feature"])
        allure.dynamic.title(case["name"])
        run_case(case)

# 在收集完测试用例后才会执行
# def pytest_collection_modifyitems(items):
#     print('\npytest 收集到的所有测试用例：\n', items)
#
#     for item in items:
#         # 打印出每条参数化后的测试用例路径以及每条测试用例的ids
#         print('---' * 10)
#         print('用例名：', item.name)
#         print('用例节点：', item.nodeid)
