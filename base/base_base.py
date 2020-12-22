import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tool.logger import Logger
from tool.test import get_path

# 实例化Logger，获取一个日志的入口
log = Logger().get_logger()

class Base():
    def __init__(self, driver):
        '''原则：调试，print一样，代码的一个解释'''
        log.info('正在初始化获取driver对象:{}'.format(driver))
        self.driver = driver

    # 找元素（加等待，显性等待）
    # 缺省参数，在定义函数的时候有默认参数
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        log.info('正在查找元素:{}元素,最多等待:{}s'.format(loc,timeout))
        # locator
        # loc = By.XPATH, '//div[@class="member-login"]/a[text()="登录"]'
        # self.base_find_element(loc[0], loc[1])   ---> 原始写法
        # self.driver.find_element(*loc)
        # 显性等待
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
        return el

    # 点击   如果在page层想要修改等待时间和频率，那么也需要在base层也要添加位置参数
    def base_click(self, loc, timeout=20, poll_frequency=1):
        log.info('正在点击:{}元素'.format(loc))
        # self.base_find_element(loc).click()
        self.base_find_element(loc,timeout=timeout,poll_frequency=poll_frequency).click()

    # 输入（清空、输入）
    def base_input(self, loc, value):
        log.info('正在输入:{}元素,输入值是:{}'.format(loc,value))
        # 获取元素
        el = self.base_find_element(loc)
        # 先清空
        el.clear()
        # 在输入
        el.send_keys(value)

    # 获取文本内容
    def base_get_text(self, loc):
        log.info('定位到元素{}'.format(loc))
        return self.base_find_element(loc).text

    # 切换window
    def base_switch_to_window(self, title):
        for handle in self.driver.window_handles:
            log.info('开始切换窗口')
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                log.info('窗口切换成功')
                break

    # 切换iframe
    def base_switch_to_frame(self, frame):
        log.info('切换至iframe页面:{}元素'.format(frame))
        self.driver.switch_to.frame(self.base_find_element(frame))

    # 切回默认页面
    def base_switch_to_default(self):
        log.info('切换至默认页面')
        self.driver.switch_to.default_content()

    # 截图操作
    def base_get_image(self):
        log.info('开始截图=======>')
        self.driver.get_screenshot_as_file(get_path('image', '{}.png').format(time.strftime('%Y-%m-%d_%H_%M_%S')))

    # 添加cookie
    def base_add_cookie(self, name, value):
        '''
        添加cookie
        :param name:
        :param value:
        :return:
        '''
        log.info('正在添加cookie======>')
        self.driver.add_cookie({'name':name, 'value':value})

    # 做断言，检查点
    # 判断元素是否存在
    def base_if_is_exist(self, loc):
        '''
        如果可以找到元素，那么就返回True，反之则返回False
        '''
        try:
            log.info('判断{}元素是否存在'.format(loc))
            self.base_find_element(loc, timeout=2)
            log.info('{}元素是存在的'.format(loc))
            return True
        except:
            log.error(f'{loc}元素不存在')
            return False

    # 进入首页
    def base_click_index(self):
        loc = By.XPATH, '//*[@id="doc-topbar-collapse"]/ul/li[1]/a'
        log.info('点击回到首页')
        self.base_click(loc)

    # @property 加上这个就会把函数变成属性（前提是你的函数是不需要传参数的）
    @property
    def base_page_source(self):
        log.info('获取源码')
        return self.driver.page_source

    # js脚本封装
    def base_js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.base_js('window.scrollTo(200,1000);)
        '''
        self.driver.execute_script(script)
        log.info('Execute JavaScript scripts. {}'.format(script))


    # 窗口最大化
    def base_max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.base_max_window()
        '''
        self.driver.maximize_window()
        log.info('Set browser window maximized')

    # 设置窗口大小
    def base_set_window(self, wide, high):
        '''
        Set browser window wide and high

        Usage:
        driver.base_set_window(wide, high)
        '''
        self.driver.set_window_size(wide, high)
        log.info('Set browser window %s wide and %s high.' % (wide, high))

    # 获取元素的属性
    def base_get_attribute(self, loc, attribute):
        '''
        Gets the value of an element attribute

        Usage:
        driver.base_get_attribute(By.CLASS_NAME, 'btn-go', 'value')
        '''
        element = self.base_find_element(loc)
        log.info('Gets the value %s of an element attribute %s.' %(attribute, loc))
        return element.get_attribute(attribute)

    # 是否展现这个元素
    def base_get_display(self, loc):
        '''
        Gets the element to display,The return result is true of false.

        Usage:
        driver.base_get_display(By.CLASS_NAME, 'btn-go')
        '''
        el = self.base_find_element(loc)
        log.info('The %s element is exits or not' % loc)
        return el.is_displayed()

    # 获取窗口的title
    def base_get_title(self):
        '''
        Get window title.

        Usage:
        driver.base_get_title()
        '''
        log.info('Get window title.')
        return self.driver.title

    # 选择下拉框
    def base_select(self, loc, value):
        '''
        Constuctor. A check is made that the given element is, indeed, a SELECT tag. If it is then an
        UnexpectedTagNameException is thrown.

        :Args:
        - css - element SELECT element to wrap
        - value - The value to match against

        Usage:
            <select name='NR' id='nr'>
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.base_select('#nr', 20)
            loc = By.CLASS_NAME, 'btn-go'
            drive.base_select(By.CLASS_NAME, 'btn-go', '20')
        '''
        # 先定位到元素
        el = self.base_find_element(loc)
        # 实例化Select下拉框，获取select下拉框里面的option的值
        Select(el).select_by_value(value)

    # 向前
    def base_forward(self):
        self.driver.forward()
        log.info('Click forward on current page.')

    # 向后
    def base_back(self):
        self.driver.back()
        log.info('Click backd on current page.')

    # 刷新页面
    def base_refresh(self):
        self.driver.refresh()
        log.info('Refresh on current page.')

    # 获取alert弹窗的文本信息
    def base_get_alert_text(self):
        '''
        Gets the text of the Alert.

        Usage:
        driver.base_get_alert_text()
        '''
        log.info('Gets the text of the Alert.')
        return  self.driver.switch_to.alert.text

    # 接收alert弹窗
    def base_accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.base_accept_alert()
        '''
        self.driver.switch_to.alert.accept()
        log.info('Accept warning box')

    # 取消alert弹窗
    def base_dismiss_alert(self):
        '''
        Dismisses the alert available

        Usage:
        driver.base_dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()
        log.info('Dismiss the alert available.')

    # 隐性等待
    def base_implicitly_wait(self, secs):
        '''
        Implicitly wait.All element on the page.

        Usage:
        driver.base_implicitly_wait(10)
        '''
        self.driver.implicitly_wait(secs)
        log.info('wait for %d seconds.' % secs)


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get('http://121.42.15.146:9090/mtx/')
    base = Base(driver)
    base.base_add_cookie('PHPSESSID', 'ngm6u8s3rsvpibk23fg1g0jfg1')
    driver.refresh()
    driver.implicitly_wait()





