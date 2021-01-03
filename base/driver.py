from base.opendriver import OpenDriver
import page
# import os
# import sys
# base_path = os.path.abspath(os.path.join(os.getcwd(),'..'))
# sys.path.append(base_path)

class GetDriver():
    # 单例模式的思想，只是一个衍生
    # 获取driver，标记
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls, browser):
        if cls.driver is None:
            cls.driver = OpenDriver().get_driver(browser)
            cls.driver.maximize_window()
            cls.driver.get(page.url)
            # cls.driver.get('http://121.42.15.146:9090/mtx/')
            return cls.driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        # 为了程序的健壮性，需要先判断不为空的时候再执行
        if cls.driver:
            cls.driver.quit()

            # 必须 置空
            cls.driver = None


if __name__ == '__main__':
    driver = GetDriver()
    driver.get_driver('chrome')
    driver.get_driver('chrome')
    driver.get_driver('chrome')










