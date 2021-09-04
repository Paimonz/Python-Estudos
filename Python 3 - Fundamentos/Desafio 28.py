'''Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5
e praça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se i 
usuário venceu ou perdeu.'''

from time import sleep
from random import randint
print ('-=-'*15)
print ('\nVou pensar em um número ente 0 e 5.')
print ('-=-'*15)
c = randint(0,5)
print('Pensando...')
sleep (3)
p = int(input('Já pensei, tente adivinhar:\n'))
if (p == c):
    print (f'Parabéns! eu pensei no número: {c}')
else:
    print (f'Eu venci! pois pensei no número {c} e não no número {p}')
    
    