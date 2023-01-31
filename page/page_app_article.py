from time import sleep

import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppArticle(AppBase):

    # 点击同意
    def page_click_agree(self):
        sleep(5)
        self.base_click(page.app_agree)

    # 点击首页
    def page_click_index(self):
        self.base_click(page.app_down_index)

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

    # 获取搜索结果
    def page_get_search_results(self):
        return self.base_get_text_list(page.app_search_results)

    # 查找频道
    def page_click_channel(self, click_text):
        loc = page.get_channel_loc(click_text)
        self.app_base_right_wipe_left(page.app_channel_area, loc)

    # 查找文章
    def page_click_article(self, click_text):
        loc = page.get_article_loc(click_text)
        self.app_base_down_wipe_up(page.app_index_area, loc)
        # self.app_base_refresh_click(page.app_index_area, loc)

    # 组合查询文章方法
    def page_app_search_article(self, channel, title):
        log.info("正在调用app查询文章业务方法，频道：{}，文章title：{}".format(channel, title))
        sleep(2)
        self.page_click_index()
        # sleep(1)
        self.page_click_channel(channel)
        sleep(1)
        self.page_click_article(title)

    # 组合搜索方法
    def page_app_search(self, text):
        log.info("正在调用app查询业务方法，查询关键字：{}".format(text))
        self.page_click_search_column()
        sleep(1)
        self.page_input_search_column(text)
        self.page_click_search_btn()
        sleep(2)
        print(self.page_get_search_results())





