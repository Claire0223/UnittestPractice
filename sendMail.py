#-*- coding =utf-8 -*-
#使用python格式进行邮件发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方SMTP服务,设置自己的帐号密码
mail_host='smtp.163.com' #设置服务器，选择邮箱类型
mail_user='@163.com' #设置用户
mail_pw=''#授权码
port=465

#设置接收方的邮箱
sender='@163.com'
receivers=['@qq.com']
subject='海子的诗'

meg_text='''从明天起，做一个幸福的人

喂马，劈柴，周游世界

从明天起，关心粮食和蔬菜

我有一所房子，面朝大海，春暖花开

从明天起，和每一个亲人通信

告诉他们我的幸福

那幸福的闪电告诉我的

我将告诉每一个人

给每一条河每一座山取一个温暖的名字

陌生人，我也为你祝福

愿你有一个灿烂的前程

愿你有情人终成眷属

愿你在尘世获得幸福

我只愿面朝大海，春暖花开

'''

message=MIMEText(meg_text,'plain','utf-8')
message['From']=sender
message['To']=";".join(receivers)

message['Subject']=Header(subject,'utf-8')

#发送邮件

smtpObj=smtplib.SMTP_SSL(mail_host)
smtpObj.connect(mail_host,port)#此处是非ssl端口25，如果是ssl端口465、587，需要改为SMTP_SSL
smtpObj.login(mail_user,mail_pw)
smtpObj.sendmail(sender,receivers,message.as_string())
smtpObj.quit()
