
'''
添加商品至购物车
删除购物车商品
'''
import time
from base.base_base import Base
import page

class PageCart(Base):
    '''删除购物车商品'''
    # 点击右上角的购物车进入购物车页面
    def page_click_right_cart(self):
        self.base_click(page.cart_click_right_cart)
    # 点击删除按钮
    def page_click_delete_button(self):
        self.base_click(page.cart_delete_button)
    # 点击确定删除
    def page_confirm_delete(self):
        self.base_click(page.cart_confirm_delete)

    # 判断删除按钮是否存在
    def page_if_delete_button_exist(self):
        self.base_if_is_exist(page.cart_delete_button)

    '''添加商品至购物车'''
    # 输入框输入商品名字
    def page_input_good_name(self, good):
        self.base_input(page.cart_search_input, good)
    # 点击搜索按钮
    def page_click_search_button(self):
        self.base_click(page.cart_search_button)
    # 点击商品（需要切换窗口）
    def page_click_goods(self):
        # 先去查找商品详情页的list，显性等待
        self.base_find_element(page.cart_into_detail)
        self.base_click(page.cart_into_detail)
        self.base_switch_to_window(page.cart_detail_window_title)
    # 点击商品规格（粉色，M）- time.sleep(3)
    def page_click_goods_spec(self):
        self.base_click(page.cart_pink_spec)
        time.sleep(3)
        self.base_click(page.cart_size_spec)
    # 点击加入购物车
    def page_click_add_cart(self):
        self.base_click(page.cart_add_cart)

    # todo: 组合业务区域
    '''删除购物车商品'''
    def page_delete(self):
        self.page_click_right_cart()
        self.page_click_delete_button()
        self.page_confirm_delete()

    '''组合业务2: 添加商品至购物车'''
    def page_add_cart(self, good):
        # 输入框输入商品名字
        self.page_input_good_name(good)
        # 点击搜索
        self.page_click_search_button()
        # 点击商品
        self.page_click_goods()
        # 点击选择商品规格
        self.page_click_goods_spec()
        # 点击加入购物车
        self.page_click_add_cart()
















