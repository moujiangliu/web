# 三、 业务逻辑层 --->就相当于最终的调用层，它就会调用组合好的组合的业务，实现业务逻辑
# 用到单元测试框架的层

import unittest
from page.page_login import PageLogin
from base.opendriver import OpenDriver
from base.driver import GetDriver
from tool.readExcel_list_dict import ReadExcel
from tool.readExcel import ReadExcel
import page
import ddt

# 参数化，逆向数据、正向数据   data-->列表套字典 （文件：excel，txt, yaml）
# data = [
#     {'username':'moujiang', 'password': 'moujiang1'},
#     {'username':'beihe', 'password': 'beihe'},
#     {'username':'moujiang1', 'password': 'moujiang1'}
# ]

# 列表套字典
# data = ReadExcel().get_excel(['username', 'password'])

# 列表套列表
data = ReadExcel().get_excel()

@ddt.ddt()
class Login(unittest.TestCase):
    # 类属性-->全局变量，在类方法和实例方法去用，都可以
    driver = None
    login = None

    # 前置函数 -->打开浏览器，实例化page对象
    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器  这个实例方法里面的driver是个局部变量
        # cls.driver = OpenDriver().driver('chrome')
        # driver就已经是类属性  login也是类属性
        cls.driver = GetDriver.get_driver('chrome')
        cls.login = PageLogin(cls.driver)

    # 后置函数 -->关闭浏览器
    @classmethod
    def tearDownClass(cls) -> None:
        # 原生的关闭浏览器的方式
        # cls.driver.quit()

        # 封装好的，关闭浏览器
        GetDriver.close_driver()

    # 业务的测试用例-->测试业务是否正常登录，输入具体的跟业务有关的参数，还有断言
    @ddt.data(*data)
    def test_login(self, data):
        # data -->字典
        # 调用登录业务
        # self.login.page_login(data['username'], data['password'])  # 列表套字典
        self.login.page_login(data[0], data[1])   # 列表套列表

        # 调用进行断言的方法，断言 登录链接那个按钮是否存在，登录失败（错误账户）--return True
        # 登录成功（账户正确）--> return false
        result = self.login.page_el_if_is_exist()
        # 断言
        # self.assertFalse(result)
        # self.assertTrue(result)

        # 断言
        self.assertEqual(self.driver.title, '用户登录 - 码同学实战系统')




























