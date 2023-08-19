# 作者: 张波
# 日期: 2023/8/17 10:12
# 工具: PyCharm
# Python版本: 3.10
import pymysql
from log.GetLogger import GetLog

log = GetLog.get_logger()
# 数据库链接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='bidingsystem',
                     port=3306)


def restore_data(method, sql):
    print(method)
    print(sql)
    if method == 'select_data':
        return select_data(sql)
    elif method == 'update_data':
        return update_data(sql)
    elif method == 'insert_data':
        return insert_data(sql)
    elif method == 'delete_data':
        return delete_data(sql)
    else:
        log.info("方法输入异常，请检查用例")
        return False


def select_data(sql):
    log.info("执行sql:" + sql)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        re_data = "%s" % data
        log.info("查询到数据:" + re_data)
        return re_data
    except pymysql.Error as error:
        log.info("查询出错:" + str(error))
    finally:
        cursor.close()


def update_data(sql):
    log.info("执行sql:" + sql)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        log.info("数据更新成功")
    except pymysql.Error as error:
        log.info("更新出错:" + str(error))
        db.rollback()
        log.info("数据回滚")
    finally:
        cursor.close()


def insert_data(sql):
    log.info("执行sql:" + sql)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        log.info("数据插入成功")
    except pymysql.Error as error:
        log.info("插入出错:" + str(error))
        db.rollback()
        log.info("数据回滚")
    finally:
        cursor.close()

def delete_data(sql):
    log.info("执行sql:" + sql)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        log.info("数据删除成功")
    except pymysql.Error as error:
        log.info("删除出错:" + str(error))
        # 发生错误时回滚
        db.rollback()
        log.info("数据回滚")
    finally:
        cursor.close()
