# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request
from bs4 import BeautifulSoup

def ConectaInternet():
    objUrl = urllib.request.urlopen("https://www.investopedia.com/terms/f/forex.asp")


    if objUrl.getcode() == 200:
        dados = objUrl.read()
        soup = BeautifulSoup(dados, 'html.parser')
        print(soup.get_text())

ConectaInternet()


