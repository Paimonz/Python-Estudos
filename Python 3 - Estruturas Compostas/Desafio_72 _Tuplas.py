'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrálo-lo por extenso.'''

numeros = ('zero', 'um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezssete','dezoito','dezenove','vinte')  #criado tupla de nome "numero" com elementos de 0 a 20 escrito por extenso.

while True: #loop infinito
    busca = int(input('\nDigite um número entre 0 à 20:'))

    while busca > 20 or busca <0:   #condição lógica para o usuário digitar um indice válido para a tupla 
        print('Valor inválido! Tente Novamente!')
        busca=int(input('Digite um valor entre 0 à 20: '))   
    print(f'O número que você digitou foi: {numeros[busca]}')

    continuar = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':    #quebra o loop infinito se o usuário digitar 'N'
        break

print('\nPrograma finalizado!')


