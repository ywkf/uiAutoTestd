from page.page_app_article import PageAppArticle


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    def page_get_app_article(self):
        return PageAppArticle(self.driver)


