'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
                                                                                Por Curso em Vídeo.'''

produtos = ('Lápis', 1.75,                      #aqui é criada uma tupla com os materiais escolar,
            'Caderno', 17.25,                   #seguida com seus respectivos preços.
            'Estojo', 8.89,
            'Mochila', 26.75,
            'Caneta', 3.25,
            'Borracha', 2.50)

print('\n')                                     #pula uma linha para deixar visualmente mais apresentável.
print('-=-'*20)                                 #exibe uma linha com os símbolos "-=-", fins estéticos.
print(f'{"LISTA DOS MATERIAIS ESCOLAR":^60}')   #cabeçario da lista, centralizado "^" em um tamanho de 60 espaços/caracteres.
print('-=-'*20)                                 #exibe uma linha com os símbolos "-=-", fins estéticos.

for iten in range(0, len(produtos)):            #para cada item dentro do comprimenta da tupla.
    if iten % 2 == 0:                           #se a posição do item for divisível por 2, 
        print(f'{produtos[iten]:.<50}', end='') #mostra o nome do item dentro da tupla produtos, orientado a esquerda em um espaçamento de 50 caracteres e completando-os com "."
    else:                                       #caso seja falso,
        print(f'R$:{produtos[iten]:>5.2F}')     #mostra os itens orientados a direita, formatados com duas casas decimais.

print('-=-'*20)                                 #exibe uma linha com os símbolos "-=-", fins estéticos.
print('\n')                                     #pula uma linha para deixar visualmente mais apresentável.
