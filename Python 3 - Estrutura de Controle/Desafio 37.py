n = int(input ('\nDigite um número inteiro: '))
print('\nEscolha uma das bases para fazer a conversão: ')
print('\n[ 1 ] converte para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
e = int(input ('\nSua opção: '))
	
if e == 1:
   b = bin(n)[2:]
   print ('O valor {} em Binário vale: {}'.format(n,b))
elif e == 2:
   b = oct(n)[2:]
   print ('O valor {} em Octal vale: {}'.format(n,b))
elif e == 3:
   b = hex(n)[2:]
   print ('O valor {} em Hexadecimal vale: {}'.format(n,b))
elif e != 1 and e != 2 and e != 3:
   print('Opção inválida!')
