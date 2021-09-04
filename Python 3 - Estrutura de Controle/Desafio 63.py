print ('\n')
print ('-=-'*15)
print ('Gerando a sequência de Fibonacci')
print ('-=-'*15)

termo = int(input ('Quantos termos você deseja analisar?: '))

n1 = 0
n2 = 1
cont = 1

print ('{}'.format(n1), end=' ')	
while cont != termo:
    p = n1 + n2
    n1 = n2
    n2 = p
    cont += 1
    print ('{}'.format(p), end=' ')
    