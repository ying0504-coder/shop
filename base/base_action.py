from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base_Action():
    def __init__(self, driver):
        self.driver = driver

    # 根据特征，对应的去找元素,默认timeout=5.0, poll=1.0
    def find_element_test(self,location,timeout=5.0, poll=1.0):
        location_by = location[0]
        location_path = location[1]
        #增加5秒等待超时，每1秒刷新一次
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(location_by,location_path))
    def find_elements_test(self,location,timeout=5.0, poll=1.0):
        location_by = location[0]
        location_path = location[1]
        #增加5秒等待超时，每1秒刷新一次
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(location_by,location_path))

    #根据特征，对应的去找元素，并且点击
    def click_test(self,location):
        self.find_element_test(location).click()

    # 根据特征，对应的去找元素，并且输入文字
    def input_text_test(self,location,text):
        self.find_element_test(location).send_keys(text)

    # 预期要获取的toast的部分消息，默认0.1秒刷新一次
    def find_toast(self, message, timeout=3, poll=0.1):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element = self.find_element_test((By.XPATH, message), timeout, poll)
        return element.text

    # 断言获取的toast的部分消息
    def is_toast_exist(self, message, timeout=3, poll=0.1):
        try:
            self.find_toast(message, timeout, poll)
            return True
        except Exception:
            return False
    #截图
    def screenshot(self,file_name):
        PATH= "./screen/" + file_name + ".png"
        self.driver.get_screenshot_as_file(PATH)
