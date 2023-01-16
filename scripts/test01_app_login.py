from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppLogin:

    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取PageLogin
        self.app_login = PageIn(driver).page_get_app_login()

    # 关闭driver
    def teardown_class(self):
        self.app_login.page_app_logout()
        GetDriver.quit_app_driver()

    # 测试登录
    @pytest.mark.parametrize("email,pwd", read_yaml("app_login.yaml"))
    def test01_app_login(self, email, pwd):
        sleep(3)
        self.app_login.page_app_login(email, pwd)
        try:
            assert self.app_login.page_is_login_success()
        except Exception as e:
            log.error(e)
            self.app_login.base_screenshot()
            raise




