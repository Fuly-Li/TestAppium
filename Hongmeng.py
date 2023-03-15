from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {
            "platformName": "Android",  # 手机系统
            "platformVersion": "9",  # 手机系统版本
            "deviceName": 'STF-AL10',  # 手机的名字，不会进行校验，但是没有会报错
            "automationName": "UiAutomator2",  # 自动化测试框架 （1.4以上的appium不用写）
            "appPackage": "com.ihear.audiobook",  # app包名
            "appActivity": ".page.welcome.ui.activity.LaunchActivity",  # app的启动页面
            # "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # # 判断页面是否出现升级弹窗
    # def upgrade(self):
    #     if len(self.driver.find_element(By.ID, 'com.ihear.audiobook:id/tv_update')) >= 1:
    #         self.driver.find_element(By.ID, "com.ihear.audiobook:id/tv_later").click()
    #         return True
    #     else:
    #         return False
    #

    # 测试点击游客登陆
    def test_login(self):
        # 判断页面是否有游客登陆选项
        try:
            # 有游客登录选项，判断用户为普通用户，就走游客登陆
            self.driver.find_element(By.XPATH,
                                     "//*[contains(@class,'android.widget.TextView') and contains(@text,'Visitors')]") \
                .click()

            # 判断页面是否出现更新提醒
            # visibility_of_element_located 判断元素是否可见
            try:
                self.driver.find_element(By.ID, "com.ihear.audiobook:id/tv_later").click()
            except:
                print("没有开启升级弹窗")
            # try:
            #     WebDriverWait(self.driver).until(self.screen_advertising)
            # except NoSuchElementException:
            #     print('没有大屏广告')

        except NoSuchElementException:
            # 没有游客登陆，则为已登录过的用户
            # 点击关闭启屏Banner
            try:
                self.driver.find_element(by=By.ID, value="com.ihear.audiobook:id/iv_welfare").click()
            except NoSuchElementException:
                print("没有启屏Banner，不进行点击操作")
