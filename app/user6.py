#проверка по почте

import smtplib
from email.mime.text import MIMEText
import logging 
from  sendmail_project.ipa_api import bootstrap_ipa_api


IPA_API = bootstrap_ipa_api()
logging.warning(IPA_API._API__done)

def generate_password():
    return "new_password"
    
def send_email(recipient, password):
    sender = 'ya.alexgr4@yandex.ru'
    message = f"Временный пароль: {password}" 
    msg = MIMEText(message)
    
    msg['Subject'] = 'Временный пароль для FreeIPA' #название сообщения
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as server:
        server.login(sender, 'xsegyibpinputkgo')
        server.sendmail(sender, recipient, msg.as_string())
        
def reset_password():
    email = "ya.alexgr4@yandex.ru"
    user_username = "alex"
    #user_username, user_email = valid_user(email)
    new_password = generate_password()
    send_email(email, new_password)
    IPA_API.Command.user_mod(user_username, userpassword=new_password)
    try:
        return True, "Пароль успешно изменен и отправлен на электронную почту."
    except Exception as e:
        return False, str(e)