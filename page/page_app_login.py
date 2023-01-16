from time import sleep

import page
from base.app_base import AppBase


class PageAppLogin(AppBase):

    # 点击个人中心
    def page_click_profile(self):
        self.base_click(page.app_down_profile)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 点击邮箱登录
    def page_click_email_login(self):
        self.base_click(page.app_login_email)

    # 输入邮箱
    def page_input_email(self, email):
        self.base_input(page.app_email, email)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 点击同意条款
    def page_click_agree_protocol(self):
        self.base_click(page.app_agree_protocol)

    # 点击开始使用按钮
    def page_click_login_start_btn(self):
        self.base_click(page.app_login_start_btn)

    # 获取个人信息登录状态
    def page_get_profile_menu_state(self):
        return self.base_get_text(page.app_profile_state)

    # 点击设置按钮
    def page_click_options_btn(self):
        self.base_click(page.app_options)

    # 点击登出按钮
    def page_click_logout_btn(self):
        self.base_click(page.app_logout_btn)

    # 点击确认退出按钮
    def page_click_logout_confirm(self):
        self.base_click(page.app_logout_confirm)

    # 组合登录方法
    def page_app_login(self, email, pwd):
        sleep(3)
        self.page_click_profile()
        self.page_click_login_btn()
        self.page_click_email_login()
        self.page_input_email(email)
        self.base_click(page.app_email)
        sleep(1)
        self.page_input_pwd(pwd)
        self.page_click_agree_protocol()
        sleep(1)
        self.page_click_login_start_btn()
        sleep(2)

    # 组合登出方法
    def page_app_logout(self):
        self.page_click_options_btn()
        self.page_click_logout_btn()
        self.page_click_logout_confirm()

    # 登录成功方法
    def page_app_login_success(self):
        pass




