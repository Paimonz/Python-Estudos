print('\n')
print('='*20)
print('CADASTRO DE PESSOAS')
print('='*20)

maior = homens = mulheres = 0

while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    if idade > 18:
        maior += 1
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('\nPrograma finaliza!')
print(f'{maior} pessoas com mais de 18 anos foram cadastradas!')
print(f'{homens} homens foram cadastrados!')
print(f'{mulheres} mulhur(es) com menos de 20 anos foram cadastradas!')