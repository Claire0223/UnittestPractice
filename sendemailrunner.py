#-*- coding=utf -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os

##邮件定时整合发送

###发邮件##
def sendEmail(emailfile):   
    userhost='smtp.163.com'
    user='@163.com'
    passwd= ''
    receives=['@qq.com']
    sender='@163.com'

    f=open(emailfile,'rb')#报告的位置，及操作方式为wb
    mail_body=f.read()
    f.close()

    subject='报告整合发送'
    message=MIMEText(mail_body,'html','utf-8')
    message['Subject']=Header(subject,'utf-8')
    # message['Context-Type']='application/octet-stream'
    # message['Content-Dispositon']='attachment;filename="最新的报告.html"'

    # msg=MIMEMultipart('related')
    # msg['From']=sender
    # msg['To']=';'.join(receives)
    # msg['Subject']=subject

    smtp=smtplib.SMTP()
    smtp.connect(userhost)
    smtp.login(user,passwd)
    smtp.sendmail(sender,receives,message.as_string())
    smtp.quit()
    print("邮件已经发送！")


###查找最新的报告###
def reportFind(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda  fn: os.path.getmtime(testreport + '\\'+fn))
    file_new=os.path.join(testreport,lists[-1])
    return file_new

if __name__=='__main__':
    testdir='D:\\python\\unittest' #测试用例路径
    testreport='D:\\python\\unittest\\' #测试报告路径

    discover=unittest.defaultTestLoader.discover(testdir,pattern='test_*.py')
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename=testreport+'\\'+now+'百度测试用例执行清空.html'
    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    runner.run(discover)
    fp.close()

    #调用函数
    newreport=reportFind(testreport)
    sendEmail(newreport)
    