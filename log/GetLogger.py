# 导包
import logging.handlers
import os

from config.config import base_path


# 新建类
class GetLog:
    # 新建日志器变量
    __loger = None

    # 新建获取日志器方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if cls.__loger is None:
            # 获取日志器
            cls.__loger = logging.getLogger()
            # 修改默认级别
            cls.__loger.setLevel(logging.INFO)
            log_path = base_path + os.sep + 'log' + os.sep + "test.log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm =logging.Formatter(fmt)
            # 将格式器添加到处理器
            th.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__loger.addHandler(th)
        # 返回日志器
        return cls.__loger
if __name__ == '__main__':
    log=GetLog.get_logger()
    log.info("测试信息级别")
    log.error("测试错误级别")