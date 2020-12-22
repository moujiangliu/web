'''
封装具体的你需要打开哪一个浏览器，然后获取哪一个浏览器的driver
'''
from selenium import webdriver


class OpenDriver():
    def driver(self, browser='chrome'):
        '''
        (可写可不写)，好处：功能分明，然后查看起来比较方便
        主要是返回封装好的driver
        :return:
        '''
        driver = self.get_driver(browser=browser)
        return driver

    def get_driver(self, browser):
        '''
        具体的各种浏览器driver的封装过程
        :param browser:
        :return:
        '''
        if browser == 'firefox' or browser == 'ff':
             driver = webdriver.Firefox()
             return driver
        elif browser == 'chrome' or browser == 'ch':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'ie' or browser == 'internet explorer':
            driver = webdriver.Ie()
            return driver
        elif browser == 'safari' or browser == 'sf':
            driver = webdriver.Safari()
            return driver
        elif browser == '360':
            driver = webdriver.Ie()
            return driver
        else:
            raise NameError('Not found %s browser,you must enter"firefox,chrome,ie,safari"' % browser)


if __name__ == '__main__':
    op = OpenDriver()
    driver = op.driver('ff')
    driver.get('http://121.42.15.146:9090/mtx/')




