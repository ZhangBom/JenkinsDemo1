import requests
import json

from config.config import base_url

from log.GetLogger import GetLog

log = GetLog.get_logger()

# 获取session对象
sess = requests.session()


def send_request(**kwargs):
    # 路径
    kwargs["url"] = base_url + kwargs["url"]
    log.info("请求参数详情:" + str(kwargs))
    res = sess.request(**kwargs)
    return res
