from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestAppCircle:

    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取入口类
        self.page_in = PageIn(driver)
        # 调用登录方法
        self.page_in.page_get_app_login().page_app_login_success()
        # 获取PageAppCricle
        self.circle = self.page_in.page_get_app_circle()

    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_app_driver()

    # 测试圈子发布文章
    def test01_app_circle_article(self):
        try:
            pass
        except Exception as e:
            log.error(e)
            self.circle.base_screenshot()
            raise







