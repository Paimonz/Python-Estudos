from random import randint

print('\n')
print('=-'*20)
print('Vamos jogar PAR ou ÍMPAR!')
print('=-'*20)

cont = 0


while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor!:'))
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Você quer [P/I]?:')).upper().strip()[0]
    resultado = (computador + jogador) % 2

    if escolha == 'P' and resultado == 0:
        print('VOCÊ venceu!')
        cont += 1
    elif escolha == 'I' and resultado == 1:
        print('VOCÊ venceu!')
        cont += 1
    else:
        print('=-' * 20)
        print('O COMPUTADOR VENCEU!')
        print('=-' * 20)
        break

print(f'\nVocê ganhou {cont} vez(es)!')
print(f'Na última partida você jogou {jogador} e o computador {computador}')






