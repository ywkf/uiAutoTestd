from time import sleep

import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppCircle(AppBase):

    # 点击圈子
    def page_click_circle_btn(self):
        self.base_click(page.app_down_circle)

    # 点击发布文章按钮
    def page_click_publish_article_btn(self):
        self.base_click(page.app_publish_article_btn)

    # 选择圈子点击
    def page_select_circle_click(self, circle):
        loc = page.get_circle_loc(circle)
        self.app_base_wipe_to_up()
        self.app_base_down_wipe_up(page.app_circle_area, loc)

    # 点击加入圈子并发布按钮
    def page_click_join_publish_btn(self):
        self.base_click(page.app_join_publish_btn)

    # 点击添加标题
    def page_click_add_title(self):
        self.base_click(page.app_add_title)

    # 输入标题
    def page_input_title(self, title):
        self.base_input(page.app_circle_title, title)

    # 输入内容
    def page_input_content(self, text):
        self.base_input(page.app_circle_article, text)

    # 点击添加图片按钮
    def page_click_add_image(self):
        self.base_click(page.app_add_image_btn)

    # 点击允许权限按钮
    def page_click_permission_btn(self):
        self.base_click(page.app_permission_btn)

    # 点击选择图片
    def page_select_image(self):
        self.base_click(page.app_select_image)

    # 点击添加图片继续按钮
    def page_click_continue_btn(self):
        self.base_click(page.app_continue_btn)

    # 点击分组按钮
    def page_click_group(self):
        self.base_click(page.app_grouping_btn)

    # 点击选择分组
    def page_select_group(self, group):
        loc = page.get_group_loc(group)
        self.app_base_down_wipe_up(page.app_select_group_area, loc)

    # 点击添加投票按钮
    def page_click_add_vote(self):
        self.base_click(page.app_add_vote_btn)

    # 输入投票标题
    def page_input_vote_title(self, vote_title):
        self.base_input(page.app_vote_title, vote_title)

    # 点击添加选项按钮
    def page_click_add_options(self):
        self.base_click(page.app_vote_add_options)

    # 输入投票选项
    def page_input_vote_options(self, options):
        self.app_base_input_options(options)

    # 点击编辑投票完成按钮
    def page_click_vote_done(self):
        self.base_click(page.app_vote_done_btn)

    # 点击发布按钮
    def page_click_publish_btn(self):
        self.base_click(page.app_circle_publish_btn)

    # 查找我的圈子
    def page_select_click_my_circle(self, circle):
        loc = page.get_my_circle_loc(circle)
        self.app_base_right_wipe_left(page.app_my_circle_area, loc)

    # 查找文章
    def page_click_article(self, title):
        loc = page.get_circle_article_loc(title)
        self.app_base_wipe_refresh()
        self.app_base_down_wipe_up(page.app_circle_article_area, loc)

    # 点击右上角选项按钮
    def page_click_up_options(self):
        self.base_click(page.app_article_up_options_btn)

    # 点击文章删除按钮
    def page_click_article_delete(self):
        self.base_click(page.app_article_delete_btn)

    # 点击文章删除确认按钮
    def page_click_delete_confirm(self):
        self.base_click(page.app_delete_confirm_btn)

    # 点击取消加入按钮
    def page_click_cancel_join(self):
        self.base_click(page.app_cancel_join_btn)

    # 组合添加图片方法
    def page_add_image(self):
        log.info("正在调用文章添加图片链接方法")
        self.page_click_add_image()
        self.page_click_permission_btn()
        self.page_select_image()
        self.page_click_continue_btn()

    # 组合添加投票方法
    def page_add_vote(self, vote_title, options):
        log.info("正在调用文章添加投票链接方法：[{}: {}]".format(vote_title, options))
        num = len(options)
        self.page_click_add_vote()
        self.page_input_vote_title(vote_title)
        for i in range(num-2):
            self.page_click_add_options()
        self.page_input_vote_options(options)
        self.page_click_vote_done()

    # 组合编辑文章方法
    def page_publish_article_edit(self, circle, title, text):
        log.info("正在调用编辑文章业务方法，圈子：{}，标题：{}，内容：{}")
        self.page_click_circle_btn()
        sleep(2)
        self.page_click_publish_article_btn()
        sleep(3.5)
        self.page_select_circle_click(circle)
        if self.base_ele_is_exist(page.app_join_publish_btn, timeout=1, poll=0.2):
            self.page_click_join_publish_btn()
        self.page_click_add_title()
        self.page_input_title(title)
        self.page_input_content(text)

    # 组合发布文章方法(图片)
    def page_publish_article_image(self, circle, title, text):
        log.info("正在调用发布文章业务方法(图片)，圈子：{}，标题：{}，内容：{}")
        self.page_publish_article_edit(circle, title, text)
        self.page_add_image()
        self.page_click_publish_btn()

    # 组合发布文章方法(投票)
    def page_publish_article_vote(self, circle, title, text, vote_title, options):
        log.info("正在调用发布文章业务方法(投票)，圈子：{}，标题：{}，内容：{}")
        self.page_publish_article_edit(circle, title, text)
        self.page_add_vote(vote_title, options)
        self.page_click_publish_btn()

    # 组合查询文章方法
    def page_search_article(self, circle, title):
        log.info("正在调用查询文章业务方法，圈子：{}，标题：{}")
        self.page_select_click_my_circle(circle)
        sleep(1)
        self.page_click_article(title)

    # 组合删除文章方法
    def page_delete_article(self):
        log.info("正在调用删除文章业务方法")
        self.page_click_up_options()
        self.page_click_article_delete()
        self.page_click_delete_confirm()

    # 组合取消加入方法
    def page_cancel_join(self):
        log.info("正在调用取消加入圈子业务方法")
        self.page_click_up_options()
        self.page_click_cancel_join()







