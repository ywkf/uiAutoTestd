from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    # 登录
    def page_get_app_login(self):
        return PageAppLogin(self.driver)

    # 查找文章
    def page_get_app_article(self):
        return PageAppArticle(self.driver)



