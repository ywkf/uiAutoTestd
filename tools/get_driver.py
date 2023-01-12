import appium.webdriver
from selenium import webdriver

import page


class GetDriver:

    # 1. 声名变量
    __web_driver = None

    __app_driver = None

    # 2. 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:

            # options = webdriver.ChromeOptions()
            # # 处理SSL证书错误问题
            # options.add_argument('--ignore-certificate-errors')
            # options.add_argument('--ignore-ssl-errors')
            # chrome_options = options

            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3. 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None

    # 获取app driver
    @classmethod
    def get_app_driver(cls):
        # 判断是否为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '7'
            # 必填
            desired_caps['deviceName'] = '127.0.0.1:62001'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # 使用unicode编码方式发送字符串
            desired_caps['unicodeKeyboard'] = True
            # 重置自动化时设置的键盘
            desired_caps['resetKeyboard'] = True
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回driver
        return cls.__app_driver

    # 退出app driver
    @classmethod
    def quit_app_driver(cls):
        # 判断driver不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None

"""
            "platformName": "Android",
            "platformVersion": "9",
            "automationName": "uiautotestd",
            "deviceName": "d2q",
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings",
            "noReset": true
"""

