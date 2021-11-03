import smtplib
from email.message import EmailMessage

# Configurando o email e senha:
EMAIL = 'seu_email_aqui@email.com'
PASSWORD = 'sua_senha_aqui'

'''# Criando o email que será enviado:
email_message = EmailMessage()
email_message['Subject'] = 'TESTE DE SUBJECT'
email_message['From'] = 'email_remetente@email.com'
email_message['To'] = 'email_destinatário@email.com'
email_message.set_content('ESSE É O TESTE E APARENTEMENTE DEU TUDO CERTO!')'''

# ENVIANDO O EMAIL:


def envia_email(msg):
    email_message = EmailMessage()
    email_message['Subject'] = 'ATUALIZAÇÃO COVID-19 SCRIPT' #TÍTULO DO EMAIL
    email_message['From'] = 'email_remetente@email.com'
    email_message['To'] = 'email_destinatário@email.com'
    email_message.set_content(msg)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(email_message)
