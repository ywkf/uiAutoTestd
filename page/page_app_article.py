from time import sleep

import page
from base.app_base import AppBase


class PageAppArticle(AppBase):

    # 点击同意
    def page_click_agree(self):
        sleep(5)
        self.base_click(page.app_agree)

    # 点击频道
    def page_click_channel_btn(self, channel):
        loc = page.get_channel_loc(channel)
        self.base_click(loc)

    # 点击搜索栏
    def page_click_search_column(self):
        self.base_click(page.app_search_column)

    # 搜索栏输入
    def page_input_search_column(self, text):
        self.base_input(page.app_search_column2, text)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.app_search_btn)

    # 查找频道
    def page_click_channel(self, click_text):
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    # 查找文章
    def page_click_article(self, click_text):
        loc = page.get_article_loc(click_text)
        self.app_base_wipe_up(loc)

    # 组合搜索方法
    def page_app_search(self, text):
        self.page_click_search_column()
        sleep(1)
        self.page_input_search_column(text)
        self.page_click_search_btn()





