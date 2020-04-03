#-*-coding=utf-8 -*-
import unittest
#加载测试文件
'''import testadd
import testsub
'''
#构造测试集
'''suite=unittest.TestSuite()
suite.addTest(testadd.Testadd("test_add1"))
suite.addTest(testadd.Testadd('test_add2'))

suite.addTest(testsub.Testsub('test_sub1'))
suite.addTest(testsub.Testsub('test_sub2'))
'''
#自动识别测试用例
#定义测试用例的目录为当前目录
test_dir='./'
discover= unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')



#执行测试
if __name__ == '__main__' :
    runner=unittest.TextTestRunner()
    runner.run(discover)
