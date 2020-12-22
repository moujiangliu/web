import time
from selenium import webdriver
from base.base_base import Base
import page

'''
不变的东西（重复的东西）需要封装
变的东西，你需要做成参数，你想传什么就传什么
'''

# 该如何调用base底层的封装，1：直接从文件夹导入，from base.base import *，对Base类进行实例化；2：导入Base类，继承Base类，
class PageLogin(Base):
    # 点击登录链接，前缀page，页面层
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_input_username,username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.login_input_password, password)

    # 点击登录 如果在page层想要修改等待时间和频率，那么也需要在base层也要填加位置参数
    def page_click_login_button(self):
        # self.base_click(loc)
        self.base_click(page.login_button, timeout=20, poll_frequency=1)

    # todo 做断言，检查点，通过判断页面上是否有登录链接这个按钮来判断登录是否成功
    # 因为你要用这个值做断言，所有要return，返回这个值
    def page_el_if_is_exist(self):
        time.sleep(5)
        return self.base_if_is_exist(page.login_link)

    # 组合业务逻辑-->跟你做功能测试一样的一个组合的动作，动作顺序一样
    def page_login(self, username, password):
        # 点击登录链接
        self.page_click_login_link()
        # 输入用户名
        self.page_input_username(username)
        # 输入密码
        self.page_input_password(password)
        # 点击登录
        self.page_click_login_button()

    # 正确登录的业务（为了方便其他功能使用）
    def page_login_success(self):
        # 点击登录链接
        self.page_click_login_link()
        # 输入用户名
        self.page_input_username('moujiang')
        # 输入密码
        self.page_input_password('moujiang')
        # 点击登录
        self.page_click_login_button()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://121.42.15.146:9090/mtx/')
    # PageLogin(driver).page_login('moujiang', 'moujiang')
    login = PageLogin(driver)
    login.page_login('moujiang', 'moujiang')
    print(login.page_el_if_is_exist())
    # time.sleep(5)
    assert login.page_el_if_is_exist() == False


































