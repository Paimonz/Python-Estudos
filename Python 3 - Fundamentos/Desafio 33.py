'''Faça um programa que keia três números
e mostre qual é o maior e qual é menor'''

n1 = int(input ('\nDigite 1° número: '))
n2 = int(input ('Digite 2° número: '))
n3 = int(input ('Digite 3° número: '))

'''if (n1 > n2) and (n1 > n3):
    print (f'O maior número digitado é: {n1}')
elif (n2 > n1) and (n2 > n3):
    print (f'O maior número digitado é: {n2}')
else:
    print (f'O maior número digitado é: {n3}')'''

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print ('O menor valor digitado foi:{}'.format(menor))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print ('O maior valor digitado foi:{}'.format(maior))
