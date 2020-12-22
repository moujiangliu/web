import time
import unittest

from base.driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin

'''
1. 强相关性，不建议这样写，用例和用例之间，一定要有独立性
有依赖性的话，一个用例失败了，是会影响到另外一个用例的执行
'''

class TestCart(unittest.TestCase):
    driver = None
    cart = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver('chrome')
        # 调用登录成功的方法
        PageLogin(cls.driver).page_login_success()
        # 等待一会
        time.sleep(3)
        # 实例化购物车页面
        cls.cart = PageCart(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.close_driver()

    # 用例1
    def test_add_cart(self):
        pass

    # 用例2
    def test_delete(self):
        # 调用删除方法
        self.cart.page_delete()
        time.sleep(3)
        # 断言
        self.assertFalse(self.cart.page_if_delete_button_exist())

























