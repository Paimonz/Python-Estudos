print ('\n')
resp = 's'
cont = 0
soma = 0
maior = 0
menor = 9999

while resp not in 'Nn':   
    valor = int(input ('Digite um número: '))
    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor
    soma += valor
    cont += 1
    media = soma / cont
    resp = str(input('Deseja continuar? [S/N]: '))

print ('\nA soma dos valores digitados foi de: {}'.format(soma))
print ('A quantidade de valores digitados foi de: {}'.format(cont))
print ('A média dos valores digitados foi de: {:.2f}'.format(media))
print ('O maior valor digitado foi: {}'.format(maior))
print ('O menor valor digitado foi: {}'.format(menor))