import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

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
        # 获取PageAppCircle
        self.circle = self.page_in.page_get_app_circle()

    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_app_driver()

    # 测试圈子发布文章
    @pytest.mark.parametrize("circle,title,text", read_yaml("app_circle.yaml"))
    def test01_app_circle_article(self, circle, title, text):
        try:
            # self.circle.page_publish_article_image(circle, title, text)
            self.circle.page_publish_article_vote(circle, title, text, vote_title="1+1=?", options=[2, 3, "钝角", "C"])
            self.circle.page_search_article(circle, title)
            self.circle.page_delete_article()
            # self.circle.page_cancel_join()
        except Exception as e:
            log.error(e)
            self.circle.base_screenshot()
            raise
