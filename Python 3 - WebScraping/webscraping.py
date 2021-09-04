
import re
import requests
from bs4 import BeautifulSoup

def SalvaTexto():

    r = requests.get('https://www.investopedia.com/terms/f/forex.asp')
    dados = r.text
    soup = BeautifulSoup(dados, 'html.parser')
    artigo = soup.article
    texto = artigo.find_all(id=re.compile("^mntl-sc-block_1-0-"))

    precisaPular = True
    list = []
    for e in texto:
        if not precisaPular:
            if any([i in e['class'] for i in ['mntl-sc-block-callout', 'mntl-sc-block-inlinevideo']]):
                continue
            list.append(e.get_text())
        elif 'finance-sc-block-callout' in e['class']:
            precisaPular = False

    teste = ' '.join(list)
    print(teste)

    arquivo = open('Teste1.txt', 'w+')
    arquivo.write(teste)
    arquivo.close()
SalvaTexto()

def leituraDoTexto():
    arquivo = open('Teste1.txt', 'r')
    if(arquivo.mode == 'r'):
        conteudo = arquivo.read()
        print(conteudo)
    arquivo.close()
leituraDoTexto()



''' 
1°Achar a tag article Pegar
2° achar a div com a classe article body 
3° Verificar se  é espaço
'''



