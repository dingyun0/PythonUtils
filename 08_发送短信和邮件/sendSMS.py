from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_sms(to_number, message):
    # 从环境变量获取认证信息
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_number = os.getenv('TWILIO_PHONE_NUMBER')

    try:
        # 创建 Twilio 客户端
        client = Client(account_sid, auth_token)

        # 发送消息
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"短信已发送，消息ID: {message.sid}")
        
    except Exception as e:
        print(f"发送短信失败: {str(e)}")

if __name__ == "__main__":
    # 测试发送短信
    to_number = "+86你的手机号"  # 替换为接收者的手机号
    message = "这是一条测试短信"
    send_sms(to_number, message)
