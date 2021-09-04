'''import requests

r = requests.get('https://www.investopedia.com/terms/f/forex.asp')
print(r.text)
print(r.encoding)
print(r.headers)
print(r.status_code)'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

import requests
r = requests.get('https://www.investopedia.com/terms/f/forex.asp')
dados = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(dados, 'html.parser')
'''print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)'''
#print(soup.get_text(), end='')

arquivo = open('Teste.txt','w+')
arquivo.write(soup.get_text())

import webbrowser
webbrowser.open('www.google.com', new=0, autoraise=True)