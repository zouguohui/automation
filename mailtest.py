#coding=utf-8

from email.header import Header
from email.mime.text import MIMEText
import smtplib

mail_host = "smtp.qq.com"
mail_user = "xxxxx@qq.com"
mail_pass = "*******"

sender = "xxxxxxxx@qq.com"
receivers = ["xxxxxxx@qq.com"]

content = '邮箱测试'
title = 'TEST'

def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ",".join(receivers)
    message['Subject'] = Header(title, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("发送成功！")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    sendEmail()