from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

#=============== Email remetente ==============#
email_sender = 'dev.marciorodrigo@gmail.com'
#========= Senha do email remetente ===========#
email_password = password 
#============ Email destinatário ==============#
email_receiver = 'user@email.com'

#=======Assunto e corpo da mensagem============#
subject = "Não responda este email"
body = """
Que a força esteja com você.
May the Force be with you.
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

#==================Configurações SMTP do Gmail=======================#
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())