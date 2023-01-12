from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

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
        self.app_login.logout()
        GetDriver.quit_app_driver()

    # 测试登录
    def test01_app_login(self):
        sleep(3)
        self.app_login.login(page.wy_email, page.wy_pwd)
        try:
            assert "我的" == self.app_login.get_profile_menu_state()
        except Exception as e:
            log.error(e)
            self.app_login.base_screenshot()
            raise




