# WEB SCRAPING DA VACINAÇÃO CONTRA A COVID-19 + ENVIO DE EMAILS COM OS DADOS.
Essa é mais uma ideia que surgiu durante os meus estudos de python, no qual tive a ideia que fazer uma raspagem de dados da fonte pública do Google sobre as vacinações e enviar por email. Neste código utilizei apenas pessoas vacinadas 100% sejam com as duas doses ou dose unica e a porcentagem atual do Brasil.

Ainda estou utilizando o script para me informar, fiz o deploy do mesmo na plataforma da Heroku e coloquei ele para rodar de 20 em 20 horas, sempre me atualizando sobre a porcentagem da vacinação, o tempo pode ser alterado no próprio sleep que contem no 'main.py'.

# Bibliotecas utilizadas:
* bs4 (BeautifulSoup)
* requests
* smtplib


