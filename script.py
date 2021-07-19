import random, re, smtplib, os
from email.mime.text import MIMEText
from email.header import Header


smtp_host = "smtp.gmail.com"
#depends on your email provider gmail or outlook
port = 587
        
login = "your_email_address"
password = "your_app_based_password"

recipient_mail = "recipient_address"
cc = "optional"
        
recipient = [recipient_mail]    
        
msg = MIMEText('Hi', 'Hi', 'utf-8')
msg['Subject'] = Header("Login access", 'utf-8')
msg['From'] = login
msg['To'] = recipient_mail
msg['cc'] = "balasankarkn@gmail.com"

s = smtplib.SMTP(smtp_host, port)
try:
        s.starttls()
        s.login(login,password)
        s.sendmail(msg['From'], recipient, msg.as_string())
finally:        
        s.quit()
