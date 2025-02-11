import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject,body,to_email):
    from_email=os.getenv("FROM_EMAIL")
    password=os.getenv("EMAIL_PASSWORD")

    msg=MIMEMultipart()
    msg['From']=from_email
    msg['To']=to_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
            server.login(from_email,password)
            text=msg.as_string()
            server.sendmail(from_email,to_email,text)
            print(f"邮件已成功发送到 {to_email}")
    except Exception as e:
        print(f"邮件发送失败: {e}")

if __name__ == "__main__":
    # 只在直接运行此文件时执行发送操作
    send_email("自动邮件测试","这是一封自动发送的测试邮件","1745404409@qq.com")
