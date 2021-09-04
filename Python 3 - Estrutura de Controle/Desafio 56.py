print('\n')
mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0

for p in range (1,5):
    print('*'*15,'{}° Pessoa'.format(p), '*'*15)
    nome = str(input ('Digite o nome:'))
    idade = int(input ('Digite a idade:'))
    sexo = str(input('sexo [M/F]:'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade/4
print ('A média de idade do grupo é de:{}.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))