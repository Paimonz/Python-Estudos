n = int(input ('Digite um número inteiro:'))

if n % 1 == 0 and n % n == 0 and n % 2 == 1:
    print('O número {} é primo!'.format(n))
else:
    print (' número {} NÃO é primo!'.format(n))
