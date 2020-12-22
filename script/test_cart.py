import time
import unittest

from base.driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin

'''
1. 强相关性，不建议这样写，用例和用例之间，一定要有独立性
有依赖性的话，一个用例失败了，是会影响到另外一个用例的执行
这种方式不建议

2. 不想让用例1和用例2有强依赖关系，我们应该怎么做？？
（1）函数级别setup和teardown，可以实现不让用列之间的有依赖性，
    缺点：每次都的重新创建driver，销毁driver，效率低，耗时
（2）
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

    # 每一个函数执行完之后都会执行一次
    def tearDown(self) -> None:
        # 点击首页
        self.cart.base_click_index()

    def test_add_cart(self):
        '''
        添加商品至购物车
        '''
        # try...except.. 捕获异常，目的：就是为了截图，截图之后把错误信息抛出去
        try:
            self.cart.page_add_cart('雪纺连衣裙')
            time.sleep(2)
            self.assertIn('加入成功', self.cart.base_page_source)
        except Exception as e:
            self.cart.base_get_image()
            # 抛出错误信息
            raise e


    # 用例2: 删除购物车商品
    def test_delete(self):
        # 调用删除方法
        try:
            self.cart.page_delete()
            time.sleep(3)
            # 断言
            self.assertFalse(self.cart.page_if_delete_button_exist())
        except Exception as e:
            self.cart.base_get_image()
            raise e



























