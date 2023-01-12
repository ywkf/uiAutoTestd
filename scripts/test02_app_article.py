from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestAppArticle:

    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取入口类
        self.page_in = PageIn(driver)
        # 获取PageAppArticle
        self.app_article = self.page_in.page_get_app_article()

    # 关闭driver
    def teardown_class(self):
        # self.app_article.logout()
        GetDriver.quit_app_driver()

    # 测试查找频道
    def test01_find_channel(self):
        try:
            sleep(3)
            # self.app_article.search("中国")
            self.app_article.click_channel("科技")
            self.app_article.click_article("中国")
            # self.app_article.login(page.wy_email, page.wy_pwd)
            # assert "我的" == self.app_article.profile_menu_get_state()
        except Exception as e:
            log.error(e)
            self.app_article.base_screenshot()
            raise
