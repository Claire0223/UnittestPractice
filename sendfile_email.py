#-*-coding=utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

#发送设置
user_host='smtp.163.com'
user='leimf1128@163.com'#信件
passwd='BUHWNKEYRZXUWTZI'
sender='leimf1128@163.com'#信封
receivers=['1327686271@qq.com']
subject='邮件添加附件发送'

'''常见的multipart类型有三种：multipart/alternative, multipart/related和multipart/mixed。
邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。
邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。'''

#创建实例
message=MIMEMultipart()
message['From']=sender
message['To']=";".join(receivers)
#message['Subject']=subject
message['Subject']=Header(subject,'utf-8')
msg_txt="""
钵仔糕的经典做法
传统的砵仔糕以黄糖、粘米粉等造成后，放在一个瓦制的小砵内蒸熟；但现在的制法已多数改用小瓷碗。吃的时候才把砵仔糕从小砵倒出来，以竹签穿起来吃。
有的砵仔糕加入红豆；亦有砵仔糕以白砂糖制造，因而是白色的。刚蒸好的砵仔糕，口感暖、滑、香、绵。
在广州西关也有售卖，一般以一碗或半碗为单位，每个晶莹剔透，咬下去的口感很弹牙，不同口味的馅，如红豆。
"""
message.attach(MIMEText(msg_txt,'plain','utf-8'))


#附件1 文本
att1=MIMEText(open('E:\\测试材料\\emailsend.txt','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'#内容类型为未知的应用程序文件
att1['Content-Disposition']='attachment;filename=emailsend.txt'#附件打开的格式
message.attach(att1)



#附件2 图片
fp=open('D:\\表情包\\测试用\\123.jpg','rb')
att2=MIMEImage(fp.read())
fp.close()
att2.add_header('Content-ID','<imagel>')
#att2['Content-Disposition']='attachment;filename="小黄鸭.jpg"'
message.attach(att2)

#构造html
#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
html = """
<html>  
  <head></head>  
  <body>  
    <p>Hi!<br>  
       How are you?<br>  
       Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
    </p> 
  </body>  
</html>  
"""    
text_html = MIMEText(html,'html', 'utf-8')
text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'   
message.attach(text_html)

#创建连接及发送
smtp=smtplib.SMTP_SSL(user_host,465) #使用ssl端口
#smtp.connect(user_host)
smtp.login(user,passwd)
smtp.sendmail(sender,receivers,message.as_string())
smtp.quit()