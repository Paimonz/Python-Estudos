print ('\n')
print ('=°'*23)
print ('Gerando uma PA')
print ('=°'*23)

primeiro = int(input ('\nDigite o primeiro termo: '))
razão = int(input ('Digite a razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print ('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print ('Pausa')
    mais = int(input ('Quantos termos você quer mostrar a mais: ?'))
print ('\nProgressão finalizada com {} termos'.format(total))