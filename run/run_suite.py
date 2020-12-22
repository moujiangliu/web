import time
import unittest

from script.cart import TestCart
from script.test_login import Login
from tool.HTMLTestRunner import HTMLTestRunner
from tool.test import get_path

# 导入全部的测试用例测试
# suite = unittest.defaultTestLoader.discover('script', pattern='test*.py')
suite = unittest.defaultTestLoader.discover('script')

# 导入单个测试类测试
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Login)



# 路径都是相对路径 -->相对的是你的入口文件，执行文件
with open(get_path('report', '{}.html').format(time.strftime('%Y-%m-%d_%H-%M-%S')), 'wb') as f:
    HTMLTestRunner(stream=f, title='MTX商城', description='MTX商城自动化测试').run(suite)

# with open('../report/{}.html'.format(time.strftime('%Y-%m-%d_%H-%M-%S')), 'wb') as f:
#     HTMLTestRunner(stream=f, title='MTX商城', description='登录测试').run(suite)



