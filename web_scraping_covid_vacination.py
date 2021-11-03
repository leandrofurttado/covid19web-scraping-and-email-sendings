import requests
from bs4 import BeautifulSoup
'''
Nosso programa, irá pegar somente a quantidade de pessoas *TOTALMENTE* vacinadas
e sua respectiva porcentagem!
'''


def populacao_dados():
    url = "https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&state=7&gl=BR&ceid=BR%3Apt-419"

    busca = requests.get(url)
    soup = BeautifulSoup(busca.text, 'html.parser')

    populacao_vacinada_qtd = soup.findAll('div', {"class": "UvMayb"})
    # Nesta parte tive de usar o ''findAll'' pois apenas o find, encontrava apenas
    # 1 requests que seria o de TOTAL DE CASOS e não é o que queremos.

    porcentagem_vacinada_qtd = soup.findAll('div', {"class": "tIUMlb"})
    # Aqui pegamos exatamente a porcentagem de pessoas completamente vacinadas.

    resultado = [populacao_vacinada_qtd[3].text,
                 porcentagem_vacinada_qtd[3].strong.text]
    return resultado
