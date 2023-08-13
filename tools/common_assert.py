# 作者: 张波
# 日期: 2023/7/26 17:06
# 工具: PyCharm
# Python版本: 3.10
import jsonpath

from log.GetLogger import GetLog

log = GetLog.get_logger()


def common_assert(response, validate):
    log.info("正在调用断言公共方法...")
    # 获取响应数据
    result = response.json()
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
    # # 获取预期数据
    # expect = case.get('expect')
    # # 断言响应状态码
    # log.info("正在调用断言状态码...")
    # assert response.status_code == 200, "响应status:{}  预期status:{}".format(response.status_code, 200)
    # # 断言code
    # log.info("正在调用断言code...")
    # assert result.get('code') == expect.get('code'), "响应code:{}  预期code:{}".format(result.get("code"), expect.get("code"))
    # # 断言msg
    # log.info("正在调用断言msg...")
    # assert result.get('msg') == expect.get('msg'), "响应msg:{}  预期msg:{}".format(result.get("msg"), expect.get("msg"))
