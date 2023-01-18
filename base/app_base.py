from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):

    # 点击元素
    def app_base_find_ele_by_accessibility_id(self, accessibility_id):
        self.driver.find_element_by_accessibility_id(accessibility_id).click()

    # 左划屏幕
    def app_base_wipe_to_left(self):
        """
        720*1280
        """
        self.driver.swipe(690, 574, 0, 574, duration=2000)

    # 上划屏幕
    def app_base_wipe_to_up(self):
        """
        720*1280
        """
        self.driver.swipe(360, 1024, 360, 512, duration=1000)

    # 1. 查找是否存在元素
    def app_base_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=3)
            log.info("找到该元素：{}".format(loc))
            print("找到该元素：{}".format(loc))
            return True
        except:
            log.info("未找到该元素：{}".format(loc))
            print("未找到该元素：{}".format(loc))
            return False

    # 循环滑动查询点击
    def __wipe_search(self, loc, coord, duration=2000):
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2. 捕获异常
            try:
                sleep(2)
                # 1. 查找元素
                el = self.base_find_element(loc, timeout=3)
                # 2. 输出提示信息
                print("找到：{} 元素啦！".format(loc))
                sleep(2)
                # 3. 点击元素
                el.click()
                # 4. 跳出循环
                break
            # 3. 处理异常
            except:
                # 1. 输出提示信息
                print("未找到：{}元素！划一划".format(loc))
                # 2. 滑动屏幕
                self.driver.swipe(coord.get("start_x"), coord.get("start_y"), coord.get("end_x"), coord.get("end_y"),
                                  duration=duration)
            # 4. 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1. 输出提示信息
                print("滑到最后一屏幕，未到找元素！")
                # 2. 抛出未找到元素异常
                raise NoSuchElementException

    # 2. 从右向左滑动屏幕查询点击
    def app_base_right_wipe_left(self, loc_area, loc):
        log.info("正在调用从右向左滑动屏幕方法")
        # 1. 查找区域元素
        el = self.base_find_element(loc_area)
        # 2. 获取区域元素的位置 y坐标点
        y = el.location.get("y")
        # 3. 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4. 计算 start_x, start_y, end_x, end_y
        coord = {}
        coord["start_x"] = width * 0.8
        coord["start_y"] = y + height * 0.5
        coord["end_x"] = width * 0.2
        coord["end_y"] = y + height * 0.5

        # 获取频道元素配置信息
        # loc = page.get_channel_loc(click_text)
        # 5. 循环操作
        self.__wipe_search(loc, coord)

    # 3. 从下向上滑动屏幕查询点击
    def app_base_down_wipe_up(self, loc_area, loc):
        log.info("正在调用从下向上滑动屏幕方法")
        # 查找区域元素
        el = self.base_find_element(loc_area)
        # 获取区域x坐标
        x = el.location.get("x")
        # 获取区域宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算滑动区域
        coord = {}
        coord["start_x"] = width * 0.5
        coord["start_y"] = height * 0.8
        coord["end_x"] = width * 0.5
        coord["end_y"] = height * 0.1

        # 获取文章元素配置信息
        # loc = page.get_article_loc(click_text)
        self.__wipe_search(loc, coord)

    # 从下拉刷新屏幕查询点击
    def app_base_refresh_click(self, loc_area, loc):
        log.info("正在调用下拉刷新查询方法")
        # 查找区域元素
        el = self.base_find_element(loc_area)
        # 获取区域x坐标
        x = el.location.get("x")
        # 获取区域宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算滑动区域
        coord = {}
        coord["start_x"] = width * 0.5
        coord["start_y"] = height * 0.1
        coord["end_x"] = width * 0.5
        coord["end_y"] = height * 0.8

        self.__wipe_search(loc, coord, duration=5)

    # 下拉刷新
    def app_base_wipe_refresh(self):
        """
        720*1280
        """
        log.info("正在调用下拉刷新方法")
        self.driver.swipe(360, 640, 360, 1200)

    # 输入投票选项
    def app_base_input_options(self, options):
        j = 1
        for i in options:
            loc = page.get_options_loc(j)
            self.base_input(loc, i)
            j += 1
