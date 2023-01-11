from time import sleep

import page
from base.app_base import AppBase


class PageAppArticle(AppBase):

    # 点击同意
    def click_agree(self):
        sleep(5)
        self.base_click(page.app_agree)

    # 点击个人中心
    def click_profile(self):
        self.base_click(page.app_down_profile)

    # 点击登录按钮
    def click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 点击邮箱登录
    def click_email_login(self):
        self.base_click(page.app_login_email)

    # 输入邮箱
    def input_email(self, email):
        self.base_input(page.app_email, email)

    # 输入密码
    def input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 点击同意条款
    def click_agree_protocol(self):
        self.base_click(page.app_agree_protocol)

    # 点击开始使用按钮
    def click_login_start_btn(self):
        self.base_click(page.app_login_start_btn)

    # 获取个人信息登录状态
    def profile_menu_get_state(self):
        return self.base_get_text(page.app_profile_state)

    # 点击设置按钮
    def click_options_btn(self):
        self.base_click(page.app_options)

    # 点击登出按钮
    def click_logout_btn(self):
        self.base_click(page.app_logout_btn)

    # 点击确认退出按钮
    def click_logout_confirm(self):
        self.base_click(page.app_logout_confirm)

    # 点击频道
    def click_channel_btn(self):
        self.base_click(page.app_channel_btn)

    # 组合登录方法
    def login(self, email, pwd):
        sleep(3)
        self.click_profile()
        self.click_login_btn()
        self.click_email_login()
        self.input_email(email)
        self.base_click(page.app_email)
        sleep(1)
        self.input_pwd(pwd)
        self.click_agree_protocol()
        sleep(1)
        self.click_login_start_btn()
        sleep(2)

    # 组合登出方法
    def logout(self):
        self.click_options_btn()
        self.click_logout_btn()
        self.click_logout_confirm()

    # 查找频道
    def click_channel(self, click_text):
        self.app_base_right_wipe_left(page.app_channel_area, click_text)



