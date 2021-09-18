'''Desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
                                                    Por Curso em Vídeo.'''

números = tuple(int(input('Digite o número: '))for n in range(1,5))     #define "números" como tupla, e incremento os elementos do tipo inteiro 4 vezes dentro da tupla.

if 9 in números:                                                        #se o número 9 estiver na tupla números ele faz a contagem
    print(f'O número 9 apareceu {números.count(9)} vezes!')             #conta quantos números 9 apareceu na tupla
else:
    print('O número 9 não foi digitado!')                               #caso o núemro 9 não seja digitado

if 3 in números:
    print(f'A posição do primeiro número 3 é: {números.index(3)+1}°')   #verifica a posição do primeiros número 3, é acrescentado + 1 pois o python começa a sua contagem em 0
else:
    print('O número 3 não foi digitado!')

print('Os números pares digitados foram: ', end = '')
for n in números:                                                       #para cada elemento dentro da tupla "números"
    if n % 2 == 0:                                                      #verifica se o resto da divisão é zero
        print(n, end = ' ')                                             #mostra o número divisivel por 2, ou seja, par

