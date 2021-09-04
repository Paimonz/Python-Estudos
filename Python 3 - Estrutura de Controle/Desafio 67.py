print('\nGerador de tabuadas!')
print('Para sair do programa digite um número negativo')
print('\n')

while True:
    tabuada = int(input('Digite um número para ver a sua tabuada: '))
    if tabuada < 0:
        break
    print('-' * 20)
    for n in range(1,11):
        print(f'{tabuada} x {n} = {n*tabuada}')
    print('-' * 20)
print('\nPrograma finalizado, volte sempre!')

