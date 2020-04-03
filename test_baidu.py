#-*-coding=utf-8 -*-
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import unittest,time,os

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url='http://www.baidu.com/'

    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('新冠状肺炎')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        driver.get_screenshot_as_file('e://测试材料//新冠状肺炎新闻.jpg')


    def tearDown(self):
        self.driver.quit()


if __name__== '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu'))

    #按照一定格式获取当前时间
    now_t=time.strftime('%Y-%m-%d %H_%M_%S')

    ##定义报告存放路径,在路径上添加时间
    file_path='./' + now_t +'baiduresult.html'
    fp=open(file_path,'w')

    #定义测试报告
    runner=HTMLTestRunner (stream=fp, report_title='百度测试报告',descriptions='用例执行报告')
    runner.run(testunit)#运行测试用例
    fp.close()#关闭报告文件