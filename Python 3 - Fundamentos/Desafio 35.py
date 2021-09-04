'''Desenvolva um programa que leia o 
comprimento de três retas e diga ao 
usuário se é possível ou não formar um 
triângulo'''

from time import sleep

print('\n')
print('\033[31m_-_'*15)
print('\033[37mAnalisando a Construção de um Triângulo')
print('\033[31m_-_\033[m'*15)

r1 = int(input ('\033[36m\nDigite a 1° reta: '))
r2 = int(input ('Digite a 2° reta: '))
r3 = int(input ('Digite a 3° reta: \033[m'))

print ('\033[1;41m\nMontando o seu triângulo...\033[m')
sleep(5)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('\033[1m\nÉ possível construir um triângulo com as retas! O tipo do seu triângulo é:\033[m')
    if r1 == r2 == r3:
        print ('\033[32mTriângulo Equilátero\033[m')
    elif r1 != r2 != r3 != r1:
        print ('\033[32mTriângulo Escaleno\033[m')
    else:
        print ('\033[32mTriângulo Isósceles\033[m')
else:
    print ('\033[1m\nNão é possível construir um triângulo com as retas! \033[m')