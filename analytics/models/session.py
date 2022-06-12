import os
import email
import smtplib

EMAIL_FROM = os.getenv('EMAIL_FROM', 'yeongher@163.com')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.live.com')
SMTP_PORT = os.getenv('SMTP_PORT', '587')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'Wyh19840709')


def send_verification_code(email_to: str):
    smtp_client = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.ehlo()
    smtp_client.login(EMAIL_FROM, SMTP_PASSWORD)
    smtp_client.sendmail(EMAIL_FROM, email_to, create_email_message(email_to))
    smtp_client.quit()


def create_email_message(email_to: str) -> str:
    message = email.message_from_string('warning')
    message['From'] = EMAIL_FROM
    message['To'] = email_to
    message['Subject'] = "Agile Analytics 登录验证码"
    message['Body'] = "感谢您使用Agile Analytics, 您的验证码为：123456"

    return message


send_verification_code("wangyonghe@msn.com")