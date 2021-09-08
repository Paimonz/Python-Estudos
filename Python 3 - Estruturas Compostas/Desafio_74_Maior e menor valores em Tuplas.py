'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, moste a listagem de
 númeross gerados e também indique o menor e o maior valor que estão na tupla.
                                                                                Por Curso em Vídeo.'''

from random import sample                           #https://docs.python.org/pt-br/3.7/library/random.html

computador = tuple(sample(range(10),5))             #Define computador como uma tupla, sample sortea um numero 
                                                    #de 0 à 10 por 5 vezes e guarda na tupla computador

print(f'Os valores sorteados foram: {computador}')  #exibe os elemntos sorteados na tupla.
print(f'O valor mais alto foi: {max(computador)}')  #mostra o maior elemento na tupla.
print(f'O menor valor foi: {min(computador)}')      #mostra o menor elemento na tupla.