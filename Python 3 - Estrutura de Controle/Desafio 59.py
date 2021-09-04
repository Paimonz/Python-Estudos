from time import sleep
print ('\n')
print ('π'*45)
print ('Vou Analizar dois números!')
print ('π'*45)


n1 = int(input('\nDigite o 1° número:'))
n2 = int(input('Digite o 2° número:'))

opção = ''
while opção != 5:

    
    opção = int(input ('''\nO que você deseja fazer?:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa: '''))

    if opção == 1:
        resposta = n1 + n2
        print ('A soma de {} + {} = {}'.format(n1, n2, resposta))
    elif opção == 2:
        resposta = n1 * n2
        print(' A multiplicação de {} x {} = {}'.format(n1, n2, resposta))
    elif opção == 3:
        if n1 > n2:
            print ('O número {} é maior que {}'.format(n1,n2))
        else:
            print ('O número {} é maior que {}'.format(n2, n1))
    elif opção == 4:
        print ('Digite os valores novamente!')
        n1 = int(input('\nDigite o 1° número:'))
        n2 = int(input('Digite o 2° número:'))
       
    elif opção == 5:
        print ('Saindo do programa...')
        sleep(2)
        print ('Programa finalizado!')
    else:
        print ('Opção inválida, tente novamente:')
    
