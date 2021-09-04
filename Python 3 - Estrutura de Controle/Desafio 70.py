
total = cont = 0
barato = 9999
nome = ' '

while True:
    produto = str(input('Prduto: '))
    preço = float(input('Preço: '))
    total += preço
    if preço >= 1000:
        cont += 1
    if barato > preço:
        barato = preço
        nome = produto
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'O total da sua comprar foi de R$: {total}')
print(f'{cont} produto(s) custa(m) mais que R$:1000,00')
print(f'O produto mais barato foi {nome} e custa R$: {barato}')