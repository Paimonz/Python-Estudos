print ('\n')
print ('=°'*23)
print ('Gerando uma PA')
print ('=°'*23)

primeiro = int(input ('\nDigite o primeiro termo: '))
razão = int(input ('Digite a razão: '))

termo = primeiro
cont = 1

while cont <= 10:
    print ('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print ('Fim')