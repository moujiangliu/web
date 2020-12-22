import time
import unittest

from base.driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from page.page_cart import PageCart

class TestOrder(unittest.TestCase):
    driver = None
    order = None

    @classmethod
    def setUpClass(cls) -> None:
        # 实例化driver
        cls.driver = GetDriver().get_driver('chrome')
        # 调用登录成功的方法
        PageLogin(cls.driver).page_login_success()
        time.sleep(5)

        # 实例化order的page页面
        cls.order = PageOrder(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        # 销毁，善后操作-关闭浏览器
        GetDriver().close_driver()

    def setUp(self) -> None:
        # 添加商品
        PageCart(self.driver).page_add_cart('雪纺连衣裙')
        self.order.base_click_index()

    def test_order_pay(self):
        try:
            self.order.page_submit_order()
            time.sleep(3)
            self.assertIn('支付成功', self.driver.page_source)
        except Exception as e:
            self.order.base_get_image()
            raise e

















