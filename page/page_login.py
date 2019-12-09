import os,sys

import time

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import Base_Action


class PageLogin(Base_Action):
    # 定义各个元素
    my_button = By.ID, "com.yunmall.lc:id/tab_me"
    mylogin_button = By.XPATH, "//*[@text='已有账号，去登录' and @resource-id='com.yunmall.lc:id/textView1']"
    username = By.ID, "com.yunmall.lc:id/logon_account_textview"
    password = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    def __init__(self, driver):
        Base_Action.__init__(self, driver)
        # 点击我的
        # 点击登录/注册
        self.mypage()
    def mypage(self):  # 点击我的,进入登录页面
        self.click_test(self.my_button)
        self.click_test(self.mylogin_button)
    def input_username(self,username):#输入用户名
        self.input_text_test(self.username,username)
    def input_password(self,password):#输入密码
        self.input_text_test(self.password, password)
    def click_login(self):  # 点击登录按钮
        self.click_test(self.login_button)
    def is_login(self,assert_text): #断言查找元素
        #1.断言拼接XPATH内容，结果是"//*[@text='lq_1206085724_ybv']"
        assert_element = By.XPATH, "//*[@text='" + assert_text + "']"
        time.sleep(3)
        try:
            self.find_element_test(assert_element)
            return True
        except Exception:
            return False



