# 作者: 张波
# 日期: 2023/7/28 17:39
# 工具: PyCharm
# Python版本: 3.10
import pytest as pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', 'temp', '--clean-alluredir'])