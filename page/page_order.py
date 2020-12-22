# -*- coding:utf-8 -*-

'''
提交订单
'''
import page
from base.base_base import Base


class PageOrder(Base):
    # 点击右上角的购物车进入购物车页面
    def page_order_click_cart(self):
        self.base_click(page.order_click_cart)
    # 勾选第一个商品
    def page_order_click_first_cart(self):
        self.base_click(page.order_click_first_good)
    # 点击提交结算
    def page_order_click_pay(self):
        self.base_click(page.order_click_pay)
    # 选择货到付款
    def page_order_goods_to_pay(self):
        self.base_click(page.order_goods_to_pay)
    # 点击提交订单
    def page_order_click_submit(self):
        self.base_click(page.order_click_submit)

    '''组合业务区域'''
    def page_submit_order(self):
        self.page_order_click_cart()
        self.page_order_click_first_cart()
        self.page_order_click_pay()
        self.page_order_goods_to_pay()
        self.page_order_click_submit()

