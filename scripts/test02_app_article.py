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
        # 调用登录方法
        # self.page_in.page_get_app_login().page_app_login_success()
        # 获取PageAppArticle
        self.app_article = self.page_in.page_get_app_article()

    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_app_driver()

    # 测试查找频道文章
    def test01_app_find_channel(self):
        try:
            self.app_article.page_app_search_article("科技", "中国")
            # self.app_article.page_app_search("中国")
        except Exception as e:
            log.error(e)
            self.app_article.base_screenshot()
            raise
