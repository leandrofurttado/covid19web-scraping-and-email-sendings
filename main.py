from sending_emails import *
from time import sleep
from web_scraping_covid_vacination import *

mensagem_final = f'''Olá, Leandro! Tudo bem? Aqui vai as últimas informações que
consegui referente as informações da vacinação contra a covid-19! \n\n
Total de pessoas vacinadas: {populacao_dados()[0]}\n\n
Porcentagem total de pessoas vacinadas: {populacao_dados()[1]}'''

while True:
    try:
        envia_email(mensagem_final)
        print('E-MAIL ENVIADO COM SUCESSO!')
        sleep(72000)
    except Exception as error:
        print('HOUVE ALGUM PROBLEMA! PODE SER O E-MAIL.')
        print(f'ESSE É O ERRO: {error}')
    sleep(10)
