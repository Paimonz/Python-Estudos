'''Faça um programa que leia um ano 
qualquer e mostre se ele é bissexto'''

from datetime import date
ano = int(input ('\nDigite o ano que deseja analisar?\nColoque 0 para analisar o ano atual:\n'))

if ano == 0:
    ano = date.today().year
    
q = ano % 4
c = ano % 100
qt = ano % 400


if q == 0 and c != 0 or qt == 0:
    print ('\nO ano {} é BISSEXTO!'.format(ano))
else:
    print ('O ano {} não é BISSEXTO!'.format(ano))
    