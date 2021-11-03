'''

CONTA:
pythonprogrammingleandro02@outlook.com
123456789Saco

'''
import smtplib
from email.message import EmailMessage

# Configurando o email e senha:
EMAIL = 'opala.gyb02@gmail.com'
PASSWORD = 'Leanlv900'

'''# Criando o email que será enviado:
email_message = EmailMessage()
email_message['Subject'] = 'TESTE DE SUBJECT'
email_message['From'] = 'opala.gyb02@gmail.com'
email_message['To'] = 'leandrofx2001@hotmail.com'
email_message.set_content('ESSE É O TESTE E APARENTEMENTE DEU TUDO CERTO!')'''

# ENVIANDO O EMAIL:


def envia_email(msg):
    email_message = EmailMessage()
    email_message['Subject'] = 'ATUALIZAÇÃO COVID-19 SCRIPT'
    email_message['From'] = 'opala.gyb02@gmail.com'
    email_message['To'] = 'leandrofx2001@hotmail.com'
    email_message.set_content(msg)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(email_message)
