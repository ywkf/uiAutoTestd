from selenium.webdriver.common.by import By

# 包名
appPackage = "com.netease.newsreader.activity"
# 启动名
appActivity = "com.netease.nr.phone.main.MainActivity"
# 同意并继续
app_agree = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[2]"
# 允许权限
app_agree_authority = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]"

"""底部菜单"""
# 首页
app_down_index = By.XPATH, "//*[@index='0' and @bounds='[0,1211][180,1280]']"
# 视频
app_down_video = By.XPATH, "//*[@index='1' and @bounds='[180,1211][360,1280]']"
# 圈子
app_down_circle = By.XPATH, "//*[@index='2' and @bounds='[360,1211][540,1280]']"
# 个人信息
app_down_profile = By.XPATH, "//*[@index='3' and @bounds='[540,1211][720,1280]']"

"""个人信息"""
# 个人信息文本
app_profile_state_text = By.XPATH, "//*[@index='1' and @bounds='[615,1257][645,1278]']"
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
wy_email = "xxx"
# 密码
wy_pwd = "xxx"
# 个人信息登录状态
app_profile_state = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/j6' and contains(@text, '我的')]"
# 设置按钮
app_options = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/bv2' and contains(@text, '设置')]/.."
# 登出按钮
app_logout_btn = By.ID, "btx"
# 确认退出按钮
app_logout_confirm = By.ID, "au3"

"""首页"""
# 频道区域
app_channel_area = By.ID, "b6i"
# 页面区域
app_page_area = By.ID, "hh"


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
# 搜索结果
app_search_results = By.ID, "bey"

"""圈子"""
# 发布文章按钮
app_publish_article_btn = By.XPATH, "//*[@index='2' and @bounds='[631,1120][696,1185]']"
# 选择圈子头区域
app_circle_head = By.ID, "bpb"
# 选择圈子区域
app_circle_area = By.ID, "aq0"


# 选择圈子
def get_circle_loc(click_text):
    app_circle_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/aq1' and contains(@text, '{}')]".format(
        click_text)
    return app_circle_loc


# 加入圈子并发布按钮
app_join_publish_btn = By.ID, "a3x"
# 添加标题
app_add_title = By.ID, "bpo"
# 标题
app_circle_title = By.ID, "bpk"
# 文章内容
app_circle_article = By.ID, "b2p"
# 添加图片按钮
app_add_image_btn = By.ID, "ay1"
# 允许权限按钮
app_permission_btn = By.XPATH, "//*[@resource-id='com.android.packageinstaller:id/permission_allow_button']"
# 添加投票按钮
app_add_vote_btn = By.ID, "ayl"
# 分组按钮
app_grouping_btn = By.ID, "aq2"
# 选择图片(最新)
app_select_image = By.XPATH, "//*[@bounds='[318,113][351,146]']"
# 继续按钮
app_continue_btn = By.ID, "ka"
# 选择分组区域
app_select_group_area = By.ID, "aum"


# 选择分组
def get_group_loc(click_text):
    app_group_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/aun' and contains(@text, '{}')]".format(
        click_text)
    return app_group_loc


# 投票标题
app_vote_title = By.ID, "b2w"


# 投票选项
def get_options_loc(options_num):
    app_options_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/ayp' and contains(@text, '选项 {}')]".format(
        options_num)
    return app_options_loc


# 添加选项按钮
app_vote_add_options = By.ID, "ay9"
# 完成按钮
app_vote_done_btn = By.XPATH, "//*[@bounds='[645,36][707,108]' and contains(@text, '完成')]"
# 发布按钮
app_circle_publish_btn = By.XPATH, "//*[@bounds='[645,36][707,108]' and contains(@text, '发布')]"
# 我的圈子区域
app_my_circle_area = By.XPATH, "//*[@index='1' and @resource-id='com.netease.newsreader.activity:id/b7o']"


# 选择我的圈子
def get_my_circle_loc(click_text):
    app_my_circle_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/bm9' and contains(@text, '{}')]/..".format(
        click_text)
    return app_my_circle_loc


# 圈子文章区域
app_circle_article_area = By.ID, "a9t"


# 选择圈子文章
def get_circle_article_loc(click_text):
    app_circle_article_loc = By.XPATH, "//*[@resource-id='com.netease.newsreader.activity:id/jb' and contains(@text, '{}')]".format(
        click_text)
    return app_circle_article_loc


# 圈子文章打开选项按钮
app_article_up_options_btn = By.XPATH, "//*[@bounds='[662,36][707,108]']"
# 选项删除按钮
app_article_delete_btn = By.ID, "a9e"
# 确认删除按钮
app_delete_confirm_btn = By.ID, "au3"
# 取消加入按钮
app_cancel_join_btn = By.XPATH, "//*[@bounds='[28,1062][108,1142]']"










