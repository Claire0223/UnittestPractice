#-*- coding=utf-8 -*-
from selenium import webdriver
import unittest,time,re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class BaiduTest(unittest.TestCase):

    def setUp(self):
        self.dirver=webdriver.Chrome()
        self.dirver.implicitly_wait(30)
        self.baseUrl = 'http://www.baidu.com'
        self.verificationErrors = []#脚本运行时，错误的信息将被打印到这个列表中

    def test_baidu(self):
        driver = self.dirver
        driver.get(self.baseUrl+'/')
        driver.find_element_by_id('kw').send_keys('易烊千玺')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        driver.get_screenshot_as_file('e:\\测试材料\\unittest1.jpg')

    def is_element_present(self,how,what):#查找页面元素是否存在,可直接放在case上
        try:
            self.dirver.find_element(by=how,value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self): #对弹窗的异常处理
        try:
            self.dirver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True
    
    def close_alert_present(self):
        try:
            alert = self.dirver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally:
            self.accept_next_alert=True

    def tearDown(self):
        self.dirver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()