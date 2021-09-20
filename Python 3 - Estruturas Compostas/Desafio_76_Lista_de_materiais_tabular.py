'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('lápis', 1.75,
            'caderno', 17.25,
            'estojo', 8.89,
            'mochila', 26.75,
            'caneta', 3.25,
            'borracha', 2.50)

print('-=-'*20)
print(f'{"LISTA DOS MATERIAIS ESCOLAR":^60}')
print('-=-'*20)

for iten in range(0, len(produtos)):
    if iten % 2 == 0:
        print(f'{produtos[iten]:.<30}', end='')
    else:
        print(f'{produtos[iten]:.>30}')
