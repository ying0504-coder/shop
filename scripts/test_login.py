import os,sys

import allure
import pytest

sys.path.append(os.getcwd())
from base.base_init import Base_Init
from page.page_login import PageLogin
from base.base_yaml import yml_data_with_filename_and_key
def data_with_key(key):  #key为用例名称，如test_login
    return yml_data_with_filename_and_key("data_login", key)

class Test_Login():
    def setup(self):
        self.driver = Base_Init()  #实例化一个驱动
        self.login_driver = PageLogin(self.driver) #将初始化的驱动传给page页面，也传给test页面
    #[("15602160302","123456"),("1234567899","123")]
    @pytest.mark.parametrize(("args"), data_with_key("test_login"))
    @allure.step(title="登录测试")
    def test_login(self,args):
        #1.输入用户名
        allure.attach('输入用户名', args["username"])
        self.login_driver.input_username(args["username"])
        #2.输入密码
        allure.attach('输入密码', args["password"])
        self.login_driver.input_password(args["password"])
        #3.点击确定
        allure.attach('点击登录按钮', '')
        self.login_driver.click_login()
        #4.判断是否登录成功
        result = self.login_driver.is_login("lq_1206085724_ybv")
        print(result)
        allure.attach('判断结果', str(result))
        #5.截图并上传至allure
        self.login_driver.screenshot(args["username"])
        allure.attach("图片", open('./screen/' + args["username"] + '.png', 'rb').read(),allure.attach_type.PNG)
