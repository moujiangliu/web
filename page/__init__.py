# init这层，我希望把一些容易变化的内容放在这进行管理
'''整个项目的配置项'''

# 项目的url
from selenium.webdriver.common.by import By

url = 'http://121.42.15.146:9090/mtx/'

'''以下是登录页面的配置信息'''
login_link = By.CSS_SELECTOR, '.menu-hd>a:nth-child(3)'
login_input_username = By.XPATH, '//label[text()="登录账号"]/following-sibling::input'
login_input_password = By.XPATH, '//label[text()="登录密码"]/following-sibling::input'
login_button = By.XPATH, '//button[text()="登录"]'

'''以下是搜索商品、添加商品至购物车的配置信息'''
cart_search_input = By.CSS_SELECTOR, '#search-input'
cart_search_button = By.CSS_SELECTOR, '#ai-topsearch'
cart_into_detail = By.CSS_SELECTOR, 'ul.search-list>li:nth-child(1)'
cart_pink_spec = By.CSS_SELECTOR, 'li[data-value="粉色"]'
cart_size_spec = By.CSS_SELECTOR, 'li[data-value="M"]'
cart_add_cart = By.CSS_SELECTOR, 'button[title="加入购物车"]'
cart_detail_window_title = 'ZK爆款连衣裙'

'''以下是删除购物车的配置信息'''
cart_click_right_cart = By.XPATH, '(//*[text()="购物车"])[2]'
cart_delete_button = By.XPATH, '(//tbody/tr/td[5])[1]/a'
cart_confirm_delete = By.XPATH, '//*[text()="确定"]'

'''以下是提交订单的配置信息'''
order_click_cart = By.CSS_SELECTOR, '.am-icon-shopping-cart'
order_click_first_good = By.XPATH, '(//tbody/tr/td[1])[1]/label/span/i[2]'
order_click_pay = By.CSS_SELECTOR, 'button.separate-submit'
order_goods_to_pay = By.CSS_SELECTOR, '.payment-list>li:nth-child(1)'
order_click_submit = By.XPATH, '//button[text()="提交订单"]'





































































