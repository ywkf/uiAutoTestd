from selenium.webdriver.common.by import By

# 包名
appPackage = "com.netease.newsreader.activity"
# 启动名
appActivity = "com.netease.nr.phone.main.MainActivity"
# 同意并继续
app_agree = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[2]"
# 允许权限
app_agree_authority = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]"
# 频道区域
app_channel_area = By.ID, "b6i"
# 底部个人信息
app_down_profile = By.XPATH, "//*[@index='3' and @bounds='[540,1211][720,1280]']"
# 个人信息文本
app_profile_state = By.XPATH, "//*[@index='1' and @bounds='[615,1257][645,1278]']"
# 登录按钮
app_login_btn = By.ID, "as0"
# 邮箱登录按钮
app_login_email = By.XPATH, "//*[@index='0' and @bounds='[478,1177][547,1246]']"
# 邮箱
app_email = By.ID, "ajy"
# 密码
app_pwd = By.ID, "aka"
# 同意条款
app_agree_protocol = By.ID, "bil"
# 开始使用按钮
app_login_start_btn = By.ID, "y1"
# 邮箱
wy_email = "18340812842@163.com"
# 密码
wy_pwd = "Mdhdhbbz"
# 设置按钮
app_options = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/bv2' and contains(@text, '设置')]/.."
# 登出按钮
app_logout_btn = By.ID, "btx"
# 确认退出按钮
app_logout_confirm = By.ID, "au3"


# 频道
def get_channel_loc(click_text):
    app_channel_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/bp_' and contains(@text, '{}')]".format(
        click_text)
    return app_channel_loc


# 文章
def get_article_loc(click_text):
    app_article_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/bey' and contains(@text, '{}')]".format(
        click_text)
    return app_article_loc


# 搜索栏
app_search_column = By.ID, "bb2"
# 搜索栏2
app_search_column2 = By.ID, "bb8"
# 搜索按钮
app_search_btn = By.ID, "bav"
