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
app_down_profile = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.TabWidget/android.widget.LinearLayout[4]"
# 个人信息文本
app_profile_state = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.TabWidget/android.widget.LinearLayout[4]/android.widget.TextView"
# 登录按钮
app_login_btn = By.ID, "as0"
# 邮箱登录按钮
app_login_email = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.widget.TextView"
# 频道
app_channel_btn = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[7]"
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
app_options = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout"
# 登出按钮
app_logout_btn = By.ID, "btx"
# 确认退出按钮
app_logout_confirm = By.ID, "au3"




