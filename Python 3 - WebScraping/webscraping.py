'''Precisamos fazer um webscrap no site da investopedia pra alimentar nossa AI de conversação, precisamos pegar
tudo que estiver no texto desse artigo via python beautifulsoup e salvar em um txt, serão 2 mil webscrap,
então precisa ser feito de uma forma bem genérica, nós queremos apenas o core do texto do artigo, nada que vem
acima de key takeaway nem nada que vem abaixo de aritcle  source, tudo em plain text, nada de imagens, nem tabelas,
nem links nem vídeos.'''

import re
import requests
from bs4 import BeautifulSoup

def SalvaTexto():

    r = requests.get('https://www.investopedia.com/terms/f/forex.asp')                                  #requisição do HTML da página
    dados = r.text                                                                                      #pegando somente o corpo da página
    soup = BeautifulSoup(dados, 'html.parser')                                                          #usa o parser de HTML para ter uma árvore de XML
    artigo = soup.article                                                                               #pega todas as propriedades da tag article
    texto = artigo.find_all(id=re.compile("^mntl-sc-block_1-0-"))                                       #acha todos os elementos do HTML que tem um ID que começa com o valor: ^mntl-sc-block_1-0-, o "^" indica que o valores começam com essa estrutura

    precisaPular = True                                                                                 #estrutura para filtrar o article
    list = []                                                                                           #cria uma lista vazia
    for e in texto:                                                                                     #para cada elemento dentro da variável texto

        if not precisaPular:
            if any([i in e['class'] for i in ['mntl-sc-block-callout', 'mntl-sc-block-inlinevideo']]):  #se a clase do elemento for uma das duas, ele pula
                continue
            if e.name == 'p':                                                                           #pega todo texto dentro dos parágrafos
                list.append(e.get_text())                                                               #acrescenta na lista todo o filtro

        elif 'finance-sc-block-callout' in e['class']:                                                  #se achar algum item com essas caracteristicas ele para de pular
            precisaPular = False

    teste = ' '.join(list)                                                                              #junta todos os elementos da lista
    print(teste)                                                                                        #mostra o conteúdo

    arquivo = open('Teste1.txt', 'w+')                                                                  #abre um arquivo com o nome e extenção "Teste1.txt" no modo escrita
    arquivo.write(teste)                                                                                #escreve o conteúdo "teste" no arquivo
    arquivo.close()                                                                                     #fecha o arquivo
SalvaTexto()

def leituraDoTexto():
    arquivo = open('Teste1.txt', 'r')                                                                   #abre o arquivo no modo leitura
    if(arquivo.mode == 'r'):                                                                            #confirma se o arquivo está no modo leitura
        conteudo = arquivo.read()                                                                       #caso seja verdade, abre o arquivo no modo leitura
        print(conteudo)
    arquivo.close()
leituraDoTexto()



''' 
1°Achar a tag article Pegar
2° achar a div com a classe article body 
3° Verificar se  é espaço
'''



